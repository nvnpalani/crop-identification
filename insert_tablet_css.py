import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

tablet_css = '''
            /* Tablet Navbar Settings */
            .nav-links { gap: 15px; }
            .nav-links li a { font-size: 0.85rem; }
            .nav-actions { gap: 10px; display: flex; align-items: center; }
            .nav-actions .btn { padding: 0; font-size: 0.85rem; width: 85px; height: 34px; display: inline-flex; align-items: center; justify-content: center; }
            .logo { font-size: 1rem; }
            .logo-icon { width: 28px; height: 28px; font-size: 14px; }
'''

if '/* Tablet Navbar Settings */' not in content:
    content = content.replace('        @media (max-width: 992px) {', '        @media (max-width: 992px) {' + tablet_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
