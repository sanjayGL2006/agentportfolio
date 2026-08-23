import json
import re

merged_path = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\merged_certs.json"
with open(merged_path, "r", encoding="utf-8") as f:
    records = json.load(f)

parsed_certs = []

def clean_text(t):
    return " ".join(t.split())

for r in records:
    fn = r.get("filename", "")
    txt = clean_text(r.get("text", ""))
    url = r.get("url", "")

    # Default fallbacks
    title = ""
    org = ""
    cat = "coding"
    icon = "fa-solid fa-certificate"

    comb = (fn + " " + txt).lower()

    # Determine Org
    if "microsoft" in comb or "sanjaygl-6060" in comb:
        org = "Microsoft"
    elif "google" in comb or "coursera" in comb:
        org = "Google"
    elif "nss" in comb:
        org = "NSS / Govt. of Karnataka"
    elif "my bharat" in comb or "my_bharat" in comb or "mybharat" in comb:
        org = "Govt. of India (MY Bharat)"
    elif "cisco" in comb or "netacad" in comb:
        org = "Cisco Networking Academy"
    elif "tryhackme" in comb:
        org = "TryHackMe"
    elif "hackerrank" in comb:
        org = "HackerRank"
    elif "ibm" in comb:
        org = "IBM"
    elif "infosys" in comb or "springboard" in comb:
        org = "Infosys Springboard"
    elif "great learning" in comb:
        org = "Great Learning"
    elif "guvi" in comb:
        org = "GUVI / IIT Madras"
    elif "pes" in comb or "pesiams" in comb or "iams" in comb:
        org = "PESIAMS Shivamogga"
    elif "nptel" in comb or "swayam" in comb:
        org = "NPTEL / Swayam"
    elif "simplilearn" in comb or "skillup" in comb:
        org = "Simplilearn"
    elif "forage" in comb:
        org = "Forage"
    elif "ec-council" in comb or "eccouncil" in comb:
        org = "EC-Council"
    elif "udemy" in comb:
        org = "Udemy"
    elif "sololearn" in comb:
        org = "SoloLearn"
    else:
        org = "Verified Issuer"

    # Category matching
    if "cyber" in comb or "security" in comb or "ethical hacking" in comb or "pen testing" in comb or "network" in comb or "cryptography" in comb:
        cat = "cybersecurity"
        icon = "fa-solid fa-shield-halved"
    elif "python" in comb:
        cat = "python"
        icon = "fa-brands fa-python"
    elif "ai" in comb or "machine learning" in comb or "artificial intelligence" in comb or "prompt engineering" in comb or "deep learning" in comb or "generative" in comb:
        cat = "ai"
        icon = "fa-solid fa-brain"
    elif "nss" in comb or "bharat" in comb or "government" in comb or "govt" in comb or "seva" in comb or "youth" in comb or "election" in comb or "voter" in comb:
        cat = "government"
        icon = "fa-solid fa-landmark"
    elif "internship" in comb or "intern" in comb or "trainee" in comb or "forage" in comb:
        cat = "internships"
        icon = "fa-solid fa-briefcase"
    elif "hackathon" in comb or "competition" in comb or "contest" in comb or "winner" in comb or "finalist" in comb or "quiz" in comb or "rank" in comb:
        cat = "competitions"
        icon = "fa-solid fa-trophy"
    elif "workshop" in comb or "bootcamp" in comb or "seminar" in comb or "webinar" in comb or "training" in comb:
        cat = "workshops"
        icon = "fa-solid fa-chalkboard-user"
    else:
        cat = "coding"
        icon = "fa-solid fa-code"

    parsed_certs.append({
        "index": r["index"],
        "fn": fn,
        "txt_snippet": txt[:120],
        "cat": cat,
        "org": org,
        "icon": icon,
        "url": url
    })

out_parsed = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\parsed_certs_summary.json"
with open(out_parsed, "w", encoding="utf-8") as f:
    json.dump(parsed_certs, f, indent=2)

print("Parsed certs summary written.")
