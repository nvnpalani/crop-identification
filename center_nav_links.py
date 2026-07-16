import os
import re

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .nav-menu-wrapper
old_wrapper = '''        .nav-menu-wrapper {
            display: flex;
            align-items: center;
            gap: 30px;
        }'''
new_wrapper = '''        .nav-menu-wrapper {
            display: flex;
            align-items: center;
            flex: 1;
        }'''
if old_wrapper in content:
    content = content.replace(old_wrapper, new_wrapper)

# 2. Update .nav-links
old_links = '''        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
        }'''
new_links = '''        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
            margin: 0 auto;
        }'''
if old_links in content:
    content = content.replace(old_links, new_links)

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
