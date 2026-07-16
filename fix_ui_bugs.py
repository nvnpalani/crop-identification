import os
import re

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up duplicate CSS
# We know the duplicate CSS starts with '/* Hamburger Menu */' and ends with '        @media (max-width: 768px) {' ... '        }'
# Let's find the second occurrence and remove it up to the next '</style>'
first_idx = content.find('/* Hamburger Menu */')
if first_idx != -1:
    second_idx = content.find('/* Hamburger Menu */', first_idx + 1)
    if second_idx != -1:
        end_idx = content.find('</style>', second_idx)
        if end_idx != -1:
            # Remove the second block completely
            content = content[:second_idx] + content[end_idx:]

# 2. Fix hero-top-row inline style
bad_div = '<div style="display: flex; align-items: center; justify-content: space-between; gap: 30px;">'
good_div = '<div class="hero-top-row">'
if bad_div in content:
    content = content.replace(bad_div, good_div)
    # Add .hero-top-row to normal CSS
    normal_css = '.hero-top-row { display: flex; align-items: center; justify-content: space-between; gap: 30px; }'
    content = content.replace('/* Hamburger Menu */', normal_css + '\n        /* Hamburger Menu */')
    # Add to media query
    mobile_css = '.hero-top-row { flex-direction: column !important; text-align: center; }'
    content = content.replace('.hero .container { flex-direction: column; text-align: center; gap: 40px; }', 
                              '.hero .container { flex-direction: column; text-align: center; gap: 40px; }\n            ' + mobile_css)

# 3. Fix Contact Us alignment
# We'll replace the existing contact list items
old_li1 = '<li style="margin-bottom: 10px;"><i class="fa-solid fa-envelope"\n                                    style="margin-right: 10px;"></i> support@cropid.com</li>'
new_li1 = '<li style="margin-bottom: 10px; display: flex; align-items: center; gap: 10px;"><i class="fa-solid fa-envelope" style="width: 20px; text-align: center;"></i> support@cropid.com</li>'

old_li2 = '<li style="margin-bottom: 10px;"><i class="fa-solid fa-phone"\n                                    style="margin-right: 10px;"></i> +91 1234567890</li>'
new_li2 = '<li style="margin-bottom: 10px; display: flex; align-items: center; gap: 10px;"><i class="fa-solid fa-phone" style="width: 20px; text-align: center;"></i> +91 1234567890</li>'

old_li3 = '<li style="margin-bottom: 10px;"><i class="fa-solid fa-location-dot"\n                                    style="margin-right: 10px;"></i> Tamil Nadu, India</li>'
new_li3 = '<li style="margin-bottom: 10px; display: flex; align-items: center; gap: 10px;"><i class="fa-solid fa-location-dot" style="width: 20px; text-align: center;"></i> Tamil Nadu, India</li>'

# If the multi-line replace doesn't match perfectly, we can use regex
content = re.sub(r'<li style="margin-bottom: 10px;">\s*<i class="fa-solid fa-envelope"\s*style="margin-right: 10px;"></i>\s*support@cropid\.com</li>', new_li1, content)
content = re.sub(r'<li style="margin-bottom: 10px;">\s*<i class="fa-solid fa-phone"\s*style="margin-right: 10px;"></i>\s*\+91 1234567890</li>', new_li2, content)
content = re.sub(r'<li style="margin-bottom: 10px;">\s*<i class="fa-solid fa-location-dot"\s*style="margin-right: 10px;"></i>\s*Tamil Nadu, India</li>', new_li3, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
