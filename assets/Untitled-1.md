Here is an explanation of **how Kubernetes works**, with a focus on **Worker Nodes** and how your portfolio application runs inside them.

---

### 🏗️ 1. High-Level Kubernetes Architecture

A Kubernetes cluster is divided into two main parts:
1. **Control Plane (Master Node)**: The "Brain" of the cluster that makes decisions, schedules pods, and monitors cluster state.
2. **Worker Nodes**: The "Muscle" of the cluster where your application containers (Pods) actually run.

```mermaid
graph TD
    subgraph Control Plane "Control Plane (Master)"
        API[API Server]
        ETCD[(etcd Database)]
        SCHED[Scheduler]
        CM[Controller Manager]
    end

    subgraph WorkerNode1 "Worker Node 1"
        K1[Kubelet]
        KP1[Kube-Proxy]
        CR1[Container Runtime]
        P1["Pod 1 (sanjay-portfolio)"]
        P2["Pod 2 (sanjay-portfolio)"]
    end

    subgraph WorkerNode2 "Worker Node 2"
        K2[Kubelet]
        KP2[Kube-Proxy]
        CR2[Container Runtime]
        P3["Pod 3 (sanjay-portfolio)"]
    end

    API --> K1
    API --> K2
    KP1 <--> Service["k8s/service.yaml"]
    KP2 <--> Service
```

---

### ⚙️ 2. What Happens Inside a Worker Node?

Every **Worker Node** runs three essential components that keep your portfolio application online:

#### A. `kubelet` (The Node Supervisor Agent)
- Receives instructions from the Control Plane API Server.
- Tells the container runtime to pull [`sanjaygl2006/agentportfolio:latest`](file:///d:/portfolio/Dockerfile) and launch Pods.
- Continuously executes the **`livenessProbe`** and **`readinessProbe`** defined in [`k8s/deployment.yaml`](file:///d:/portfolio/k8s/deployment.yaml) by pinging `http://localhost:5000/health`.
- If a container crashes, `kubelet` automatically restarts it.

#### B. Container Runtime (`containerd` / Docker)
- The low-level engine running on the worker node.
- Pulls the Docker image built from [`Dockerfile`](file:///d:/portfolio/Dockerfile), unpacks the Python 3.11 environment, sets up non-root permissions (`appuser`, UID 10001), and runs Gunicorn (`gunicorn --bind 0.0.0.0:5000 app:app`).

#### C. `kube-proxy` (The Network Traffic Controller)
- Manages local network rules on every worker node.
- Directs incoming network traffic from [`k8s/service.yaml`](file:///d:/portfolio/k8s/service.yaml) (Port 80) directly to the correct container IP and port (`5000`).

---

### 🔄 3. Step-by-Step Flow: How Your App Runs on Kubernetes

1. **Deployment Submission**:
   When you run `kubectl apply -k k8s/`, Kubernetes parses [`k8s/deployment.yaml`](file:///d:/portfolio/k8s/deployment.yaml) and requests **2 Pod replicas**.

2. **Scheduling**:
   The Control Plane **Scheduler** chooses the best Worker Nodes with available CPU and RAM.

3. **Pod Creation**:
   The **`kubelet`** on the assigned Worker Node instructs the container runtime to launch the container running [`app.py`](file:///d:/portfolio/app.py).

4. **Storage Mounting**:
   The worker mounts the Persistent Volume from [`k8s/pvc.yaml`](file:///d:/portfolio/k8s/pvc.yaml) to store SQLite data persistently.

5. **Traffic Routing**:
   External HTTP requests hit the **Ingress** ([`k8s/ingress.yaml`](file:///d:/portfolio/k8s/ingress.yaml)), flow through the **Service** ([`k8s/service.yaml`](file:///d:/portfolio/k8s/service.yaml)), and get load-balanced by **`kube-proxy`** across active worker Pods.

6. **Auto-Scaling (HPA)**:
   If website traffic increases, the **HorizontalPodAutoscaler** ([`k8s/hpa.yaml`](file:///d:/portfolio/k8s/hpa.yaml)) instructs the Control Plane to add more worker Pods (up to 5 replicas) to distribute load.

Viewed docker-compose.yml:1-22
Ran command: `python app.py`