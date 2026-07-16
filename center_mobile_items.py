import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .dashboard-stats-bar > div in media query
# Currently it is: .dashboard-stats-bar > div { width: 100%; justify-content: flex-start; }
# We want it to be center aligned on mobile
old_stats_css = '.dashboard-stats-bar > div { width: 100%; justify-content: flex-start; }'
new_stats_css = '.dashboard-stats-bar > div { width: 100%; justify-content: center; }'
if old_stats_css in content:
    content = content.replace(old_stats_css, new_stats_css)
elif '.dashboard-stats-bar > div { width: 100%; justify-content: center; }' not in content:
    # Add it to the mobile media query
    content = content.replace('.dashboard-stats-bar { flex-direction: column !important; gap: 30px; }',
                              '.dashboard-stats-bar { flex-direction: column !important; gap: 30px; }\n            .dashboard-stats-bar > div { width: 100%; justify-content: center !important; }')

# 2. Update .contact-info li in media query
# Add justify-content: center; to the .contact-info li items on mobile.
contact_css_mobile = '''            .contact-info li { justify-content: center !important; }'''
if '.contact-info li { justify-content: center !important; }' not in content:
    content = content.replace('.social-icons { justify-content: center; }', 
                              '.social-icons { justify-content: center; }\n' + contact_css_mobile)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
