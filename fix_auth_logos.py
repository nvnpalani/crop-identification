import os
import re

new_logo_only = '''<div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
    <div style="width: 48px; height: 48px; background-color: #1e7e34; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
        <i class="fa-solid fa-leaf"></i>
    </div>
</div>'''

def fix_auth_logos(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous full logo block
    old_logo_pattern = r'<div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; gap: 10px; font-weight: 700; font-size: 1.2rem; color: #1f2937; text-decoration: none;">.*?</div>\s*</div>\s*</div>'
    
    # We use regex to find and replace
    new_content = re.sub(old_logo_pattern, new_logo_only, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

fix_auth_logos('d:/plant/templates/login.html')
fix_auth_logos('d:/plant/templates/signup.html')

print("Fixed auth logos")
