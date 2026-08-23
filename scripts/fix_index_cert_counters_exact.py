import re

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if "Certificates</div>" in lines[i] and i > 0:
        lines[i-1] = re.sub(r'>\d+\+?<', '>145+<', lines[i-1])
        lines[i-1] = re.sub(r'data-count="\d+"', 'data-count="145"', lines[i-1])
    if "Certificates (171 Total)" in lines[i]:
        lines[i] = lines[i].replace("Certificates (171 Total)", "Certificates (145 Total)")

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Updated index.html stat counters to 145+")
