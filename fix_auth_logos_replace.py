import os

new_logo_only = '''<div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
    <div style="width: 48px; height: 48px; background-color: #1e7e34; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
        <i class="fa-solid fa-leaf"></i>
    </div>
</div>'''

old_logo_block = '''<div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; gap: 10px; font-weight: 700; font-size: 1.2rem; color: #1f2937; text-decoration: none;">
    <div style="width: 32px; height: 32px; background-color: #1e7e34; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 16px;">
        <i class="fa-solid fa-leaf"></i>
    </div>
    <div style="display: flex; flex-direction: column; line-height: 1.1;">
        <span style="font-size: 1.2rem; margin: 0; padding: 0;">CropID</span>
        <span style="font-size: 0.7rem; font-weight: 400; color: #4b5563;">Crop Identification</span>
    </div>
</div>'''

def fix_auth_logos(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_logo_block in content:
        new_content = content.replace(old_logo_block, new_logo_only)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")
    else:
        print(f"Old block not found in {filepath}")

fix_auth_logos('d:/plant/templates/login.html')
fix_auth_logos('d:/plant/templates/signup.html')
