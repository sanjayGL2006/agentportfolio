# 🚀 Kubernetes Learning Guide & Manifest Architecture

Welcome to the **Kubernetes Learning & Deployment Guide** for the **Sanjay G. L. Portfolio & Sanjay AIOS v2.5** backend application!

---

## 📚 1. What is Kubernetes (K8s)?

**Kubernetes (K8s)** is an open-source container orchestration system that automates the deployment, scaling, load balancing, and management of containerized applications.

### 🌟 Key Benefits of Kubernetes
- **Auto-Healing**: If a container crashes, Kubernetes automatically restarts it or replaces it.
- **Horizontal Scaling**: Scales from 2 to 5+ replicas automatically when CPU or RAM usage spikes.
- **Zero-Downtime Updates**: Performs rolling upgrades so users never experience downtime during code updates.
- **Service Discovery & Load Balancing**: Automatically distributes web traffic across multiple application pods.

---

## 🛠️ 2. Explanation of Kubernetes Files in `k8s/`

Each file in the [`k8s/`](file:///d:/portfolio/k8s) folder represents a specific Kubernetes **Object**:

| File | Kubernetes Resource | Learning Purpose |
|---|---|---|
| [`k8s/namespace.yaml`](file:///d:/portfolio/k8s/namespace.yaml) | `Namespace` | Creates an isolated logical workspace named `portfolio` inside the cluster. |
| [`k8s/configmap.yaml`](file:///d:/portfolio/k8s/configmap.yaml) | `ConfigMap` | Stores non-sensitive environment variables (`PORT`, `FLASK_ENV`, `SUPABASE_URL`). |
| [`k8s/secret.yaml`](file:///d:/portfolio/k8s/secret.yaml) | `Secret` | Stores sensitive API keys (`GEMINI_API_KEY`, `SUPABASE_KEY`, `SUPABASE_SECRET_KEY`). |
| [`k8s/pvc.yaml`](file:///d:/portfolio/k8s/pvc.yaml) | `PersistentVolumeClaim` | Requests 1Gi persistent disk storage for saving SQLite database data across container restarts. |
| [`k8s/deployment.yaml`](file:///d:/portfolio/k8s/deployment.yaml) | `Deployment` | Defines the container image, 2 replica pods, CPU/RAM limits, non-root security rules, and `/health` probes. |
| [`k8s/service.yaml`](file:///d:/portfolio/k8s/service.yaml) | `Service` | Creates an internal cluster IP load balancer mapping port `80` to backend port `5000`. |
| [`k8s/ingress.yaml`](file:///d:/portfolio/k8s/ingress.yaml) | `Ingress` | Configures NGINX reverse proxy rules to route domain traffic (`http://portfolio.local`) to the service. |
| [`k8s/hpa.yaml`](file:///d:/portfolio/k8s/hpa.yaml) | `HorizontalPodAutoscaler` | Dynamically scales pod count between 2 and 5 based on 70% CPU / 80% Memory utilization thresholds. |
| [`k8s/kustomization.yaml`](file:///d:/portfolio/k8s/kustomization.yaml) | `Kustomization` | Packages all YAML files into a single bundle for one-command deployment (`kubectl apply -k k8s/`). |

---

## 🎮 3. `kubectl` Command Cheatsheet for Learners

### A. Deploying & Deleting
```bash
# Deploy all Kubernetes manifests in k8s/
kubectl apply -k k8s/

# Delete all deployed resources in k8s/
kubectl delete -k k8s/
```

### B. Checking Cluster Status
```bash
# List all resources in the portfolio namespace
kubectl get all -n portfolio

# List pods with IP addresses and assigned nodes
kubectl get pods -n portfolio -o wide

# Check Persistent Volume Claim status
kubectl get pvc -n portfolio

# View Horizontal Pod Autoscaler status
kubectl get hpa -n portfolio
```

### C. Troubleshooting & Debugging
```bash
# View live logs of a specific pod
kubectl logs -f <pod-name> -n portfolio

# Inspect detailed events and health status of a pod
kubectl describe pod <pod-name> -n portfolio

# Port-forward service to test on http://localhost:5000
kubectl port-forward svc/sanjay-portfolio-service 5000:80 -n portfolio

# Open interactive bash terminal inside a running pod
kubectl exec -it <pod-name> -n portfolio -- /bin/bash
```

---

## 📦 4. Helm vs Kustomize (How They Differ)

- **Kustomize** (located in [`k8s/kustomization.yaml`](file:///d:/portfolio/k8s/kustomization.yaml)): Built into `kubectl`. It takes raw YAML files and layers configurations on top without modifying original templates.
- **Helm** (located in [`helm/sanjay-portfolio/`](file:///d:/portfolio/helm/sanjay-portfolio)): The package manager for Kubernetes. Uses parameterized Go templates and a `values.yaml` file to install and manage versioned releases (`helm install sanjay-portfolio ./helm/sanjay-portfolio`).

---

## 💻 5. Setting Up Kubernetes on Windows

To run Kubernetes locally on Windows:
1. **Install Docker Desktop for Windows**:
   - Download from [docker.com](https://www.docker.com/products/docker-desktop/).
   - Open Docker Desktop Settings -> **Kubernetes** -> Check **"Enable Kubernetes"** -> Click **Apply & restart**.
2. **Alternative: Minikube**:
   - Install Minikube: `winget install Kubernetes.minikube`
   - Start Minikube cluster: `minikube start`
