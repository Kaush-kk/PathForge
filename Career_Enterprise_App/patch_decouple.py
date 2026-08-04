import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update render_nav_bar
old_nav_pattern = r"def render_nav_bar\(current_page, unique_key\):.*?st\.markdown\(\"<hr style='margin:0\.25rem 0 0\.5rem 0; border:none; border-top:1px solid rgba\(255,255,255,0\.08\);'>\", unsafe_allow_html=True\)"
new_nav = '''def render_nav_bar(current_page, unique_key):
    nav_items = [
        ("🚀  Career Engine", "Career Engine"),
        ("📝  Exam Directory", "Exam Directory"),
        ("🎓  Course Guide", "Course Guide"),
    ]
    nav_cols = st.columns([1.5, 1.5, 1.5, 3, 1.5])
    
    for i, (label, page_key) in enumerate(nav_items):
        with nav_cols[i]:
            is_active = (current_page == page_key)
            if st.button(
                label,
                key=f"nav_{page_key}_{unique_key}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                if not is_active:
                    st.session_state.current_page = page_key
                    st.rerun()
                    
    with nav_cols[4]:
        st.markdown('<span class="nav-hiw-anchor"></span>', unsafe_allow_html=True)
        if st.button("💡 How It Works", key=f"nav_hiw_{unique_key}", use_container_width=True):
            how_it_works_dialog()
            
    st.markdown("""
    <style>
    div[data-testid="column"]:has(.nav-hiw-anchor) button {
        background: rgba(15, 23, 42, 0.6) !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 100px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        min-height: 42px !important;
    }
    div[data-testid="column"]:has(.nav-hiw-anchor) button:hover {
        background: rgba(15, 23, 42, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    <hr style='margin:0.25rem 0 0.5rem 0; border:none; border-top:1px solid rgba(255,255,255,0.08);'>
    """, unsafe_allow_html=True)'''

content, count1 = re.subn(old_nav_pattern, new_nav, content, flags=re.DOTALL)
print(f"NavBar replaced: {count1}")

# 2. Clean up Hero Section buttons
old_hero_buttons_pattern = r"st\.markdown\(\"\"\"\n<style>\n/\* Eliminate blank space and overlay native buttons seamlessly \*/.*?how_it_works_dialog\(\)"
content, count2 = re.subn(old_hero_buttons_pattern, "", content, flags=re.DOTALL)
print(f"Hero Buttons replaced: {count2}")

# 3. Add pill badge before st.columns(2, gap="medium")
badge_html = '''    st.markdown("""
    <div style="display:flex; justify-content:center; margin-bottom: 2rem;">
        <div style="display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg, rgba(139, 92, 246, 0.8) 0%, rgba(56, 189, 248, 0.8) 100%); color:#ffffff; padding:12px 30px; border-radius:100px; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:1rem; letter-spacing:0.05em; text-transform:uppercase; border:1px solid rgba(255,255,255,0.2); box-shadow:0 0 20px rgba(139, 92, 246, 0.3), inset 0 0 10px rgba(56, 189, 248, 0.2); backdrop-filter:blur(8px);">
            🚀 Step 1: Select Your Interests Below
        </div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="medium")'''

if 'col1, col2 = st.columns(2, gap="medium")' in content:
    content = content.replace('    col1, col2 = st.columns(2, gap="medium")', badge_html)
    print("Badge replaced: 1")
else:
    print("Badge replaced: 0")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
