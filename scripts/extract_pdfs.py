import urllib.request
import re
import ssl
import json
import os
import concurrent.futures
from pypdf import PdfReader

urls = [
    "https://drive.google.com/file/d/1-8vlFb8yc5f-75UT-QQfIqD4JMFGqt1h/view?usp=sharing",
    "https://drive.google.com/file/d/1-L38L9BUDCu4VUJ5EIce_XhSV2v2ye4u/view?usp=sharing",
    "https://drive.google.com/file/d/10-hk5wBRsMyFM1l-TDbIRDwkkSY95t2q/view?usp=sharing",
    "https://drive.google.com/file/d/107VX9Fm7p8BC5KqtAgcNzSvjush6jojn/view?usp=sharing",
    "https://drive.google.com/file/d/10_bXPiY61DOfO80JCCVA90HekvacNu8P/view?usp=sharing",
    "https://drive.google.com/file/d/12ESuKNWaY74SOox4TgXZhqOZ2_dpszg-/view?usp=sharing",
    "https://drive.google.com/file/d/12FfoBj33hsQ-tXD1rGp0UEIQIC84MGuh/view?usp=sharing",
    "https://drive.google.com/file/d/12eZFsMPUG0EA46sGRMqDLKduQCP-BMry/view?usp=sharing",
    "https://drive.google.com/file/d/13D2dbLhCL-eNlpQfJeviYKe2XZWSRSnK/view?usp=sharing",
    "https://drive.google.com/file/d/17-3D0VFRQIPewrjwF2s3PJWVOVFWrcjc/view?usp=sharing",
    "https://drive.google.com/file/d/18xJnFWhEI29Cr7dmw1VRoV-8Gg9iuK0P/view?usp=sharing",
    "https://drive.google.com/file/d/19kO2mnjt5X4a4qWJfhfhovZnuMXaH5y6/view?usp=sharing",
    "https://drive.google.com/file/d/19tI2hT0kFgW39QHMAXRpFDrjqyXql1nJ/view?usp=sharing",
    "https://drive.google.com/file/d/1A2qcI_R_XUdHGCvQ6H2s14yrlGW5Su6J/view?usp=sharing",
    "https://drive.google.com/file/d/1AuaHR5rUdHrOajrTN-R3pO_KKK1rGs03/view?usp=sharing",
    "https://drive.google.com/file/d/1CM5hBJGy0YXnPxRO-7_Ckp752TaiCNFF/view?usp=sharing",
    "https://drive.google.com/file/d/1DYVbdydpVeue7ALlbgBhmt7dTKHut1c6/view?usp=sharing",
    "https://drive.google.com/file/d/1Dk5TfiaT3BHQmZimaMydJUCw1_0FjRLF/view?usp=sharing",
    "https://drive.google.com/file/d/1DlKD1aXq6bmWjG6h6x4LEOj2WAmOAG3y/view?usp=sharing",
    "https://drive.google.com/file/d/1Ev6wBrNmYhsraaOL2VUubPIpqhlBtVQQ/view?usp=sharing",
    "https://drive.google.com/file/d/1FF2h55xWlvz5GTZ42St7P8wPobN6BX5w/view?usp=sharing",
    "https://drive.google.com/file/d/1FrObW8f-cLRoPGlUfEzHOyD6AeczPG_X/view?usp=sharing",
    "https://drive.google.com/file/d/1G0dmF-R5AZCFMO0ZAeSwH0j_n0wqvWfg/view?usp=sharing",
    "https://drive.google.com/file/d/1H0aeNMwCLhJjg_6rHGyooPiZk-BflFJ1/view?usp=sharing",
    "https://drive.google.com/file/d/1HYju4f-8ZBdwEOd6Wrim_p6Gbw_JAaMT/view?usp=sharing",
    "https://drive.google.com/file/d/1HeYLoKJV7QeeU2mKMWGfmiILI9N_AH6b/view?usp=sharing",
    "https://drive.google.com/file/d/1Ho2ZBv7au6GOXr-6MmU0bfwxm8Yp3G-K/view?usp=sharing",
    "https://drive.google.com/file/d/1HstoSfhckvsOO6_aidfT1bBHOBrOhKqE/view?usp=sharing",
    "https://drive.google.com/file/d/1KDxQE2OMcW77LO6wFqPp-HArzXRRoPR8/view?usp=sharing",
    "https://drive.google.com/file/d/1KIIPDP0th4fxTyFxU_9F7f-fXu3psEu4/view?usp=sharing",
    "https://drive.google.com/file/d/1Kd3bYcNXnGknIwfcJxsZ8sk-GE_gyE0q/view?usp=sharing",
    "https://drive.google.com/file/d/1Ko9fEoQI3xs3kwaEc6yFhF0l2AWtm1JW/view?usp=sharing",
    "https://drive.google.com/file/d/1LJmJmbS2YcKoQEQLppfU6vEO61PCj2dP/view?usp=sharing",
    "https://drive.google.com/file/d/1Lgomj0lv7CuaDxciz48_yULDkPVSzNPE/view?usp=sharing",
    "https://drive.google.com/file/d/1P5RVLlM4b_O7JfXW8ikYGRuw-hWFkZZ8/view?usp=sharing",
    "https://drive.google.com/file/d/1PEJhU_PTOj5fA-69RPCv7-cc9euSS587/view?usp=sharing",
    "https://drive.google.com/file/d/1PFtwIztabc1SqH8QgGPS7tqvJN2VKDTk/view?usp=sharing",
    "https://drive.google.com/file/d/1PuWfOdlg4wlJgfk-iLpJ4rvWs-Wv4ney/view?usp=sharing",
    "https://drive.google.com/file/d/1Q5VmaMDRqlECVGOQpXSSv2WlZt8rZH6P/view?usp=sharing",
    "https://drive.google.com/file/d/1Sio5inFWOyaSlhcM-sq1_lK7tJINERzD/view?usp=sharing",
    "https://drive.google.com/file/d/1SiqiQcVQovnAVxlWVkOSn07n2ZKyTazM/view?usp=sharing",
    "https://drive.google.com/file/d/1StpifccCvsK5GDdUeGFClbTVvyXu_Ni-/view?usp=sharing",
    "https://drive.google.com/file/d/1V0JTji0RoBPs8aFtLppu6DJecObVIIb_/view?usp=sharing",
    "https://drive.google.com/file/d/1V8TGbqTHXWRMv88AROnHLdJPlPX5EOBW/view?usp=sharing",
    "https://drive.google.com/file/d/1Va3EftdPvra16nxljqF9AJGatKcmbIzH/view?usp=sharing",
    "https://drive.google.com/file/d/1Vi6oU5I_evEU5bTBBpKpBYeiyYprYP6N/view?usp=sharing",
    "https://drive.google.com/file/d/1WgPyuEnrmXjSvwhdOAVN1zl_U2HR15yG/view?usp=sharing",
    "https://drive.google.com/file/d/1XmNJeCENmfKiIlAqeRlaZS7Elo3f2HuV/view?usp=sharing",
    "https://drive.google.com/file/d/1YtVQaC7XuePtK-VYQUnAbRDqzQKbRwyd/view?usp=sharing",
    "https://drive.google.com/file/d/1Z0F1u-nTvbEy4q8TVMS2rELe0kuMoNtE/view?usp=sharing",
    "https://drive.google.com/file/d/1ZJ6E2M48Y-mj4GkGL-xdcjfHGCiYso0I/view?usp=sharing",
    "https://drive.google.com/file/d/1ZeUhN2iYIf5Qx-5AidLGfRNzEg4iWp6x/view?usp=sharing",
    "https://drive.google.com/file/d/1Zr158pxcZCJH7M1PD7JsscMgzfMhTwHJ/view?usp=sharing",
    "https://drive.google.com/file/d/1_Vz8_jU0SgckNLGQIJi7eC8yyxBlvGJo/view?usp=sharing",
    "https://drive.google.com/file/d/1_eU4dhnAaT8CMeKXGLweWvToiZLGT8o3/view?usp=sharing",
    "https://drive.google.com/file/d/1ad64sUF24acWjdzamotge-zTsGGQ_E8R/view?usp=sharing",
    "https://drive.google.com/file/d/1cNWOwLa-_K4DHVbRfQxI0lRRX4dBjOLQ/view?usp=sharing",
    "https://drive.google.com/file/d/1cgI8KCXQOIMn7PhFcp-FNbljiQjXRk83/view?usp=sharing",
    "https://drive.google.com/file/d/1clNKGjfJZ_CYftMSi4s61-_MF6Yh9HHG/view?usp=sharing",
    "https://drive.google.com/file/d/1d3z70UTE6nMJzoNE3uy4qJxbB4dfONxl/view?usp=sharing",
    "https://drive.google.com/file/d/1e7pe4wmwbW7eAj03lnh4oT7B5uq_W0W_/view?usp=sharing",
    "https://drive.google.com/file/d/1eC9jJkh24fbp3yPFhkJFCXtMsEctM91h/view?usp=sharing",
    "https://drive.google.com/file/d/1eedO8IwoX9TdVJuWUK24DTaCASAroFN0/view?usp=sharing",
    "https://drive.google.com/file/d/1eyKeDX2ZgZRQrCPwWPKPnbeKl0pHw2R-/view?usp=sharing",
    "https://drive.google.com/file/d/1f2Llv6lx868hu-W25jbo3PSkz_jCjBAH/view?usp=sharing",
    "https://drive.google.com/file/d/1fL9CQM8Opf_jHvr5J_oOXy63yqIwF4Nq/view?usp=sharing",
    "https://drive.google.com/file/d/1gzBXs737Ot0kS8v9-Ajn5BG3Su2i3CbN/view?usp=sharing",
    "https://drive.google.com/file/d/1hjFaezuClZ-G4UtkAY8imuYyEbrnoVfb/view?usp=sharing",
    "https://drive.google.com/file/d/1hyC37Swp986ppG60K7PU1S8ncAypuMQE/view?usp=sharing",
    "https://drive.google.com/file/d/1iKLa4JLdhBlqrROJQMvx2B3NSPXnFvoS/view?usp=sharing",
    "https://drive.google.com/file/d/1idUojsowgcO2qQMRQvVsovxBA6Aad9dj/view?usp=sharing",
    "https://drive.google.com/file/d/1ikI0HNMQCN3ng-EE6eBlOcpc539CdZmj/view?usp=sharing",
    "https://drive.google.com/file/d/1jLIQ565Lm2gCpIBYUowsgnRHP4l91bAz/view?usp=sharing",
    "https://drive.google.com/file/d/1k8bx7UmpHXWgzGXYUTSt1pfLcNn2iycX/view?usp=sharing",
    "https://drive.google.com/file/d/1kVQLmzBadGWljq9Op837-wIOZB3O8TR-/view?usp=sharing",
    "https://drive.google.com/file/d/1lRyftt6wcJK02cvvOfnnAIKj_MXVJmos/view?usp=sharing",
    "https://drive.google.com/file/d/1m1P88OdYCZtiSagfdpiw6SWEJjKlWSh8/view?usp=sharing",
    "https://drive.google.com/file/d/1nTBVUP0UVKlZHnl2fxI7KsAqRvTeKk_8/view?usp=sharing",
    "https://drive.google.com/file/d/1objmnAgNf5jqs4IXatJFdkVdekgi41zB/view?usp=sharing",
    "https://drive.google.com/file/d/1qjvW1_s_s7QLhAZxLKLlWkBDw0lwefgT/view?usp=sharing",
    "https://drive.google.com/file/d/1qrn_Nqa-r9O2w2uPQXzSW6YAxu7xyCAD/view?usp=sharing",
    "https://drive.google.com/file/d/1qvZCWbebWlDLnXu1WhmG1lty4zY-fnhX/view?usp=sharing",
    "https://drive.google.com/file/d/1t-sjmI2gImUCdMTXQBbP8ToWcZSY_mWa/view?usp=sharing",
    "https://drive.google.com/file/d/1ugi0TlsDbIVQUIrRW1lwiiwquGSJKKU3/view?usp=sharing",
    "https://drive.google.com/file/d/1umLZDA9DjUQD3xiD802UWeBT45wffykH/view?usp=sharing",
    "https://drive.google.com/file/d/1wrKJr7sS0BaZcMAdqGzvrC5uBw2Ba1n9/view?usp=sharing",
    "https://drive.google.com/file/d/1wtxBphD8QjfypQZbrsaAHwxueftJStlH/view?usp=sharing",
    "https://drive.google.com/file/d/1yVHpUp9mLInP0_i2TQAYHUnDvCBdrjj6/view?usp=sharing",
    "https://drive.google.com/file/d/1yaie6FEX0EdVrMd1uPiREMQjyeyaJvOA/view?usp=sharing",
    "https://drive.google.com/file/d/1yzjrn_fY79UvR64tD2WR4IFqwZlrl88r/view?usp=sharing",
    "https://drive.google.com/file/d/1z0zzGW6tuUvPa0ZO-vtUFAaT2_MDarJa/view?usp=sharing",
    "https://drive.google.com/file/d/1z9xLVvDvY2UvEgnPNO2CCNWZqbnJKkdo/view?usp=sharing",
    "https://drive.google.com/file/d/1zIkX7arTsVXtMerLdnYWpMiNedrsug9V/view?usp=sharing",
    "https://drive.google.com/file/d/1zVtR64fW604WSRjv3Pj51nmRakFunHbw/view?usp=sharing",
    "https://drive.google.com/file/d/1zZBqx4FPxFI3dcdZmPiovkJcHM9UTfvv/view?usp=sharing",
    "https://drive.google.com/file/d/1zo3gkBCRyjgOJFUtCYO-ZjcMjENk3Of6/view?usp=sharing"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

download_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\pdf_downloads"
os.makedirs(download_dir, exist_ok=True)

def process_url(idx_url):
    idx, url = idx_url
    file_id = url.split('/d/')[1].split('/')[0]
    dl_url = f"https://drive.google.com/uc?export=download&confirm=t&id={file_id}"
    
    req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
    extracted_text = ""
    file_type = "unknown"
    local_path = ""
    
    try:
        data = urllib.request.urlopen(req, context=ctx, timeout=15).read()
        if data.startswith(b'%PDF'):
            file_type = "pdf"
            local_path = os.path.join(download_dir, f"cert_{idx:02d}.pdf")
            with open(local_path, "wb") as f:
                f.write(data)
            try:
                reader = PdfReader(local_path)
                text_pages = [page.extract_text() for page in reader.pages if page.extract_text()]
                extracted_text = " ".join(text_pages).strip()
            except Exception as e:
                extracted_text = f"PDF Read Error: {e}"
        elif data.startswith(b'\x89PNG') or data.startswith(b'\xff\xd8') or b'JFIF' in data[:20]:
            file_type = "image"
        else:
            file_type = "html/other"
    except Exception as e:
        extracted_text = f"Download Error: {e}"

    return {
        "index": idx,
        "url": url,
        "file_id": file_id,
        "file_type": file_type,
        "extracted_text": extracted_text[:500] if extracted_text else ""
    }

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(process_url, list(enumerate(urls))))

out_path = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\extracted_certs.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Finished processing downloads and pdf text extraction.")
