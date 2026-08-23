import sys
import os
import json
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)

def run_tests():
    print("==========================================================")
    print("      RUNNING FULL PORTFOLIO PROJECT TEST SUITE           ")
    print("==========================================================\n")

    from app import app
    app.testing = True
    client = app.test_client()
    passed = 0
    failed = 0

    def test(name, condition, detail=""):
        nonlocal passed, failed
        if condition:
            print(f" [PASS] {name} {f'- {detail}' if detail else ''}")
            passed += 1
        else:
            print(f" [FAIL] {name} {f'- {detail}' if detail else ''}")
            failed += 1

    # 1. Page Routes
    print("--- 1. Testing Page Routes ---")
    r_home = client.get('/')
    test("GET / (Index Page)", r_home.status_code == 200, f"Status: {r_home.status_code}")
    home_html = r_home.data.decode('utf-8')
    test("Index HTML Title Present", "<title>" in home_html, "Found <title>")
    test("Index HTML Meta Tags Present", '<meta name="description"' in home_html, "Found meta description")
    test("No cursor.js script in index.html", "js/cursor.js" not in home_html, "Cursor script removed")

    r_proj = client.get('/projects.html')
    test("GET /projects.html", r_proj.status_code == 200, f"Status: {r_proj.status_code}")
    proj_html = r_proj.data.decode('utf-8')
    test("No cursor.js script in projects.html", "js/cursor.js" not in proj_html, "Cursor script removed")

    r_cert = client.get('/certificates.html')
    test("GET /certificates.html", r_cert.status_code == 200, f"Status: {r_cert.status_code}")
    cert_html = r_cert.data.decode('utf-8')
    test("No cursor.js script in certificates.html", "js/cursor.js" not in cert_html, "Cursor script removed")

    r_priv = client.get('/privacy.html')
    test("GET /privacy.html", r_priv.status_code == 200, f"Status: {r_priv.status_code}")
    priv_html = r_priv.data.decode('utf-8')
    test("Privacy Policy HTML Title Present", "<title>" in priv_html, "Found <title>")

    # 2. Dynamic JS Data Routes
    print("\n--- 2. Testing Data Routes ---")
    r_pdata = client.get('/js/projectsData.js')
    test("GET /js/projectsData.js", r_pdata.status_code == 200 and "PROJECTS_DATA" in r_pdata.data.decode('utf-8'))
    
    r_cdata = client.get('/js/certificatesData.js')
    test("GET /js/certificatesData.js", r_cdata.status_code == 200 and "CERTIFICATES_DATA" in r_cdata.data.decode('utf-8'))

    # 3. Static Assets & SEO Files
    print("\n--- 3. Testing Static Assets & SEO ---")
    r_css = client.get('/css/styles.css')
    test("GET /css/styles.css", r_css.status_code == 200 and len(r_css.data) > 1000)

    r_manifest = client.get('/manifest.json')
    test("GET /manifest.json", r_manifest.status_code == 200)

    r_robots = client.get('/robots.txt')
    test("GET /robots.txt", r_robots.status_code == 200)

    r_sitemap = client.get('/sitemap.xml')
    test("GET /sitemap.xml", r_sitemap.status_code == 200)

    # 4. API Endpoints
    print("\n--- 4. Testing API Endpoints ---")
    r_stats = client.get('/api/stats')
    test("GET /api/stats Status", r_stats.status_code == 200)
    if r_stats.status_code == 200:
        stats = json.loads(r_stats.data)
        test("API Stats Projects Count", stats.get("projects") == 28, f"Count: {stats.get('projects')}")
        test("API Stats Certificates Count", stats.get("certificates") == 86, f"Count: {stats.get('certificates')}")

    r_about = client.get('/api/about')
    test("GET /api/about Status", r_about.status_code == 200)
    if r_about.status_code == 200:
        about = json.loads(r_about.data)
        test("API About Email", about.get("email") == "sanjaygl2006@gmail.com", f"Email: {about.get('email')}")

    # 5. Interactive Form & Agent Routes
    print("\n--- 5. Testing Interactive Form & AI Agent ---")
    r_contact = client.post('/api/contact', json={
        "name": "Integration Test Runner",
        "email": "testrunner@example.com",
        "subject": "Full Test Suite Run",
        "message": "Testing complete portfolio form submission & email delivery logic."
    })
    test("POST /api/contact Status", r_contact.status_code == 200, f"Status: {r_contact.status_code}")
    if r_contact.status_code == 200:
        contact_res = json.loads(r_contact.data)
        test("POST /api/contact Response Success", contact_res.get("status") in ["success", "partial"], contact_res.get("message"))

    r_agent = client.post('/api/agent', json={
        "message": "What projects has Sanjay built?",
        "session_id": "test_session_001"
    })
    test("POST /api/agent Status", r_agent.status_code == 200, f"Status: {r_agent.status_code}")
    if r_agent.status_code == 200:
        agent_res = json.loads(r_agent.data)
        test("POST /api/agent Reply Present", "reply" in agent_res and len(agent_res["reply"]) > 5)

    print("\n==========================================================")
    print(f"      TEST RESULTS: {passed} PASSED, {failed} FAILED     ")
    print("==========================================================")

    assert failed == 0, f"{failed} test(s) failed"

def test_full_project():
    run_tests()

if __name__ == "__main__":
    run_tests()
