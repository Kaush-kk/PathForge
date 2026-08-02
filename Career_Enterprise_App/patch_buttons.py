import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert how_it_works_dialog() at the top, right after page config
dialog_code = """

@st.dialog("💡 Welcome to PathForge")
def how_it_works_dialog():
    st.markdown('''
    ### How to use this platform
    PathForge simplifies your career planning into 3 actionable steps:
    
    1. **🚀 Career Engine (Tab 1)**
       - *Select your academic interests and work style preferences.*
       - *Discover AI-curated, future-proof career paths tailored for you.*
    
    2. **📝 Exam Directory (Tab 2)**
       - *Find the critical Indian entrance exams required for your chosen fields.*
       - *View eligibility, crucial dates, and step-by-step preparation roadmaps.*
    
    3. **🎓 Course Guide (Tab 3)**
       - *Explore premium degree programs and top colleges.*
       - *Get insights on fee structures and recommended online coaching platforms.*
       
    Ready? Close this dialog and click on the **Career Engine** tab to begin!
    ''')
"""

if "def how_it_works_dialog():" not in content:
    # Insert right after initial setup (around line 38)
    parts = content.split("# ═══════════════════════════════════════════════════════════════════════════════\n# MASTER CSS", 1)
    content = parts[0] + dialog_code + "# ═══════════════════════════════════════════════════════════════════════════════\n# MASTER CSS" + parts[1]

# 2. Remove the hardcoded HTML buttons from HERO_SHADER_HTML
old_buttons = '''        <div style="display:flex; flex-wrap:wrap; gap:1.5rem; justify-content:center;">
            <a href="javascript:void(0);" style="display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg,#d0bcff 0%,#4cd7f6 100%); color:#23005c; font-family:'Space Grotesk',sans-serif; font-size:0.85rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:18px 40px; border-radius:10px; text-decoration:none; box-shadow: 0 8px 30px rgba(208,188,255,0.3); transition:all 0.3s;">Schedule a Consult &#x2192;</a>
            <a href="javascript:void(0);" style="display:inline-flex; align-items:center; gap:10px; background:rgba(255,255,255,0.04); color:#d0bcff; font-family:'Space Grotesk',sans-serif; font-size:0.85rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:18px 40px; border-radius:10px; border:1px solid rgba(208,188,255,0.4); text-decoration:none; transition:all 0.3s;">Explore Platform</a>
        </div>'''

if old_buttons in content:
    content = content.replace(old_buttons, "")
else:
    print("WARNING: Could not find HTML buttons to remove.")

# 3. Insert native st.columns and custom CSS directly below components.html(HERO_SHADER_HTML)
# We will reduce the height of components.html slightly since the buttons are moving outside.
# Also adjust the margin-bottom to pull the native buttons up slightly over the canvas, or just place them seamlessly.

old_components_call = '''components.html(HERO_SHADER_HTML, height=640, scrolling=False)

st.markdown("""
<style>
/* Eliminate the blank space caused by the 92vh height inside the 700px iframe */
iframe[title="streamlit_components.v1.components.html"] {
    margin-bottom: -32px !important;
}
</style>
""", unsafe_allow_html=True)'''

new_components_call = '''components.html(HERO_SHADER_HTML, height=520, scrolling=False)

st.markdown("""
<style>
/* Eliminate blank space and overlay native buttons seamlessly */
iframe[title="streamlit_components.v1.components.html"] {
    margin-bottom: -10px !important;
}
/* Style the native Hero buttons using a targeted container approach */
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) {
    justify-content: center !important;
    gap: 1.5rem !important;
    margin-bottom: 2rem !important;
}
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="primary"] {
    background: linear-gradient(135deg, #d0bcff 0%, #4cd7f6 100%) !important;
    color: #23005c !important;
    border: none !important;
    padding: 10px 40px !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    box-shadow: 0 8px 30px rgba(208, 188, 255, 0.3) !important;
    transition: all 0.3s ease !important;
    height: 55px !important;
}
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.04) !important;
    color: #d0bcff !important;
    border: 1px solid rgba(208, 188, 255, 0.4) !important;
    padding: 10px 40px !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    transition: all 0.3s ease !important;
    height: 55px !important;
}
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(208, 188, 255, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 1.2, 1.2, 1])
with col2:
    st.markdown('<span class="hero-btn-anchor"></span>', unsafe_allow_html=True)
    st.button("🚀 Forge Your Path", type="primary", use_container_width=True)
with col3:
    if st.button("💡 How It Works", type="secondary", use_container_width=True):
        how_it_works_dialog()
'''

if old_components_call in content:
    content = content.replace(old_components_call, new_components_call)
else:
    print("WARNING: Could not find old components call.")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Buttons refactored to native Streamlit components.")
