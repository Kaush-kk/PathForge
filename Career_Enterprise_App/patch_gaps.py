import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS in render_nav_bar
old_nav_css = '''    st.markdown("""
    <style>
    div[data-testid="column"]:has(.nav-hiw-anchor) button {'''

new_nav_css = '''    st.markdown("""
    <style>
    /* TARGET THE HERO IFRAME CONTAINER */
    iframe[title*="components.html"],
    div[data-testid="stCustomComponentV1"] {
        margin-bottom: -2.5rem !important;
        padding-bottom: 0px !important;
    }
    
    /* TIGHTEN THE NAVIGATION / OPTION BAR */
    div[data-testid="stHorizontalBlock"]:has(.nav-hiw-anchor) {
        margin-top: 0px !important;
        padding-top: 0.25rem !important;
    }
    
    div[data-testid="column"]:has(.nav-hiw-anchor) button {'''

content = content.replace(old_nav_css, new_nav_css)

# 2. Cleanup Hero Padding in HERO_SHADER_HTML
# Look for: padding:3rem 2rem;
old_hero_padding = 'text-align:center; padding:3rem 2rem;">'
new_hero_padding = 'text-align:center; padding:3rem 2rem 0.5rem;">'
content = content.replace(old_hero_padding, new_hero_padding)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS adjustments applied.")
