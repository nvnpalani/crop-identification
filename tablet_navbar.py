import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to extract the hamburger logic from @media (max-width: 992px)
# and put it into @media (max-width: 768px), and then add tablet specific navbar CSS in 992px.

# Here is the hamburger logic inside 992px:
hamburger_logic = '''            .nav-menu-wrapper {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background: white;
                flex-direction: column;
                justify-content: flex-start;
                padding: 40px 20px;
                gap: 30px;
                transition: left 0.3s ease;
                box-shadow: 0 10px 15px rgba(0,0,0,0.1);
                overflow-y: auto;
            }
            .nav-menu-wrapper.active {
                left: 0;
            }
            .nav-links {
                flex-direction: column;
                text-align: center;
                gap: 20px;
            }
            .nav-actions {
                flex-direction: column;
                width: 100%;
                gap: 15px;
            }
            .nav-actions .btn {
                width: 100%;
            }
            .hamburger {
                display: block;
            }'''

# Remove hamburger logic from 992px
if hamburger_logic in content:
    content = content.replace(hamburger_logic, '')

    # Tablet Navbar tweaks (to go into 992px where hamburger was)
    tablet_navbar_css = '''            /* Tablet Navbar Settings (No Hamburger) */
            .nav-links { gap: 15px; }
            .nav-links li a { font-size: 0.85rem; }
            .nav-actions { gap: 10px; }
            .nav-actions .btn { padding: 6px 15px; font-size: 0.85rem; }
            .logo { font-size: 1rem; }
            .logo-icon { width: 28px; height: 28px; font-size: 14px; }'''
    
    # Insert tablet CSS right after "@media (max-width: 992px) {"
    # We replaced hamburger logic, so now it's just "@media (max-width: 992px) {\n\n            /* Fix Spacing */"
    content = content.replace('@media (max-width: 992px) {\n\n            /* Fix Spacing */', 
                              '@media (max-width: 992px) {\n' + tablet_navbar_css + '\n            /* Fix Spacing */')

    # Add hamburger logic to 768px
    if '@media (max-width: 768px) {' in content:
        content = content.replace('@media (max-width: 768px) {', '@media (max-width: 768px) {\n' + hamburger_logic)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
