import glob
import time
import re

html_files = glob.glob('*.html')
js_files = glob.glob('js/*.js')
ts = str(int(time.time()))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the script tags with versioned ones
    content = re.sub(r'src="js/projectsData\.js(\?v=\d+)?"', f'src="js/projectsData.js?v={ts}"', content)
    content = re.sub(r'src="js/certificatesData\.js(\?v=\d+)?"', f'src="js/certificatesData.js?v={ts}"', content)
    
    # Also update the hardcoded counts in HTML UI
    content = content.replace('All Certificates (102+)', 'All Certificates (224+)')
    content = content.replace('29+', '69+')
    content = content.replace('222+', '224+')
    content = content.replace('30+', '69+')
    content = content.replace('All Certificates (70+)', 'All Certificates (224+)')
    content = content.replace('70+', '224+')
    content = content.replace('123+', '224+')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

for file in js_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('All Certificates (102+)', 'All Certificates (224+)')
    content = content.replace('All Certificates (70+)', 'All Certificates (224+)')
    content = content.replace('29+', '69+')
    content = content.replace('30+', '69+')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Cache busted and counts updated!')
