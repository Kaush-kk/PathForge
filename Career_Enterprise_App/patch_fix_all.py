import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Height 92vh -> 100% inside HERO_SHADER_HTML
content = content.replace(
    '<div style="position:relative; width:100%; height:92vh; overflow:hidden; background:#03040a;">',
    '<div style="position:relative; width:100%; height:100%; overflow:hidden; background:#03040a;">'
)

# 2. Iframe negative margin
content = content.replace(
    'margin-bottom: -64px !important;',
    'margin-bottom: -48px !important;'
)

# 3. hr margin in render_nav_bar
content = content.replace(
    "margin:0.5rem 0 1.5rem 0;",
    "margin:0.25rem 0 0.5rem 0;"
)

# 4. .hero CSS padding
content = re.sub(
    r'\.hero\s*\{\s*text-align:\s*center;\s*padding:\s*4\.5rem\s+2rem\s+3\.5rem;\s*\}',
    '.hero {\n    text-align: center;\n    padding: 0.5rem 2rem 1.5rem;\n}',
    content
)

# 5. .cg-hero CSS padding
content = re.sub(
    r'\.cg-hero\s*\{\s*text-align:\s*center;\s*padding:\s*3rem\s+1rem\s+1\.5rem;\s*\}',
    '.cg-hero {\n        text-align: center;\n        padding: 0.5rem 1rem 1.5rem;\n    }',
    content
)

# 6. .page-wrapper CSS min-height removal
content = re.sub(
    r'\.page-wrapper\s*\{[^}]*min-height:\s*75vh;[^}]*\}',
    '''.page-wrapper {
    position: relative;
    z-index: 1;
    padding: 0 2rem 2rem;
    max-width: 1320px;
    margin: 0 auto;
}''',
    content
)

# 7. Inline hero style in Career Engine
content = content.replace(
    '<div class="hero" style="text-align: left; padding: 3rem 0 2.5rem;">',
    '<div class="hero" style="text-align: left; padding: 0.5rem 0 1.5rem;">'
)

# 8. Inline hero style in Exam Directory
content = content.replace(
    '<div class="hero" style="padding-bottom:2rem;">',
    '<div class="hero" style="padding: 0.5rem 0 1.5rem;">'
)

# 9. Remove block-container min-height 100vh and flex margin-top: auto for footer
content = content.replace(
    'min-height: 100vh !important;\n}',
    '}'
)
content = re.sub(
    r'div\[data-testid="stElementContainer"\]:has\(\.site-footer\)\s*\{[^}]*\}',
    '',
    content
)

# 10. Completely remove the SITE FOOTER block at the end of app.py
footer_block_pattern = r'# ═+\n# SITE FOOTER.*$'
content = re.sub(footer_block_pattern, '', content, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
