import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline style for dashboard-stats-bar
old_stats_bar = 'style="background: white; border-radius: 20px; padding: 30px 40px; display: flex; justify-content: space-around; align-items: center; box-shadow: 0 10px 40px rgba(0,0,0,0.06); border: 1px solid var(--border-color); margin-top: 10px;"'
new_stats_bar = 'style="background: white; border-radius: 20px; padding: 30px 40px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); border: 1px solid var(--border-color); margin-top: 10px;"'

if old_stats_bar in content:
    content = content.replace(old_stats_bar, new_stats_bar)

# Replace inline dividers
old_divider = '<div style="width: 1px; height: 50px; background: var(--border-color);"></div>'
new_divider = '<div class="stat-divider"></div>'
if old_divider in content:
    content = content.replace(old_divider, new_divider)

# Add CSS for .dashboard-stats-bar and .stat-divider
css_to_add = '''        .dashboard-stats-bar {
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
        .stat-divider {
            width: 1px;
            height: 50px;
            background: var(--border-color);
        }'''

if '.dashboard-stats-bar {' not in content:
    content = content.replace('/* Hamburger Menu */', css_to_add + '\n        /* Hamburger Menu */')

# Add to mobile media query (max-width: 992px)
mobile_css = '''            .dashboard-stats-bar { flex-direction: column !important; gap: 30px; }
            .stat-divider { width: 100% !important; height: 1px !important; }'''

if '.stat-divider { width: 100%' not in content:
    content = content.replace('.features-grid { grid-template-columns: repeat(2, 1fr); }', 
                              '.features-grid { grid-template-columns: repeat(2, 1fr); }\n' + mobile_css)

# Also make the individual stats items flex correctly (they are already flex-row, which is fine, but maybe text left aligned)
# They are already <div style="display: flex; align-items: center; gap: 15px;">, which will stay row, but they might need to be width 100% or justified to center.
# Actually, if we just stack them, they will be left aligned or centered depending on flex.
# Adding width: 100%; justify-content: center; to the stat items on mobile might be better.
mobile_css_extra = '''            .dashboard-stats-bar > div { width: 100%; justify-content: flex-start; }'''
if 'dashboard-stats-bar > div' not in content:
    content = content.replace('.stat-divider { width: 100%', mobile_css_extra + '\n            .stat-divider { width: 100%')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
