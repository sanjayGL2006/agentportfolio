import json
import re

# Load 96 certs from earlier
with open(r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\merged_certs.json", "r", encoding="utf-8") as f:
    merged_96 = json.load(f)

# Extra drive IDs from user prompt
user_drive_ids = [
  '101EnojK-vT0ofRpus24ChpMwcdWH-IZO',
  '130a-6aNkI7aFpkshYVmNix87aZ01UHcE',
  '14NdHcaMOp_PZazhdogWEivBFnuxQ48vH',
  '1594kubNx4SjWmslpFmbAXql2DA47uTtS',
  '16Qblc4p_4TJZaArfGaFd9mc6kNkqvBDi',
  '18UlXGYGdSoGRAr_Nc3K9ufm6YCDE5tkm',
  '1ADOYbQnbBXty6o5xvsXDtg6dNca1rupZ',
  '1DkSdN2bxFXmyph2ZH3dr86p-fYWwiDaY',
  '1G_Nus4dXaqf0VPqmshw1aGhlbMiGDaIH',
  '1HVb5L5YXxR38YU8lcw2VYG54gZD-uwvG',
  '1LsdDdH6e1HmUazBPOu3n6SBs-soR7RYo',
  '1R7EuPTZx7IZ7k-YZBWr7LAOL94O7dPaJ',
  '1RVRosZtbOqGHwrh3Kuui-e7CeYWdm4P8',
  '1RrSw1fQ3AnjW5GKWIry2lvtU1Npu146X',
  '1Rut3XME0UEtUBm2szqMxSuPTXE9rvQPt',
  '1Sv8HTIbdCxYf4pCpRsc4fNJ1CNty6HCp',
  '1Tb0rlxqkr8JJPmJpGWgWUvhq0Qi4Jqvs',
  '1YaNypcypvIUuyWW8z_YGPLDHxkUaqfbv',
  '1d4OsQE1h9Z6ygmzd2ljLgZi339CGvk3P',
  '1fb5eR4ho4Ca5Z4knefKxsqrwguU3kcQs',
  '1hKUXoYL5sBiNBJQS1waJsOfXeiBRR8ez',
  '1iT_5RwkR9liECzqi9BKVMNhEE4alRzSo',
  '1nTVsryCXykfBTOK6yeLXC-WOPbN4spGY',
  '1p4NrRfXAt_RJeyw4abjHGHSP_hVMEv-o',
  '1p7IJcaM_n72aonhS4kzXTE3c0pRMta_w',
  '1uMh0IOXelO4yaV4olwvCgusVXlGBjHmM',
  '1w89vGvXCAaSAOl_nbABD4q9isreEhRfY',
  '1xlMToEx0wICuj0DO0V-v5eVhdRG9rSMT',
  '10Vq4__te_q1wvywgIYY_4K0blPOavMx2',
  '10X0Dc2H73UQVjr4U-MVCDC85i2EsOPza',
  '12KVoyJXjFSlezR0KmmgPF8NI6PUjhsQm',
  '12kpcrCqwxr6pXerLfTx-qG2tUG5sL_Q_',
  '15fVZ-fG_TAJ3QtCnssQ78UevlX8F4VB7',
  '16MphtLGwY66nvg4jsP5xA7dXPv7IUrBp',
  '1877ISKlvZJQzSU4BifL2YmrxBv5bhjp5',
  '19slYtiNlnLEISoxdcVURfu8Bh-j5eZtw',
  '1ChT2M3eLGBeToJhNhR9oyPk5_FDB8-jJ',
  '1DFdXmKWOkln0TtwYCOCa--ScSguy0Ge6',
  '1DmLh4jeFLpJ-T2ZyjubCofobbuXcI2Gn',
  '1HxUJJoqbTEKHvs8MRoOu_Dohe-aPkaC8',
  '1IyBlb7kWZuM0dPXhye0XEB97VLqPj1kC',
  '1JgfgUFhCFIHQqosiw9H_f_IoarmSjGSR',
  '1K39PVSnV18lTUFvcog5qc_Vo7nk_D7tZ',
  '1Mnxz57JcjNMeW5j7SpMV4c0JOIrc6p3f',
  '1NqvIvqwazFLo19wHuO2PHnPQ3kw35JDK',
  '1OnGOESlfekUoEvZ56OzlXDhj9ru-QfmI',
  '1P21MYbYAFpijVCYDPFMcOxQbZpAjaHSg',
  '1Xh1NYTGBxVToxpLS5ngiHu6yyR4c7IBI',
  '1Xto3xt5RG2EptLCsuap4brTlRGyiw7gG',
  '1_CYRjPS0KAtxVsVmE_Jl-IltmF6l_VkF',
  '1abdQquiBZSFFWkD1l8k9Rzdrv-1Xnlw5',
  '1b0GV6XlyExJ1Fd0qkuATHeqt887cq4Sa',
  '1fETmYIeOCcBhFnTrrZh4GXZ9Q3mRejdX',
  '1ipYVxar9n7a1ayOeLVQExL1wF9Q5vNqv',
  '1n1cflo3Fg-MyWNkX1eqkQzV6ru4m5Fzg',
  '1oqPDg7U2enLUcCaLuygE7UM6XFqfhvV7',
  '1pE1c-P_VrxYxO72VrMEDH_cCfADTpZ9U',
  '1pLglzX_GC-OhFCoDOK9lEE_-9jbVgIHs',
  '1pf2zSgxW7_OZfcxEsB6wkM_61o2M-Ddp',
  '1sfJv-CTGomeDyZR39of7kU8Qxnhwj0RK',
  '1stEhxu3MUiTfByiaMhe5qYFr-n8BG1EB',
  '1sxOO59k6UwVmHVQfRzVGoD20bj32EvDE',
  '1wkRqKU2HE98FeycskozqgXk40i1fF7hl',
  '1zXArkZNUWyfe9Quz0k6lhWVCcN5rA4rH',
  '1GbYj1y9ao2wGQeXyrp5cTjt4zszK61iM',
  '1PzYpEBBYJvfsExPJy9ksPS4oR88PaTDy',
  '1i-CTvb4kMtdGe7nWxSMxEwKUPssghrhT',
  '1pu_99X1w68I98YhkZIAd8YaeVVuFcWSz',
  '1x0y_iFE7NBF0TUe03u9FHksX1AjA9SmJ'
]

# Extract IDs from the 96 URLs
drive_entries = []
seen_ids = set()

# First add the prompt's 69 IDs
for idx, did in enumerate(user_drive_ids):
    if did not in seen_ids:
        seen_ids.add(did)
        drive_entries.append({
            "driveId": did,
            "title": f"Verified Certificate #{len(drive_entries)+1}",
            "cat": ["drive", "tech"]
        })

# Next add the 96 cert URLs from the earlier prompt if ID is new
with open(r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\certificates_array.js", "r", encoding="utf-8") as f:
    raw_js = f.read()

import json
data_96 = json.loads(raw_js.replace("const CERTIFICATES = ", "").rstrip(";\n"))

for item in data_96:
    url = item.get("url", "")
    match = re.search(r'/d/([^/]+)', url)
    if match:
        did = match.group(1)
        if did not in seen_ids:
            seen_ids.add(did)
            cat_list = ["drive"]
            c_cat = item.get("cat", "")
            if c_cat == "government":
                cat_list.append("government")
            elif c_cat == "internships":
                cat_list.append("internship")
            else:
                cat_list.append("tech")
                
            drive_entries.append({
                "driveId": did,
                "title": item.get("title", f"Verified Certificate #{len(drive_entries)+1}"),
                "cat": cat_list
            })

print(f"Total Unique Drive Certificate Entries: {len(drive_entries)}")
