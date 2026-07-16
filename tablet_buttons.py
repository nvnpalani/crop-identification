import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous tablet button CSS with a fixed width/height one
old_css = '.nav-actions .btn { padding: 6px 15px; font-size: 0.85rem; }'
new_css = '.nav-actions .btn { padding: 0; font-size: 0.85rem; width: 85px; height: 34px; display: inline-flex; align-items: center; justify-content: center; }'

if old_css in content:
    content = content.replace(old_css, new_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
