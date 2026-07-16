import os
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update admin-styles
    old_style = '''    <style id="admin-styles">
        body { margin: 0; padding: 0; display: flex; background: #f8fafc; }
        .admin-sidebar { width: 260px; height: 100vh; background: white; border-right: 1px solid var(--glass-border); display: flex; flex-direction: column; position: fixed; top: 0; left: 0; z-index: 100; }
        .admin-main { margin-left: 260px; width: calc(100% - 260px); min-height: 100vh; display: flex; flex-direction: column; }
        .admin-topbar { height: 70px; background: white; border-bottom: 1px solid var(--glass-border); display: flex; justify-content: space-between; align-items: center; padding: 0 2rem; position: fixed; top: 0; left: 260px; right: 0; z-index: 500; box-sizing: border-box; }'''
    
    new_style = '''    <style id="admin-styles">
        body { margin: 0; padding: 0; display: flex; background: #f8fafc; overflow-x: hidden; }
        .admin-sidebar { width: 260px; height: 100vh; background: white; border-right: 1px solid var(--glass-border); display: flex; flex-direction: column; position: fixed; top: 0; left: 0; z-index: 1000; transition: transform 0.3s ease; }
        .admin-main { margin-left: 260px; width: calc(100% - 260px); min-height: 100vh; display: flex; flex-direction: column; transition: margin-left 0.3s ease, width 0.3s ease; }
        .admin-topbar { height: 70px; background: white; border-bottom: 1px solid var(--glass-border); display: flex; justify-content: space-between; align-items: center; padding: 0 2rem; position: fixed; top: 0; left: 260px; right: 0; z-index: 500; box-sizing: border-box; transition: left 0.3s ease; }
        
        @media (max-width: 768px) {
            .admin-sidebar { transform: translateX(-100%); }
            .admin-sidebar.show { transform: translateX(0); }
            .admin-main { margin-left: 0; width: 100%; }
            .admin-topbar { left: 0; padding: 0 1rem; }
            .admin-content { padding: 1rem; margin-top: 60px; overflow-x: hidden; }
            .mobile-menu-btn { display: block !important; }
            .sidebar-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 999; }
            .sidebar-overlay.show { display: block; }
        }
        .mobile-menu-btn { display: none; background: none; border: none; font-size: 1.5rem; color: var(--text-main); cursor: pointer; padding: 0.5rem; }'''

    content = content.replace(old_style, new_style)

    # Remove the extra media query block from auto_training.html and others just in case
    old_auto_training_media = '''        @media (max-width: 768px) {
            .admin-sidebar { display: none; }
            .admin-main { margin-left: 0; width: 100%; }
            .admin-topbar { padding: 0 1rem; }
            .admin-content { padding: 1rem; }
        }'''
    content = content.replace(old_auto_training_media, "")

    # 2. Add overlay before .admin-sidebar
    if '<div class="sidebar-overlay"' not in content:
        content = content.replace('<div class="admin-sidebar">', '<div class="sidebar-overlay" onclick="document.querySelector(\'.admin-sidebar\').classList.remove(\'show\'); this.classList.remove(\'show\');"></div>\n    <div class="admin-sidebar">')

    # 3. Update admin-topbar to include hamburger button
    old_topbar = '''        <div class="admin-topbar">
            <div></div> <!-- Left empty spacer -->'''
    
    new_topbar = '''        <div class="admin-topbar">
            <div style="display: flex; align-items: center; gap: 10px;">
                <button class="mobile-menu-btn" onclick="document.querySelector('.admin-sidebar').classList.add('show'); document.querySelector('.sidebar-overlay').classList.add('show');">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </button>
            </div>'''
            
    content = content.replace(old_topbar, new_topbar)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Processed {filepath}")

for file in glob.glob('templates/admin/*.html'):
    process_file(file)
