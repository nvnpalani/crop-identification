import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for <div class="admin-topbar"> followed by whitespace and <div></div> (with or without comments)
    pattern = r'<div class="admin-topbar">\s*<div></div>(?: <!--.*?-->)?'
    replacement = '''<div class="admin-topbar">
            <div style="display: flex; align-items: center; gap: 10px;">
                <button class="mobile-menu-btn" onclick="document.querySelector('.admin-sidebar').classList.add('show'); document.querySelector('.sidebar-overlay').classList.add('show');">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </button>
            </div>'''
            
    # Check if we already inserted the button
    if 'class="mobile-menu-btn"' not in content[content.find('<div class="admin-topbar">'):content.find('<div class="admin-topbar">')+500]:
        content = re.sub(pattern, replacement, content, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"Already fixed {filepath}")

for file in glob.glob('templates/admin/*.html'):
    process_file(file)
