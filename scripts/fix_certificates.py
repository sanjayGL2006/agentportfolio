import re
import uuid

def fix_certificates():
    with open('js/certificatesData.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will look for objects that just have { driveId: '...', ... } and rewrite them
    # But wait, doing this via regex might be tricky. Let's just do a simple replacement
    # for patterns like:
    # { driveId: '1-9WHvzovaXE7Bm_vSMJaTauO15fiNFn6', title: "IMG_20250618_213916", org: "Verified Credential", category: 'tech', year: 2026, month: 'September', tags: ["Tech", "Certificate"] }
    
    def replacer(match):
        drive_id = match.group(1)
        # Check if verifyLink is already in the match string
        if "verifyLink" in match.group(0):
            return match.group(0)
            
        new_id = f"cert-auto-{uuid.uuid4().hex[:8]}"
        
        # We replace the start of the object to inject id, type, verifyLink, image, emoji
        obj_content = match.group(0)
        obj_content = obj_content.replace("{ driveId:", f"{{\n    id: '{new_id}',\n    type: 'certificate',\n    verifyLink: 'https://drive.google.com/file/d/{drive_id}/view?usp=sharing',\n    image: 'https://drive.google.com/thumbnail?id={drive_id}&sz=w800',\n    emoji: '🏆',\n    driveId:")
        return obj_content

    # Regex to find lines or blocks starting with { driveId: '...'
    # Or just search for driveId: '...' and inject fields before it if they don't exist
    
    # Actually, let's find all driveId: '...'
    # It looks like the generic ones were appended on a single line
    new_content = re.sub(r'\{\s*driveId:\s*[\'"]([a-zA-Z0-9_-]+)[\'"][^\}]+\}', replacer, content)
    
    with open('js/certificatesData.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Fixed malformed certificates in js/certificatesData.js")

if __name__ == "__main__":
    fix_certificates()
