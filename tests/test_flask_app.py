import sys, os, json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)
print("=== TESTING FLASK APPLICATION ROUTES & SUPABASE INTEGRATION ===")

try:
    from app import app
    app.testing = True
    client = app.test_client()
    
    # 1. Test GET /
    res_home = client.get('/')
    assert res_home.status_code == 200, f"GET / status code: {res_home.status_code}"
    print("[OK] GET / returns 200 OK")

    # 2. Test GET /api/stats
    res_stats = client.get('/api/stats')
    assert res_stats.status_code == 200, f"GET /api/stats status code: {res_stats.status_code}"
    stats_data = json.loads(res_stats.data)
    print(f"[OK] GET /api/stats returns 200 OK: {stats_data}")

    # 2b. Test GET /health
    res_health = client.get('/health')
    assert res_health.status_code == 200, f"GET /health status code: {res_health.status_code}"
    health_data = json.loads(res_health.data)
    assert health_data.get("status") == "healthy"
    print(f"[OK] GET /health returns 200 OK: {health_data}")


    # 3. Test GET /api/projects
    res_proj = client.get('/api/projects')
    assert res_proj.status_code == 200
    proj_data = json.loads(res_proj.data)
    print(f"[OK] GET /api/projects returns 200 OK ({len(proj_data)} projects)")

    # 4. Test GET /api/certificates
    res_cert = client.get('/api/certificates')
    assert res_cert.status_code == 200
    cert_data = json.loads(res_cert.data)
    print(f"[OK] GET /api/certificates returns 200 OK ({len(cert_data)} certificates)")

    # 5. Test POST /chat
    res_chat = client.post('/chat', json={"message": "Hello Sanjay AIOS!"})
    assert res_chat.status_code == 200
    chat_reply = json.loads(res_chat.data)
    print(f"[OK] POST /chat returns 200 OK: {chat_reply.get('reply')[:80]}...")

    print("\nSUCCESS: ALL FLASK APPLICATION ROUTE TESTS PASSED CLEANLY!")

except Exception as e:
    print(f"[FAIL] TEST FAILED: {e}")
    sys.exit(1)
