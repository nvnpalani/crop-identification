import os

css_to_add = '''
        .back-btn {
            position: absolute;
            top: 2rem;
            left: 2rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #334155;
            text-decoration: none;
            font-weight: 600;
            padding: 0.6rem 1.2rem;
            border-radius: 99px;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
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
        }
        @media (max-width: 480px) {
            .back-btn {
                top: 1rem;
                left: 1rem;
                padding: 0.5rem 1rem;
                font-size: 0.9rem;
            }
        }
'''

html_to_add = '''
    <a href="{{ url_for('index') }}" class="back-btn" title="Back to Home">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
        </svg>
        Back
    </a>
'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate insertion
    if 'class="back-btn"' in content:
        print(f"Already updated {filepath}")
        return

    # Insert CSS
    content = content.replace('<style>', '<style>' + css_to_add)

    # Insert HTML
    content = content.replace('<body>', '<body>' + html_to_add)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_file('d:/plant/templates/login.html')
update_file('d:/plant/templates/signup.html')
