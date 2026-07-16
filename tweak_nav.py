import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will just add the transform to the existing classes
css_addon = '''
        /* Tiny alignment tweaks requested by user */
        .logo { transform: translateX(-2px); }
        .nav-actions { transform: translateX(2px); }
'''

if '/* Tiny alignment tweaks requested by user */' not in content:
    content = content.replace('        .nav-actions {', css_addon + '\n        .nav-actions {')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
