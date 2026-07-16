import os

filepath = 'd:/plant/templates/website.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the incorrect justify-content: center with the inline-block logic
old_css = '.contact-info li { justify-content: center !important; }'
new_css = '.contact-info { display: inline-block; text-align: left; }\n            .contact-info li { justify-content: flex-start !important; }'

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    # Fallback if old_css doesn't match perfectly
    content = content.replace('.social-icons { justify-content: center; }', 
                              '.social-icons { justify-content: center; }\n            ' + new_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {filepath}")
