import os
import glob
import re

# 1. Inject FontAwesome to all html files
html_files = glob.glob('d:/plant/templates/**/*.html', recursive=True)
fa_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if fa_link not in content and '<head>' in content:
        content = content.replace('<head>', '<head>\n    ' + fa_link)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. Update the logos
new_logo_html = '''<div style="display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 1.2rem; color: #1f2937; text-decoration: none;">
    <div style="width: 32px; height: 32px; background-color: #1e7e34; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 16px;">
        <i class="fa-solid fa-leaf"></i>
    </div>
    <div style="display: flex; flex-direction: column; line-height: 1.1;">
        <span style="font-size: 1.2rem; margin: 0; padding: 0;">CropID</span>
        <span style="font-size: 0.7rem; font-weight: 400; color: #4b5563;">Crop Identification</span>
    </div>
</div>'''

def replace_svg_logo(filepath, is_sidebar=False):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # For login and signup, it's just <svg class="brand-icon" ...> ... </svg>
    # Wait, in login and signup, there's a title below it? Let's check what's there
    # The regex will find <svg class="brand-icon" ... </svg> and replace it.
    if is_sidebar:
        # Sidebars have <div class="sidebar-logo"> ... </div>
        # We replace the inner content or the whole div
        old_div_pattern = r'<svg class="brand-icon".*?</svg>\s*CropID'
        content = re.sub(r'<svg class="brand-icon".*?</svg>\s*(?:CropID|image detection)', new_logo_html, content, flags=re.DOTALL | re.IGNORECASE)
    else:
        # login / signup have brand-icon
        content = re.sub(r'<svg class="brand-icon".*?</svg>', new_logo_html, content, flags=re.DOTALL)
        # We might also need to center it in login/signup
        # new_logo_html is a div. If it's flex, let's make sure it's centered
        content = content.replace('style="display: flex; align-items: center; gap: 10px;', 'style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; gap: 10px;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_svg_logo('d:/plant/templates/login.html')
replace_svg_logo('d:/plant/templates/signup.html')
replace_svg_logo('d:/plant/templates/components/admin_sidebar.html', is_sidebar=True)
replace_svg_logo('d:/plant/templates/components/user_sidebar.html', is_sidebar=True)

print("Updated logos")
