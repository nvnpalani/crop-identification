import os
import glob
import re

def process_admin_file(filepath, active_page_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the sidebar overlay
    start_idx = content.find('<div class="sidebar-overlay"')
    if start_idx == -1:
        # try finding aside
        start_idx = content.find('<aside class="admin-sidebar">')
        if start_idx == -1:
            start_idx = content.find('<div class="admin-sidebar">')
            
    # Find the start of the main content
    end_idx = content.find('<div class="admin-main">')
    
    if start_idx != -1 and end_idx != -1:
        before = content[:start_idx]
        after = content[end_idx:]
        
        replacement = f"{{% set active_page = '{active_page_name}' %}}\n    {{% include 'components/admin_sidebar.html' %}}\n    "
        new_content = before + replacement + after
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Refactored {filepath}")
    else:
        print(f"Could not find markers in {filepath}")

admin_pages = {
    'templates/admin/admin_dashboard.html': 'admin_dashboard',
    'templates/admin/admin_users.html': 'admin_users',
    'templates/admin/admin_detect.html': 'admin_detect',
    'templates/admin/auto_training.html': 'auto_training',
    'templates/admin/suggestions.html': 'suggestions',
    'templates/admin/training_history.html': 'training_history'
}

for path, active_page in admin_pages.items():
    filepath = os.path.join(os.getcwd(), path.replace('/', os.sep))
    if os.path.exists(filepath):
        process_admin_file(filepath, active_page)
    else:
        print(f"File not found: {filepath}")

# Process user index.html
def process_user_file(filepath, active_page_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('<div class="sidebar-overlay"')
    if start_idx == -1:
        start_idx = content.find('<aside class="admin-sidebar">')
        if start_idx == -1:
            start_idx = content.find('<div class="admin-sidebar">')
            
    end_idx = content.find('<div class="admin-main">')
    
    if start_idx != -1 and end_idx != -1:
        before = content[:start_idx]
        after = content[end_idx:]
        
        replacement = f"{{% set active_page = '{active_page_name}' %}}\n    {{% include 'components/user_sidebar.html' %}}\n    "
        new_content = before + replacement + after
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Refactored {filepath}")
    else:
        print(f"Could not find markers in {filepath}")

user_filepath = os.path.join(os.getcwd(), 'templates', 'user', 'index.html')
if os.path.exists(user_filepath):
    process_user_file(user_filepath, 'detect')
