import os

files_to_update = [
    'd:/plant/templates/admin/admin_dashboard.html',
    'd:/plant/templates/admin/admin_detect.html',
    'd:/plant/templates/admin/admin_users.html',
    'd:/plant/templates/admin/auto_training.html',
    'd:/plant/templates/admin/suggestions.html',
    'd:/plant/templates/admin/training_history.html',
    'd:/plant/templates/user/index.html'
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the background color of the overlay
    new_content = content.replace('background: rgba(0,0,0,0.5);', 'background: transparent;')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
