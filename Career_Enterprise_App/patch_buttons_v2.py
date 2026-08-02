import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old ugly CSS and button logic with the beautiful new UI
old_block = '''/* Style the native Hero buttons using a targeted container approach */
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

new_block = '''/* ── PREMIUM HERO BUTTONS RE-DESIGN ── */
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) {
    justify-content: center !important;
    gap: 2.5rem !important;
    margin-bottom: 2.5rem !important;
}

div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button {
    border: none !important;
    outline: none !important;
    margin: 0 !important;
    padding: 18px 45px !important;
    border-radius: 100px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 65px !important;
}

div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button p {
    margin: 0 !important;
    padding: 0 !important;
    color: inherit !important;
}

/* Primary Button: Solid Vibrant Gradient */
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="primary"] {
    background: linear-gradient(135deg, #d0bcff 0%, #38bdf8 100%) !important;
    color: #03040a !important;
    box-shadow: 0 10px 35px rgba(56, 189, 248, 0.4) !important;
}
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="primary"]:hover {
    transform: translateY(-4px) scale(1.03) !important;
    box-shadow: 0 15px 45px rgba(56, 189, 248, 0.6) !important;
    color: #000 !important;
}

/* Secondary Button: Premium Glassmorphism */
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.04) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(12px) !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}
div[data-testid="stHorizontalBlock"]:has(.hero-btn-anchor) button[kind="secondary"]:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    border-color: rgba(255, 255, 255, 0.35) !important;
    transform: translateY(-4px) scale(1.03) !important;
    color: #fff !important;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 1.3, 1.3, 1])
with col2:
    st.markdown('<span class="hero-btn-anchor"></span>', unsafe_allow_html=True)
    if st.button("🚀 Forge Your Path", type="primary", use_container_width=True):
        st.session_state.current_page = "Career Engine"
        st.toast("⚡ Profile configuration engaged. Scroll down to select your academic interest and work style!")
        
with col3:
    if st.button("💡 How It Works", type="secondary", use_container_width=True):
        how_it_works_dialog()
'''

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("WARNING: Could not find old block to replace.")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesigned hero buttons.")
