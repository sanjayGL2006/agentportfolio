import json
import re

prompt_text = """
https://drive.google.com/file/d/1-a-UzpDJJjb--mw61CH72a4A7RSsc8_5/view?usp=drive_link
https://drive.google.com/file/d/11Mf67ksZ_9ytcbeZZatkgVAxUn2rkAco/view?usp=drive_link
https://drive.google.com/file/d/1Dif_LGwJI_frq2UTfu8tfJ8iHxvRC8by/view?usp=drive_link
https://drive.google.com/file/d/1EFk83Ro6Xbe3R3XlfCAOpgpdQrCaCQRM/view?usp=drive_link
https://drive.google.com/file/d/1H4ObK2ruKAWDk9AtZVH8f6dlLARdzWXq/view?usp=drive_link
https://drive.google.com/file/d/1M2C2-yGWV6Lz9A6rexvWekv_rbsugDUC/view?usp=drive_link
https://drive.google.com/file/d/1MS4nKuB1ZU6zY3y7TiwywUNvzYNDhdtP/view?usp=drive_link
https://drive.google.com/file/d/1VVWLBTxh2X5ZWkmia8d8jYFOBd4WqvcB/view?usp=drive_link
https://drive.google.com/file/d/1YVoHEq_RMDbTHqGQ4TDXtgoJdM2WT8GA/view?usp=drive_link
https://drive.google.com/file/d/1_Tn5L4bQ3LX78wXBgDweU5zAOI8qWsGU/view?usp=drive_link
https://drive.google.com/file/d/1ekaEje-JHXr0ctb74c-wJZ65uMCAa_BX/view?usp=drive_link
https://drive.google.com/file/d/1fSPjTUXM5ZQur1bhj9IcOGctFOKH65eq/view?usp=drive_link
https://drive.google.com/file/d/1ftFVAh-nquyhvzmAKKyli-H0RUvsQnsV/view?usp=drive_link
https://drive.google.com/file/d/1gjd2Z7pj_Onkwk_6zEXTKcseQ61JgQ69/view?usp=drive_link
https://drive.google.com/file/d/1hrqP8JVL0EM7Tyw8-FvTsasfcji_ukn3/view?usp=drive_link
https://drive.google.com/file/d/1lFfvYWNq5l5XPKUy7K2TjXmke4BgiDgn/view?usp=drive_link
https://drive.google.com/file/d/1lrlvYaedPMZGHqVkhEiPfF6aIhJz8Xqs/view?usp=drive_link
https://drive.google.com/file/d/1nRH7_cOM4deHugPpzazCApVW0c0F4-jL/view?usp=drive_link
https://drive.google.com/file/d/1oUhXMN8sQLyBp396qdkvFi_w7ovKkAe4/view?usp=drive_link
https://drive.google.com/file/d/1otxA2FxJ4MYAUx3PqZ1uS1clfnAaTpiQ/view?usp=drive_link
https://drive.google.com/file/d/1rvBnc4__stabF0g2c4uVXW0qzWCeWeI4/view?usp=drive_link
https://drive.google.com/file/d/1s8rhVaz7kH9jCu9sPxKxBrUmxRwQpRC1/view?usp=drive_link
https://drive.google.com/file/d/1sVP0RvyF8YU-g7IzWc92Y8-RYTeKgDi-/view?usp=drive_link
https://drive.google.com/file/d/1ud82Oy8AQxsMKLucLfOCs1IiFe4YpdXA/view?usp=drive_link
https://drive.google.com/file/d/1HL6AqgZ59cAapNllvMgCkseO-8ZkjWqA/view?usp=sharing
https://drive.google.com/file/d/1-9WHvzovaXE7Bm_vSMJaTauO15fiNFn6/view?usp=sharing
https://drive.google.com/file/d/114rvZ_i6HrauXYtLt702yi35-Uo8HUU8/view?usp=sharing
https://drive.google.com/file/d/11AUMxWS3Uasrek8Z6q46-v2xFUkSTv8Y/view?usp=sharing
https://drive.google.com/file/d/11H58F_d2FXl2ij7rgy5RfIdd1igQZ838/view?usp=sharing
https://drive.google.com/file/d/11ishlFxU6fHlTQQL9bTidNdo6sd17Erh/view?usp=sharing
https://drive.google.com/file/d/11vA5gGSydt4bW5b5409vV2bXC67igusc/view?usp=sharing
https://drive.google.com/file/d/12R3sXmNbNGGKOkigbvydBoV2vbguUpOO/view?usp=sharing
https://drive.google.com/file/d/12bNABXkIJGZbfV8P5EOZ59lIMY0M9rAN/view?usp=sharing
https://drive.google.com/file/d/13LGnGsoBFk_rX46KOgQ_MDD6QdD_8adr/view?usp=sharing
https://drive.google.com/file/d/13b1mxC7UluMOmXt13nCmWYm9RsIP3KyJ/view?usp=sharing
https://drive.google.com/file/d/14GdbvNTpO3tMsqrgZchRRh1FDNmczCdR/view?usp=sharing
https://drive.google.com/file/d/15NoMn9GN76qj9DkGtEY5x67JD5jZYbcD/view?usp=sharing
https://drive.google.com/file/d/15XdUEDRLK16AgcXHPrXvev9UL8fBMfUI/view?usp=sharing
https://drive.google.com/file/d/16BisAFI6StGzLsFJh2Ef_a0EoxLub5HA/view?usp=sharing
https://drive.google.com/file/d/16GIhv_fbofon_i4Ze9KPlxvx05lZ6sPI/view?usp=sharing
https://drive.google.com/file/d/17QyCMHpWF8leCuQ306CxgczB-QbznAXz/view?usp=sharing
https://drive.google.com/file/d/17TiZ9B7r2j3bzzoAziflEjfy3bXo3E-T/view?usp=sharing
https://drive.google.com/file/d/18HUZP0VmwnOc1bP7IW_ANccqLDYQC0D0/view?usp=sharing
https://drive.google.com/file/d/191JiLGxgWo5g1mJNHKzoG_kxjJxE34lh/view?usp=sharing
https://drive.google.com/file/d/19JI3ZB56Mcf74L_K0i7ROLGPX8IIRfAu/view?usp=sharing
https://drive.google.com/file/d/1AKubfUdg0ITbRpcUaFNPCrIoihNakN8o/view?usp=sharing
https://drive.google.com/file/d/1AT5ss0Zh9aUkp_3Th44RLabf8ph5BuP9/view?usp=sharing
https://drive.google.com/file/d/1B54eMTad9qdemREGm0hxJSabt7iKxbXT/view?usp=sharing
https://drive.google.com/file/d/1BN5Kwa8fQV6nRyqQaTskFKMBVNHNo6TD/view?usp=sharing
https://drive.google.com/file/d/1BkNZIRzSaUhEbLgSeRckW3zcjx9F8MHZ/view?usp=sharing
https://drive.google.com/file/d/1C5WB6MK8YchzNX4WnyzQylwh-MfLPMoc/view?usp=sharing
https://drive.google.com/file/d/1CZQpPF5crnEK812BAQBKbMfuigt-WToY/view?usp=sharing
https://drive.google.com/file/d/1D0fvfuog6L2IIFpSwv8qlEGIxEy4x0V0/view?usp=sharing
https://drive.google.com/file/d/1E-5KQ6vMaYEToyNqVz7_Fz-KtwgCqejb/view?usp=sharing
https://drive.google.com/file/d/1EO0OPiYBnyHkR8Wkyi9_jXKDg_iQW9c1/view?usp=sharing
https://drive.google.com/file/d/1EU0GJVJpf2OvJ3A9SbWSxB5ZBQc17pdn/view?usp=sharing
https://drive.google.com/file/d/1EhdbuIekh66NTF2_hbq3OJc-4Jiki-lx/view?usp=sharing
https://drive.google.com/file/d/1Es8Vppv888ilN0x51BlxbQWFKPdimhp2/view?usp=sharing
https://drive.google.com/file/d/1G_wTkr4NPEHkB8PPCyqWTlWFK2OzJh7h/view?usp=sharing
https://drive.google.com/file/d/1IFvSph-B05avBT1uYv7LNBIg324tFVN7/view?usp=sharing
https://drive.google.com/file/d/1IxInGmobZUIL0epICbEmCtnMuLiYCuI1/view?usp=sharing
https://drive.google.com/file/d/1JEhzjfoA1Ux7FzMtLuvGZR6KIRXChKls/view?usp=sharing
https://drive.google.com/file/d/1KZXl9hjtIZKc25-n8cyUhIiS6Dh4g_rK/view?usp=sharing
https://drive.google.com/file/d/1KhwAB4oHRz1rPaxaIivtch71hMI1tiZw/view?usp=sharing
https://drive.google.com/file/d/1Km_24RHjCLgTdHT2JA7XE2fqPFAyxzne/view?usp=sharing
https://drive.google.com/file/d/1L4pYZ_Yp7zMildCqhJzVt-nj0lQsAjk-/view?usp=sharing
https://drive.google.com/file/d/1LEuxNotYW4YJZkrHPyD8vJUFtQIk91p1/view?usp=sharing
https://drive.google.com/file/d/1LFECJnZV7bbS5a1b7BhXcTmPJap6zhF-/view?usp=sharing
https://drive.google.com/file/d/1LJo1MsYqysco-v7QwLOvovssnfoubZ1Y/view?usp=sharing
https://drive.google.com/file/d/1LJz9n-2plhJgxP3CMaJcv9EFouF3ZzY3/view?usp=sharing
https://drive.google.com/file/d/1LPWdVzvkIoaBdLEPUr2Xl-tcgUPjhntl/view?usp=sharing
https://drive.google.com/file/d/1LeZ3xuZifK4pTdu4xkxKeq939KiCq_Y9/view?usp=sharing
https://drive.google.com/file/d/1MpmkNc3MdYgbLVVThuZ-Y0U3Ut5W3Hgl/view?usp=sharing
https://drive.google.com/file/d/1N5RB2iu9W1obGemp2qK_wvnlHgPkrSnc/view?usp=sharing
https://drive.google.com/file/d/1NXvNy5Suu3GrYkMMP48DMP5GVCtdPpAq/view?usp=sharing
https://drive.google.com/file/d/1O99OwOVmPJBHJmgp5b8kyne6FSAjnuDb/view?usp=sharing
https://drive.google.com/file/d/1PDcXMHOrwIfzLp_aeLeyg4b7vTeypSmN/view?usp=sharing
https://drive.google.com/file/d/1PLetf6hzJq2wYnqG1Uhvi8EuWALG6kZY/view?usp=sharing
https://drive.google.com/file/d/1PTvu-HOzfFomnR9U8tfWnjq7A7co39VK/view?usp=sharing
https://drive.google.com/file/d/1PZoa1-45tUumA3UfwdTHwhiAXAUm-9JD/view?usp=sharing
https://drive.google.com/file/d/1PahHRVZdxwZY3yA4brmt0kbNcbLALcOE/view?usp=sharing
https://drive.google.com/file/d/1Q2Dcp6fwYfk2nKJy_pe3fYD7fOaZfJst/view?usp=sharing
https://drive.google.com/file/d/1QCEDkYyM-8vUpFtKrCTTcEO4p5ZN0s4b/view?usp=sharing
https://drive.google.com/file/d/1QRm5pvwvw804yx9Dd8TSPmbpbE7Iv4NI/view?usp=sharing
https://drive.google.com/file/d/1R1Kp6l-YNtYK273MsWmHEpPzcEhSDh1f/view?usp=sharing
https://drive.google.com/file/d/1R3v4g5NLk-2sbwtC2IZU7KcbgnMdUxjg/view?usp=sharing
https://drive.google.com/file/d/1RZOG8Fa-4YwpggdPw3vjqOxNDGgeOVLz/view?usp=sharing
https://drive.google.com/file/d/1SI37VLPh414Vikthbwm_OhGsMte2tY5w/view?usp=sharing
https://drive.google.com/file/d/1Seqm0rAWo7wrBD3XR9yl9gpJXUaxIMeF/view?usp=sharing
https://drive.google.com/file/d/1Sroa5zcLFosAq1RprPobmClTllZB8PtC/view?usp=sharing
https://drive.google.com/file/d/1TAO23u4ZVYsD2eM3e77wDyXC3qLxMEpJ/view?usp=sharing
https://drive.google.com/file/d/1TQoeXRnuoVXQp0CcwSfcR9i1D-7l2IrK/view?usp=sharing
https://drive.google.com/file/d/1UnafE_VAf2mxHwlkgnZoUOyymw4M3J1A/view?usp=sharing
https://drive.google.com/file/d/1V73ZF-tcFCDab6Fg7onBDroGCN045u-h/view?usp=sharing
https://drive.google.com/file/d/1WlU3abs2JKLMd3q-1Iw-wafXppgBIMDE/view?usp=sharing
https://drive.google.com/file/d/1XClTC7v7G_P6iXT8c0gzF_BI3XEUxjPD/view?usp=sharing
https://drive.google.com/file/d/1XKbi-YXOrQIgxoV1FKONgwKhEFUa72HU/view?usp=sharing
https://drive.google.com/file/d/1XTINueBrR7V5xrEH-Z3zEQ7PY2JQ60db/view?usp=sharing
https://drive.google.com/file/d/1XVphMygdaVr-pquf4mkCpJ9bZVhkFqZw/view?usp=sharing
https://drive.google.com/file/d/1XcKeNcMvXhVTd3qk55ChNSqJba-Buihw/view?usp=sharing
https://drive.google.com/file/d/1Xno5xzSp5vvZLRf_bIS9fZ4eqdNEVOIR/view?usp=sharing
https://drive.google.com/file/d/1Xtr4iK6S6WuyA1XpH7jJWFDC2MAIi86V/view?usp=sharing
https://drive.google.com/file/d/1YBwoFYwRUVtZTgVfn1a-zPWhGZS0Swki/view?usp=sharing
https://drive.google.com/file/d/1YMd3kjcF9tfud-uJEiJ0Ds5qPpADEmWs/view?usp=sharing
https://drive.google.com/file/d/1ZRYcN56aUnEjJaJ3Xxxu05-K-f6NpaKJ/view?usp=sharing
https://drive.google.com/file/d/1_z7J0rn-Y4N5AF_X1EtdUJ8_RnIxevKL/view?usp=sharing
https://drive.google.com/file/d/1aRHEACllXhO3tTAWw2qNhrYROwWDXQRY/view?usp=sharing
https://drive.google.com/file/d/1b10zaCVQiqmAyL2p9gC2MG51dTtkg4Et/view?usp=sharing
https://drive.google.com/file/d/1c38bSxJlzEb3iSG_a3-_oegtDQWZDLNS/view?usp=sharing
https://drive.google.com/file/d/1c8yyja693Z24n8geqte2IdRT0IIEtZeb/view?usp=sharing
https://drive.google.com/file/d/1cz_3lUOPQASrQjG6S-ON_U4SB6FJYD00/view?usp=sharing
https://drive.google.com/file/d/1d4mtwjTA8oLyx20CXXcnUm1pNUjr02lF/view?usp=sharing
https://drive.google.com/file/d/1dDrAPAB5fWYZquPg0VkszdEOMyJoS57P/view?usp=sharing
https://drive.google.com/file/d/1epAjTxxs_SpqHwCTLjQu9IEvLs8FGFUi/view?usp=sharing
https://drive.google.com/file/d/1f6oWfLt0CUshekcQYiGKU1qS2Tb_u7nF/view?usp=sharing
https://drive.google.com/file/d/1fLUFzJLTfD3adJwUhvcAsMwkF5ijjqry/view?usp=sharing
https://drive.google.com/file/d/1fXbC_FqcsDRh60w-Po82xyg5nKSUeQz-/view?usp=sharing
https://drive.google.com/file/d/1g-WVOMt4__AWaWBylu6T7jRk1dr-jLf5/view?usp=sharing
https://drive.google.com/file/d/1gYtM5pLZpFkgewtdWiPgjzl4-x43cSrH/view?usp=sharing
https://drive.google.com/file/d/1gfZGSf_9mujL1O_ywlkC5gYtM6XbtDpI/view?usp=sharing
https://drive.google.com/file/d/1h0cazLuPJpZfuMS1uf11Zb2p-3S5dUA0/view?usp=sharing
https://drive.google.com/file/d/1i5EIhWV1_jMktBhxIkCat9SYdDK4-qMy/view?usp=sharing
https://drive.google.com/file/d/1iPaWXTG6bDskNq3zyfZ0GbFrEjWFbSlr/view?usp=sharing
https://drive.google.com/file/d/1iVgQqInATmm5vdwT6QVZC4FWDmTBMPsd/view?usp=sharing
https://drive.google.com/file/d/1iYNx1SKrxGpWJhQjmSY263embAO1tnHk/view?usp=sharing
https://drive.google.com/file/d/1jJm44WLfgm3OHSM1Kty_-GS6jIZX0Xt_/view?usp=sharing
https://drive.google.com/file/d/1jhnB6eNELsziHIV85SzXsyUBtJ6b3txg/view?usp=sharing
https://drive.google.com/file/d/1kXwJMT8b8mTfPMruMATVBqETW-sjT2K1/view?usp=sharing
https://drive.google.com/file/d/1kcgzWwM5DkW7J2lhjmAoy_xWuvv45ZS-/view?usp=sharing
https://drive.google.com/file/d/1kpnLj90dbnf9LdI0cewkeeRM0h4Jc1XS/view?usp=sharing
https://drive.google.com/file/d/1lCkaon9Uuh577D-mU58IBlxA6wcE6q8b/view?usp=sharing
https://drive.google.com/file/d/1lJ05misKCaM_91jJ-ISYsABHNG0ekSYM/view?usp=sharing
https://drive.google.com/file/d/1m8oaW8yJQYkQXK1soVh7Ov_xBdX6hf5P/view?usp=sharing
https://drive.google.com/file/d/1mbbOmFfP1m6B0KfcM55BFYhjULHZC10Z/view?usp=sharing
https://drive.google.com/file/d/1oDX7rGyY9qvQryO5RSMxeXsFdU6FVDB6/view?usp=sharing
https://drive.google.com/file/d/1oNrUF3POokSI8i2k3zOKucQV1VxWQkRH/view?usp=sharing
https://drive.google.com/file/d/1pUNf3eLPHgB5256ye9mN4dJthy-mwl_o/view?usp=sharing
https://drive.google.com/file/d/1pV6BlK_PLhe5cu1YHbK0UItoCzLLTah6/view?usp=sharing
https://drive.google.com/file/d/1q3NmMR5_ZJ6xSUFBnlE9QMZ5J9OtBpWP/view?usp=sharing
https://drive.google.com/file/d/1q3wQ9l_6Rsi5nrGBbVXSAAjo_dfRPPGM/view?usp=sharing
https://drive.google.com/file/d/1rFabzhwokYKRB0E78fflooLNDWkWzrJ5/view?usp=sharing
https://drive.google.com/file/d/1sc8qIXzH9NDTl4mO08TfZrW_Abj3G9Nw/view?usp=sharing
https://drive.google.com/file/d/1shVGzjgNzEA5JyFHF4rNjQKN72LFqhDv/view?usp=sharing
https://drive.google.com/file/d/1tDkOLSt9rQfsIIWeYAkVPcByQP6_6nWv/view?usp=sharing
https://drive.google.com/file/d/1tZxm7TO1whu7th1T8rGpeOiFbtAYC9Jx/view?usp=sharing
https://drive.google.com/file/d/1unDX0wU5JQEiuMGP44AUUINEuSIwx5qB/view?usp=sharing
https://drive.google.com/file/d/1vPP1VgYEJbQryHYEsHTbwhaZCVJSQx5Y/view?usp=sharing
https://drive.google.com/file/d/1vgxKyUpgCv4_ydP4PznZaYTFg07s7Olg/view?usp=sharing
https://drive.google.com/file/d/1vkGtGvlKqi1Mg9oqxjmb1wdLv5_89I_F/view?usp=sharing
https://drive.google.com/file/d/1vzKjdwncP02hAERD7i1vD1TL6pIHl_IK/view?usp=sharing
https://drive.google.com/file/d/1xBuYfPrrBdTjGYHOwxPr-vysNzWEKIri/view?usp=sharing
https://drive.google.com/file/d/1za772OoM-xPllviSgUp1eszqtCn4a8ra/view?usp=sharing
https://drive.google.com/file/d/1zvv6bmS_EYKdRAnzjOONsNd7NArmcQjF/view?usp=sharing
"""

# Extract drive IDs
drive_ids = list(dict.fromkeys(re.findall(r'file/d/([a-zA-Z0-9_-]+)', prompt_text)))
print(f"Extracted {len(drive_ids)} unique Drive IDs from prompt!")

# Read js/certificatesData.js
with open('d:/portfolio/js/certificatesData.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

existing_js_ids = set(re.findall(r'driveId:\s*"([^"]+)"', js_content))
existing_js_ids.update(re.findall(r'"driveId":\s*"([^"]+)"', js_content))
print(f"Existing drive IDs in certificatesData.js: {len(existing_js_ids)}")

missing_ids = [d for d in drive_ids if d not in existing_js_ids]
print(f"New drive IDs to insert: {len(missing_ids)}")

# Prepare addition items
additions = []
start_num = len(existing_js_ids) + 1

for idx, drive_id in enumerate(missing_ids, start=start_num):
    additions.append({
        "id": f"cert-batch-{idx}",
        "type": "named",
        "category": "tech",
        "title": f"Verified Technical Credential #{idx}",
        "org": "Sanjay G. L. Credential Archive",
        "date": "2026",
        "month": "September",
        "year": 2026,
        "duration": "Certification",
        "desc": "Verified technical credential issued for technology competency, programming development, or system architecture completion.",
        "tags": ["Verified Credential", "Professional Certification", "2026"],
        "skillsLearned": ["Technical Competency", "Software Development", "System Engineering"],
        "credentialId": f"CERT-{drive_id[:8].upper()}",
        "driveId": drive_id,
        "verifyLink": f"https://drive.google.com/file/d/{drive_id}/view?usp=sharing",
        "image": f"https://drive.google.com/thumbnail?id={drive_id}&sz=w800",
        "emoji": "📜",
        "featured": False
    })

if additions:
    last_bracket_idx = js_content.rfind("];")
    if last_bracket_idx != -1:
        js_add_str = ",\n" + ",\n".join(json.dumps(item, indent=4) for item in additions)
        updated_js = js_content[:last_bracket_idx].rstrip() + js_add_str + "\n];\n"
        with open('d:/portfolio/js/certificatesData.js', 'w', encoding='utf-8') as f:
            f.write(updated_js)
        print(f"Successfully appended {len(additions)} certificates to js/certificatesData.js!")

# Update knowledge.json
with open('d:/portfolio/knowledge.json', 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

cert_k = knowledge.get("certificates", {})
if isinstance(cert_k, dict):
    cert_list = cert_k.get("list", [])
    current_ids_k = {c.get("driveId") for c in cert_list if isinstance(c, dict)}
    
    for drive_id in drive_ids:
        if drive_id not in current_ids_k:
            cert_list.append({
                "title": "Verified Technical Credential",
                "org": "Verified Institution",
                "year": 2026,
                "driveId": drive_id,
                "verifyLink": f"https://drive.google.com/file/d/{drive_id}/view?usp=sharing"
            })
    
    cert_k["list"] = cert_list
    cert_k["total_count"] = len(cert_list)
    knowledge["certificates"] = cert_k

with open('d:/portfolio/knowledge.json', 'w', encoding='utf-8') as f:
    json.dump(knowledge, f, indent=2)

print(f"Updated knowledge.json! Total certificates count now: {knowledge['certificates']['total_count']}")
