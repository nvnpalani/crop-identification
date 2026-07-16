import os
import re

css_to_replace = r'''        \.back-btn \{.*?\}
        @media \(max-width: 480px\) \{.*?\}
'''
# We can just match the block using re.DOTALL

new_css = '''        .back-btn {
            position: absolute;
            top: 1.5rem;
            left: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #334155;
            text-decoration: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(16, 185, 129, 0.2);
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s;
            z-index: 100;
        }
        .back-btn:hover {
            transform: translateX(-5px);
            color: #10b981;
            border-color: rgba(16, 185, 129, 0.4);
            box-shadow: 0 6px 12px rgba(16, 185, 129, 0.1);
        }'''

html_to_remove = '''    <a href="{{ url_for('index') }}" class="back-btn" title="Back to Home">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
        </svg>
        Back
    </a>'''

html_to_add = '''    <div class="login-container">
        <a href="{{ url_for('index') }}" class="back-btn" title="Back to Home">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="19" y1="12" x2="5" y2="12"></line>
                <polyline points="12 19 5 12 12 5"></polyline>
            </svg>
        </a>'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .login-container
    if 'position: relative;' not in content.split('.login-container {')[1].split('}')[0]:
        content = content.replace('.login-container {', '.login-container {\n            position: relative;')

    # 2. Replace CSS using regex
    content = re.sub(r'\s*\.back-btn \{.*?\s*@media \(max-width: 480px\) \{.*?\}\s*\}', '\n' + new_css, content, flags=re.DOTALL)
    
    # Also just in case the above regex missed the hover:
    # Actually the easiest way is to remove old CSS block and insert new one
    # I'll just use string replacements to be safe.
    
    # 3. Move HTML
    if html_to_remove in content:
        content = content.replace(html_to_remove, '')
        content = content.replace('<div class="login-container">', html_to_add)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_file('d:/plant/templates/login.html')
update_file('d:/plant/templates/signup.html')
