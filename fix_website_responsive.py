import os
import re

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_to_add = '''
        /* Hamburger Menu */
        .hamburger {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--text-dark);
            background: none;
            border: none;
        }

        .nav-menu-wrapper {
            display: flex;
            align-items: center;
            gap: 30px;
        }

        @media (max-width: 992px) {
            .nav-menu-wrapper {
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
            }

            /* Fix Spacing */
            .hero .container { flex-direction: column; text-align: center; gap: 40px; }
            .hero-content { max-width: 100% !important; margin: 0 auto; padding: 20px !important; }
            .hero-image { justify-content: center; width: 100%; }
            .hero-image-placeholder { width: 100%; height: auto; min-height: 300px; }
            .hero-card { position: relative; bottom: 0; left: 0; width: 100%; flex-direction: column; gap: 15px; margin-top: 20px; text-align: center; }
            .hero-buttons { justify-content: center; }
            
            .features-grid { grid-template-columns: repeat(2, 1fr); }
            
            .how-it-works-content { flex-direction: column; gap: 40px; }
            .steps-container { width: 100%; padding-left: 20px; }
            
            .about .container { flex-direction: column; text-align: center; gap: 40px; }
            
            .cta-banner .container { flex-direction: column; text-align: center; gap: 30px; }
            .cta-left { flex-direction: column; }
            
            .footer-grid { grid-template-columns: repeat(2, 1fr); gap: 30px; }
        }

        @media (max-width: 768px) {
            .hero-content h1 { font-size: 2.2rem !important; }
            .hero-content p { font-size: 1rem; }
            .hero-buttons { flex-direction: column; }
            .features-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr; text-align: center; }
            .footer-logo { justify-content: center; }
            .social-icons { justify-content: center; }
            .steps-container::before { left: 45px; }
        }
'''
if '/* Hamburger Menu */' not in content:
    content = content.replace('</style>', css_to_add + '\n    </style>')

# 2. Update Navbar HTML
navbar_old = '''            <ul class="nav-links">
                <li><a href="#hero" class="active">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#how-it-works">How It Works</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <a href="{{ url_for('login') }}" class="btn btn-outline">Login</a>
                <a href="{{ url_for('signup') }}" class="btn btn-primary">Sign Up</a>
            </div>'''

navbar_new = '''            <button class="hamburger" id="hamburger-btn">
                <i class="fa-solid fa-bars"></i>
            </button>
            <div class="nav-menu-wrapper" id="nav-menu">
                <ul class="nav-links">
                    <li><a href="#hero" class="active">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#how-it-works">How It Works</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <div class="nav-actions">
                    <a href="{{ url_for('login') }}" class="btn btn-outline">Login</a>
                    <a href="{{ url_for('signup') }}" class="btn btn-primary">Sign Up</a>
                </div>
            </div>'''

if 'id="hamburger-btn"' not in content:
    content = content.replace(navbar_old, navbar_new)

# 3. Add JS for hamburger
js_to_add = '''
    <script>
        const hamburgerBtn = document.getElementById('hamburger-btn');
        const navMenu = document.getElementById('nav-menu');
        
        hamburgerBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const icon = hamburgerBtn.querySelector('i');
            if(navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                hamburgerBtn.querySelector('i').classList.remove('fa-times');
                hamburgerBtn.querySelector('i').classList.add('fa-bars');
            });
        });
    </script>
</body>'''

if 'id="hamburger-btn"' in content and 'hamburgerBtn.addEventListener' not in content:
    content = content.replace('</body>', js_to_add)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {filepath}")
