import streamlit as st
import streamlit.components.v1 as components
import json
import re
import html
import time
import os
from st_supabase_connection import SupabaseConnection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INFO_PATH  = os.path.join(BASE_DIR, "information.md")
INFO2_PATH = os.path.join(BASE_DIR, "information2.md")
INFO3_PATH = os.path.join(BASE_DIR, "information3.md")

@st.cache_resource(show_spinner=False)
def init_db_connection():
    """Establish and cache the Supabase connection globally."""
    return st.connection("supabase", type=SupabaseConnection)



@st.cache_data(show_spinner=False)
def load_course_data(mtime: float = 0.0):
    """Load premium degree data from information3.md."""
    try:
        with open(INFO3_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content.startswith("```json"):
            content = content.split("\n", 1)[1]
        elif content.startswith("```"):
            content = content.split("\n", 1)[1]
        if content.endswith("```"):
            content = content.rsplit("\n", 1)[0]
        return json.loads(content)
    except Exception:
        return []

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Beyond Engineering | Discover Your True Path",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)



@st.dialog("💡 Welcome to PathForge")
def how_it_works_dialog():
    st.markdown('''
    ## Welcome to PathForge: Break the Matrix. 🚀
Forget the traditional tunnel vision. PathForge is your personal, interactive navigation engine designed to map out elite careers across Science, Arts, and Commerce. 

Here is how to forge your path:

### 1️⃣ The Career Engine (Tab 1)
Explore over 185+ highly detailed, non-overlapping careers. Click any career card to open its **Pathway Flowchart**, mapping your exact chronological steps from high school to professional income.

### 2️⃣ The Exam Directory & Course Guide (Tabs 2 & 3)
Access a hardcoded, SSL-verified database of 50+ crucial entrance exams and 117+ Master Degrees. Filter by specialization and jump straight to official portals without hitting security walls.

### 3️⃣ Build Your Forge (The Sidebar HUD) 🛠️
**[NEW]** PathForge now features dynamic User Memory! 
* Click **"Log In / Register"** to secure your profile.
* When exploring a career, click the massive **"⭐ Save to My Forge"** button in the sidebar.
* Your sidebar transforms into a personal HUD, storing your shortlisted careers, required exams, and a private **"My Notes"** matrix that saves your thoughts to the cloud instantly. Your data stays with you, no matter where you navigate.
* To "log-out" simply refresh the page.
    ''')
# ═══════════════════════════════════════════════════════════════════════════════
# MASTER CSS — Enterprise Dark Mode Design System
# ═══════════════════════════════════════════════════════════════════════════════
MASTER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Hanken+Grotesk:wght@400;600;700&display=swap');
/* ── Google Fonts ──────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

/* ── Design Tokens ─────────────────────────────────────────────────────── */
:root {
    --void:             #03040a;
    --surface-0:        #080b14;
    --surface-1:        #0d1021;
    --surface-2:        #111528;
    --glass-fill:       rgba(255,255,255,0.035);
    --glass-border:     rgba(255,255,255,0.07);
    --glass-hover:      rgba(59,130,246,0.18);
    --neon-blue:        #3b82f6;
    --neon-blue-dim:    rgba(59,130,246,0.15);
    --neon-blue-glow:   rgba(59,130,246,0.35);
    --neon-purple:      #8b5cf6;
    --neon-purple-dim:  rgba(139,92,246,0.12);
    --neon-purple-glow: rgba(139,92,246,0.3);
    --neon-cyan:        #06b6d4;
    --neon-cyan-dim:    rgba(6,182,212,0.12);
    --accent-green:     #10b981;
    --accent-green-dim: rgba(16,185,129,0.1);
    --accent-amber:     #f59e0b;
    --text-primary:     #f1f5f9;
    --text-secondary:   #64748b;
    --text-muted:       #2d3a52;
    --text-dim:         #94a3b8;
    --radius:           16px;
    --radius-lg:        22px;
    --radius-xl:        28px;
    --transition:       0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
    --shadow-card:      0 4px 24px rgba(0,0,0,0.4), 0 1px 4px rgba(0,0,0,0.3);
    --shadow-hover:     0 0 40px rgba(59,130,246,0.22), 0 0 90px rgba(139,92,246,0.12), 0 32px 80px rgba(0,0,0,0.6);
    --shadow-3d:        0 30px 80px rgba(0,0,0,0.7), 0 0 60px rgba(59,130,246,0.25), 0 0 120px rgba(139,92,246,0.15);
    --perspective:      1200px;
}

/* ── Global Reset & Base ───────────────────────────────────────────────── */
.surgical-dark-box {
    background: rgba(15, 15, 25, 0.88) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    padding: 16px !important;
}

html {
    background-color: var(--void) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-primary) !important;
}
body {
    background-color: var(--void) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-primary) !important;
}
/* Make Streamlit containers transparent so WebGL canvas shows through */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"],
[data-testid="stHeader"],
section.main {
    background: transparent !important;
    background-color: transparent !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-primary) !important;
}
[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    }

[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}
section.main > div {
    padding: 0 !important;
}
#MainMenu, footer, header { display: none !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }
/* stSidebar display:none PURGED — visibility now managed by conditional CSS injection */

/* ── Keyframe: Levitate (smooth infinite float) ────────────────────────── */
@keyframes levitate {
    0%   { transform: translateY(0px) scale(1); }
    25%  { transform: translateY(-10px) scale(1.012); }
    50%  { transform: translateY(-18px) scale(1.018); }
    75%  { transform: translateY(-8px) scale(1.008); }
    100% { transform: translateY(0px) scale(1); }
}

/* ── Keyframe: Orb Drift + Float ───────────────────────────────────────── */
@keyframes orb-drift {
    0%, 100% { transform: translate(0, 0) scale(1); }
    25%       { transform: translate(20px, -30px) scale(1.06); }
    50%       { transform: translate(35px, -15px) scale(1.04); }
    75%       { transform: translate(-10px, 20px) scale(0.96); }
}
@keyframes orb-float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-22px); }
}

/* ── Keyframe: Gradient Border Rotation ────────────────────────────────── */
@keyframes gradient-rotate {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Keyframe: Blink pulse ─────────────────────────────────────────────── */
@keyframes blink {
    0%, 100% { opacity: 1; box-shadow: 0 0 10px var(--accent-green); }
    50%       { opacity: 0.35; box-shadow: 0 0 4px var(--accent-green); }
}
@keyframes blink-hero {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.35; }
}

/* ── Orb Background ────────────────────────────────────────────────────── */
.orb-bg {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(160px);
    will-change: transform;
}
.orb-1 {
    width: 950px; height: 950px;
    background: radial-gradient(circle, rgba(59,130,246,0.28) 0%, transparent 65%);
    top: -300px; right: -200px;
    animation: orb-drift 18s ease-in-out infinite, orb-float 9s ease-in-out infinite;
}
.orb-2 {
    width: 750px; height: 750px;
    background: radial-gradient(circle, rgba(139,92,246,0.24) 0%, transparent 65%);
    bottom: -200px; left: -150px;
    animation: orb-drift 22s ease-in-out infinite reverse, orb-float 12s ease-in-out infinite 3s;
}
.orb-3 {
    width: 420px; height: 420px;
    background: radial-gradient(circle, rgba(6,182,212,0.15) 0%, transparent 65%);
    top: 50%; left: 42%;
    animation: orb-float 8s ease-in-out infinite 1.5s;
}

/* ── Page Wrapper ──────────────────────────────────────────────────────── */
.page-wrapper {
    position: relative;
    z-index: 1;
    padding: 0 2rem 2rem;
    max-width: 1320px;
    margin: 0 auto;
}
@media (max-width: 768px) { .page-wrapper { padding: 0 1rem 3rem; } }

/* ── Tab overrides ─────────────────────────────────────────────────────── */
[data-testid="stTabs"] {
    background: transparent !important;
}
[data-testid="stTabsTabList"] {
    background: var(--surface-1) !important;
    border-bottom: 1px solid var(--glass-border) !important;
    padding: 0 2rem !important;
    gap: 0 !important;
    justify-content: flex-start !important;
}
button[data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-secondary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    padding: 1rem 1.6rem !important;
    border-bottom: 2px solid transparent !important;
    transition: all var(--transition) !important;
    white-space: nowrap !important;
}
button[data-baseweb="tab"]:hover {
    color: var(--text-primary) !important;
    background: rgba(255,255,255,0.03) !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--neon-blue) !important;
    border-bottom-color: var(--neon-blue) !important;
    background: transparent !important;
}
[data-testid="stTabsContent"] {
    background: transparent !important;
    padding: 0 !important;
}

/* ── Hero ───────────────────────────────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 0.5rem 2rem 1.5rem;
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.22);
    border-radius: 100px;
    padding: 5px 18px;
    font-size: 0.7rem;
    font-weight: 600;
    color: #60a5fa;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1.75rem;
    font-family: 'Space Grotesk', sans-serif;
}
.hero-dot {
    width: 6px; height: 6px;
    background: #3b82f6;
    border-radius: 50%;
    box-shadow: 0 0 8px #3b82f6;
    animation: blink-hero 2s ease-in-out infinite;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.6rem, 6vw, 5rem);
    font-weight: 800;
    line-height: 1.03;
    letter-spacing: -0.035em;
    background: linear-gradient(140deg,
        #ffffff 0%,
        #e2e8f0 25%,
        #93c5fd 55%,
        #c4b5fd 80%,
        #818cf8 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.25rem;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto 3rem;
    line-height: 1.75;
}
.hero-stats {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
    flex-wrap: wrap;
    margin-bottom: 3.5rem;
}
.hero-stat { text-align: center; }
.hero-stat-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-stat-label {
    font-size: 0.7rem;
    color: var(--text-secondary);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 2px;
}
.hero-stat-sep {
    width: 1px;
    height: 36px;
    background: var(--glass-border);
}

/* ── Gradient Divider ──────────────────────────────────────────────────── */
.gradient-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(59,130,246,0.4), rgba(139,92,246,0.35), transparent);
    margin: 0 0 2.5rem;
}

/* ── Hero Banner (Full-screen animated shader hero) ───────────────────── */
.hero-banner-wrapper {
    position: relative;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    min-height: 92vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin-top: -1.5rem;
}
.hero-banner-content {
    position: relative;
    z-index: 10;
    text-align: center;
    padding: 2rem;
    max-width: 900px;
    margin: 0 auto;
}
.hero-banner-content h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(3.5rem, 10vw, 8rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    background: linear-gradient(180deg, #ffffff 0%, #d0bcff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.25rem;
}
.hero-banner-content p {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    line-height: 1.6;
    color: #cbc3d7;
    max-width: 640px;
    margin: 0 auto 2.5rem;
}
.hero-banner-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
}
.hero-btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #d0bcff 0%, #4cd7f6 100%);
    color: #23005c;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 14px 32px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}
.hero-btn-primary:hover {
    filter: brightness(1.15);
    transform: scale(1.03);
}
.hero-btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: transparent;
    color: #d0bcff;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 14px 32px;
    border-radius: 8px;
    border: 1px solid #d0bcff;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}
.hero-btn-secondary:hover {
    background: rgba(208, 188, 255, 0.1);
}
.hero-scroll-indicator {
    position: absolute;
    bottom: 2.5rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    opacity: 0.5;
    animation: bounce-arrow 2s ease-in-out infinite;
    font-size: 2rem;
    color: #cbc3d7;
}
@keyframes bounce-arrow {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(12px); }
}

/* ── Site Footer ──────────────────────────────────────────────────────── */
.site-footer {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    padding: 3rem 2rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    background: #0e0e0e;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin-top: 4rem;
}
.site-footer-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #d0bcff;
}
.site-footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
}
.site-footer-links a {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: #94a3b8;
    text-decoration: none;
    transition: color 0.3s;
}
.site-footer-links a:hover {
    color: #d0bcff;
}
.site-footer-copy {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    color: #64748b;
}

/* ── Selection Section ─────────────────────────────────────────────────── */
.selection-section {
    background: var(--glass-fill);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-xl);
    padding: 2rem 2.25rem;
    margin-bottom: 2.5rem;
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
}
.section-eyebrow {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    font-family: 'Space Grotesk', sans-serif;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-eyebrow::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--glass-border);
}

/* ── Selectbox Overrides ───────────────────────────────────────────────── */
[data-testid="stSelectbox"] label {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: var(--text-secondary) !important;
    margin-bottom: 0.5rem !important;
}
[data-testid="stSelectbox"] > div > div {
    background: rgba(10,14,28,0.8) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius) !important;
    color: var(--text-primary) !important;
    backdrop-filter: blur(12px) !important;
    transition: border-color var(--transition), box-shadow var(--transition) !important;
    min-height: 52px !important;
}
[data-testid="stSelectbox"] > div > div:hover,
[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: rgba(59,130,246,0.5) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.08), 0 0 20px rgba(59,130,246,0.1) !important;
}
[data-testid="stSelectbox"] > div > div > div {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
}
[data-testid="stSelectbox"] svg { color: var(--text-secondary) !important; }

/* ── Results Banner — Levitate Animation ───────────────────────────────── */
.results-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    background: linear-gradient(135deg,
        rgba(59,130,246,0.08) 0%,
        rgba(139,92,246,0.06) 100%
    );
    border: 1px solid rgba(59,130,246,0.22);
    border-radius: var(--radius-lg);
    padding: 1.25rem 1.75rem;
    margin-top: 1.5rem !important;
    margin-bottom: 2rem !important;
    position: relative;
    z-index: 2;
    animation: levitate 6s ease-in-out infinite;
    will-change: transform;
    box-shadow: 0 8px 32px rgba(59,130,246,0.1), 0 2px 8px rgba(0,0,0,0.3);
}
.results-left {
    display: flex;
    align-items: center;
    gap: 14px;
}
.results-count {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
}
.results-label {
    font-size: 0.9rem;
    color: var(--text-secondary);
    line-height: 1.4;
    font-weight: 500;
}
.results-label strong {
    color: var(--text-primary);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
}
.results-tag {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.72rem;
    font-weight: 600;
    color: #34d399;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.04em;
}

/* ── Bento Cards Grid ──────────────────────────────────────────────────── */
.bento-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
    perspective: var(--perspective);
}

/* ══════════════════════════════════════════════════════════════════════
   BENTO CARD — 3D Perspective Hover + Glassmorphic Depth
   ══════════════════════════════════════════════════════════════════════ */
.bento-card {
    position: relative;
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.055) 0%,
        rgba(255,255,255,0.028) 50%,
        rgba(59,130,246,0.018) 100%
    );
    /* Asymmetric glass border — top-left reflection highlight */
    border: 1px solid var(--glass-border);
    border-top-color:    rgba(255,255,255,0.12);
    border-left-color:   rgba(255,255,255,0.10);
    border-bottom-color: rgba(0,0,0,0.20);
    border-right-color:  rgba(0,0,0,0.15);
    border-radius: var(--radius-xl);
    padding: 2.25rem 2.5rem;
    backdrop-filter: blur(32px) saturate(180%);
    -webkit-backdrop-filter: blur(32px) saturate(180%);
    /* FIX OVERLAP: allow card height to grow with child content */
    overflow: visible !important;
    height: auto !important;
    min-height: fit-content !important;
    transform-style: preserve-3d;
    transform: perspective(var(--perspective)) rotateX(0deg) rotateY(0deg) translateZ(0px);
    transition:
        transform       0.4s cubic-bezier(0.23, 1, 0.32, 1),
        border-color    0.4s ease,
        box-shadow      0.4s ease;
    cursor: default;
    box-shadow: var(--shadow-card);
    will-change: transform, box-shadow;
}

/* Glass inner top-edge shine */
.bento-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg,
        transparent 0%,
        rgba(255,255,255,0.35) 30%,
        rgba(255,255,255,0.55) 50%,
        rgba(255,255,255,0.35) 70%,
        transparent 100%
    );
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
    pointer-events: none;
    z-index: 2;
}

/* Inner gradient fill */
.bento-card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: var(--radius-xl);
    background: linear-gradient(135deg,
        rgba(59,130,246,0.05) 0%,
        transparent 45%,
        rgba(139,92,246,0.04) 100%);
    pointer-events: none;
    z-index: 1;
}

/* ── ELEVATED HOVER — straight-up lift, no tilt, premium neon depth ──── */
.bento-card:hover {
    transform: perspective(var(--perspective))
               translateY(-6px)
               translateZ(10px)
               scale(1.008);
    border-top-color:    rgba(255,255,255,0.22);
    border-left-color:   rgba(255,255,255,0.18);
    border-bottom-color: rgba(59,130,246,0.35);
    border-right-color:  rgba(139,92,246,0.25);
    box-shadow:
        /* Heavy diffused drop shadow */
        0 40px 100px rgba(0,0,0,0.75),
        0 20px 60px  rgba(0,0,0,0.55),
        /* Blue neon corona */
        0 0  60px rgba(59,130,246,0.30),
        0 0 120px rgba(59,130,246,0.16),
        /* Purple ambient */
        0 0  80px rgba(139,92,246,0.18),
        /* Cyan edge accent */
        0 0  30px rgba(6,182,212,0.10);
}

/* Top gradient accent line */
.bento-accent {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
    opacity: 0;
    transition: opacity var(--transition);
    z-index: 3;
}
.bento-card:hover .bento-accent { opacity: 1; }

/* Card header row */
.card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 0.75rem;
    position: relative;
    z-index: 2;
}
.card-index {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--text-muted);
    text-transform: uppercase;
    white-space: nowrap;
    margin-top: 4px;
    flex-shrink: 0;
}

/* Career name */
.career-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.25rem, 2.5vw, 1.7rem);
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.2;
    letter-spacing: -0.02em;
    margin-bottom: 0.75rem;
    position: relative;
    z-index: 2;
}

/* Career description */
.career-description {
    font-size: 0.92rem;
    color: var(--text-dim);
    line-height: 1.72;
    margin-bottom: 1.6rem;
    padding-left: 0.75rem;
    border-left: 2px solid rgba(99,102,241,0.35);
    position: relative;
    z-index: 2;
}

/* ── Income Badge — raises off card on hover ───────────────────────────── */
.income-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--accent-green-dim);
    border: 1px solid rgba(16,185,129,0.22);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.8rem;
    font-weight: 600;
    color: #34d399;
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 1.75rem;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
    transition:
        transform  0.3s cubic-bezier(0.23, 1, 0.32, 1),
        box-shadow 0.3s ease,
        border-color 0.3s ease;
    cursor: default;
}
.income-badge:hover {
    transform: scale(1.08) translateY(-3px);
    box-shadow:
        0 8px 28px rgba(16,185,129,0.30),
        0 0  20px rgba(16,185,129,0.20);
    border-color: rgba(16,185,129,0.55);
}
.income-dot {
    width: 7px; height: 7px;
    background: var(--accent-green);
    border-radius: 50%;
    flex-shrink: 0;
    box-shadow: 0 0 10px var(--accent-green);
    animation: blink 2.5s ease-in-out infinite;
}

/* ── Startup Pill — raises off card on hover ───────────────────────────── */
.startup-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border-radius: 100px;
    padding: 3px 12px;
    font-size: 0.68rem;
    font-weight: 700;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    position: relative;
    z-index: 2;
    transition:
        transform  0.3s cubic-bezier(0.23, 1, 0.32, 1),
        box-shadow 0.3s ease,
        border-color 0.3s ease;
    cursor: default;
}
.startup-pill:hover { transform: scale(1.10) translateY(-4px); }

.startup-massive {
    background: rgba(239,68,68,0.10);
    border: 1px solid rgba(239,68,68,0.25);
    color: #f87171;
}
.startup-massive:hover {
    box-shadow: 0 8px 28px rgba(239,68,68,0.28), 0 0 16px rgba(239,68,68,0.20);
    border-color: rgba(239,68,68,0.60);
}
.startup-high {
    background: rgba(245,158,11,0.10);
    border: 1px solid rgba(245,158,11,0.25);
    color: #fbbf24;
}
.startup-high:hover {
    box-shadow: 0 8px 28px rgba(245,158,11,0.28), 0 0 16px rgba(245,158,11,0.20);
    border-color: rgba(245,158,11,0.60);
}
.startup-medium {
    background: rgba(59,130,246,0.10);
    border: 1px solid rgba(59,130,246,0.22);
    color: #93c5fd;
}
.startup-medium:hover {
    box-shadow: 0 8px 28px rgba(59,130,246,0.28), 0 0 16px rgba(59,130,246,0.20);
    border-color: rgba(59,130,246,0.60);
}
.startup-low {
    background: rgba(100,116,139,0.10);
    border: 1px solid rgba(100,116,139,0.20);
    color: #94a3b8;
}
.startup-low:hover {
    box-shadow: 0 6px 20px rgba(100,116,139,0.20);
    border-color: rgba(100,116,139,0.45);
}

/* Info grid inside card */
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.1rem 2rem;
    margin-bottom: 1.6rem;
    position: relative;
    z-index: 2;
}
@media (max-width: 640px) { .info-grid { grid-template-columns: 1fr; } }
.info-cell { display: flex; flex-direction: column; gap: 5px; }
.info-label {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-secondary);
    font-family: 'Space Grotesk', sans-serif;
}
.info-value { font-size: 0.88rem; color: var(--text-dim); line-height: 1.55; }
.full-width { grid-column: 1 / -1; }

/* Pathway section */
.pathway-block {
    border-top: 1px solid var(--glass-border);
    padding-top: 1.5rem;
    margin-top: 0.5rem;
    position: relative;
    z-index: 2;
}
.pathway-title {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-secondary);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 1rem;
}
.pathway-steps { display: flex; flex-direction: column; gap: 0.65rem; }
.pathway-step {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 0.88rem;
    color: var(--text-dim);
    line-height: 1.55;
}
.step-badge {
    flex-shrink: 0;
    width: 22px; height: 22px;
    border-radius: 50%;
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.22);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.6rem;
    font-weight: 800;
    color: #60a5fa;
    font-family: 'Space Grotesk', sans-serif;
    margin-top: 2px;
}

/* Startup Detail — FIX OVERLAP: relative flow so card expands naturally */
.startup-detail {
    position: relative !important;
    display: block !important;
    width: 100% !important;
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: var(--radius);
    padding: 1rem 1.25rem;
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
    clear: both !important;
    font-size: 0.88rem;
    color: #c4b5fd;
    line-height: 1.65;
    z-index: 2;
    box-sizing: border-box;
}

/* ══════════════════════════════════════════════════════════════════════
   CTA BUTTON — Animated rotating gradient border (dynamic lighting)
   ══════════════════════════════════════════════════════════════════════ */
[data-testid="stButton"] > button {
    position: relative !important;
    background: rgba(8, 10, 20, 0.90) !important;
    border: none !important;
    border-radius: 100px !important;
    color: #c4b5fd !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    padding: 0.6rem 1.7rem !important;
    margin-top: 1.25rem !important;
    cursor: pointer !important;
    z-index: 1 !important;
    transition: color 0.3s ease, transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s ease !important;
    box-shadow:
        0 0 0 1.5px rgba(139,92,246,0.50),
        0 4px 20px rgba(139,92,246,0.18),
        inset 0 1px 0 rgba(255,255,255,0.06) !important;
    outline: none !important;
    overflow: visible !important;
}

/* Animated spinning gradient border via ::before */
[data-testid="stButton"] > button::before {
    content: '';
    position: absolute;
    inset: -2px;
    border-radius: 100px;
    background: linear-gradient(
        90deg,
        #3b82f6 0%,
        #8b5cf6 20%,
        #06b6d4 40%,
        #f59e0b 60%,
        #ec4899 80%,
        #3b82f6 100%
    );
    background-size: 300% 300%;
    animation: gradient-rotate 3s linear infinite;
    z-index: -1;
    opacity: 0.85;
    transition: opacity 0.3s ease;
}

/* Dark pill background behind text */
[data-testid="stButton"] > button::after {
    content: '';
    position: absolute;
    inset: 1.5px;
    border-radius: 100px;
    background: rgba(8, 10, 20, 0.92);
    z-index: -1;
}

[data-testid="stButton"] > button:hover {
    color: #ede9fe !important;
    transform: translateY(-3px) scale(1.04) !important;
    box-shadow:
        0 14px 44px rgba(139,92,246,0.38),
        0  0   55px rgba(59,130,246,0.28),
        inset 0 1px 0 rgba(255,255,255,0.12) !important;
}
[data-testid="stButton"] > button:hover::before { opacity: 1; }

/* ── Alert / Info / Warning ────────────────────────────────────────────── */
[data-testid="stAlert"] {
    background: rgba(59,130,246,0.05) !important;
    border: 1px solid rgba(59,130,246,0.18) !important;
    border-radius: var(--radius-lg) !important;
    color: #93c5fd !important;
}
[data-testid="stAlert"] p,
[data-testid="stAlert"] strong { color: #93c5fd !important; }

/* ── Placeholder Tab Content ───────────────────────────────────────────── */
.placeholder-pane {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 380px;
    gap: 1.25rem;
    text-align: center;
    padding: 4rem 2rem;
}
.placeholder-icon {
    font-size: 3.5rem;
    filter: grayscale(0.4);
    margin-bottom: 0.5rem;
    animation: levitate 7s ease-in-out infinite;
}
.placeholder-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
}
.placeholder-sub {
    font-size: 0.9rem;
    color: var(--text-secondary);
    max-width: 420px;
    line-height: 1.7;
}
.placeholder-badge {
    display: inline-block;
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 100px;
    padding: 5px 16px;
    font-size: 0.7rem;
    font-weight: 700;
    color: #a78bfa;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Column spacing ────────────────────────────────────────────────────── */
[data-testid="column"] { padding: 0 0.5rem !important; }
[data-testid="stHorizontalBlock"] { gap: 0 !important; }

/* ══════════════════════════════════════════════════════════════════════
   PATHWAY FLOWCHART DIALOG — Vertical Chronological Timeline
   ══════════════════════════════════════════════════════════════════════ */
.timeline-wrap {
    padding: 1.5rem 0.5rem;
}
.timeline-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
    letter-spacing: -0.02em;
}
.timeline-sub {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.6;
}
.timeline-track {
    display: flex;
    flex-direction: column;
    gap: 0;
    position: relative;
    padding-left: 48px;
}
.timeline-track::before {
    content: '';
    position: absolute;
    left: 18px;
    top: 22px;
    bottom: 22px;
    width: 2px;
    background: linear-gradient(180deg,
        rgba(59,130,246,0.7) 0%,
        rgba(139,92,246,0.6) 50%,
        rgba(6,182,212,0.5) 100%
    );
    border-radius: 2px;
}
.tl-node {
    position: relative;
    margin-bottom: 1.5rem;
    padding: 1.1rem 1.4rem;
    background: var(--glass-fill);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    backdrop-filter: blur(12px);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}
.tl-node:hover {
    border-color: rgba(59,130,246,0.35);
    box-shadow: 0 0 24px rgba(59,130,246,0.12);
}
.tl-dot {
    position: absolute;
    left: -38px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 2px solid;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.55rem;
    font-weight: 800;
    font-family: 'Space Grotesk', sans-serif;
    background: var(--surface-1);
    z-index: 1;
}
.tl-dot-blue  { border-color: var(--neon-blue);   color: var(--neon-blue);   box-shadow: 0 0 10px rgba(59,130,246,0.5); }
.tl-dot-purple{ border-color: var(--neon-purple); color: var(--neon-purple); box-shadow: 0 0 10px rgba(139,92,246,0.5); }
.tl-dot-cyan  { border-color: var(--neon-cyan);   color: var(--neon-cyan);   box-shadow: 0 0 10px rgba(6,182,212,0.5); }
.tl-dot-green { border-color: var(--accent-green);color: var(--accent-green);box-shadow: 0 0 10px rgba(16,185,129,0.5); }
.tl-label {
    font-size: 0.58rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
    font-family: 'Space Grotesk', sans-serif;
}
.tl-content {
    font-size: 0.9rem;
    color: var(--text-dim);
    line-height: 1.6;
}
.tl-tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.5rem;
}
.tl-tag {
    display: inline-block;
    border-radius: 100px;
    padding: 2px 10px;
    font-size: 0.68rem;
    font-weight: 600;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.04em;
}
.tl-tag-blue   { background: rgba(59,130,246,0.12);  color: #93c5fd;  border: 1px solid rgba(59,130,246,0.28); }
.tl-tag-purple { background: rgba(139,92,246,0.12); color: #c4b5fd; border: 1px solid rgba(139,92,246,0.28); }
.tl-tag-green  { background: rgba(16,185,129,0.10);  color: #34d399;  border: 1px solid rgba(16,185,129,0.25); }

/* ══════════════════════════════════════════════════════════════════════
   EXAM DIRECTORY — Tab 2 UI Components
   ══════════════════════════════════════════════════════════════════════ */
.exam-section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.5rem, 3vw, 2.2rem);
    font-weight: 800;
    letter-spacing: -0.025em;
    background: linear-gradient(135deg, #f1f5f9 0%, #93c5fd 55%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}
.exam-section-sub {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.65;
}
.exam-meta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.85rem;
}
.exam-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    border-radius: 100px;
    padding: 3px 11px;
    font-size: 0.7rem;
    font-weight: 600;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: 0.04em;
}
.exam-chip-blue   { background: rgba(59,130,246,0.1);  color: #93c5fd;  border: 1px solid rgba(59,130,246,0.25); }
.exam-chip-amber  { background: rgba(245,158,11,0.1);  color: #fbbf24;  border: 1px solid rgba(245,158,11,0.25); }
.exam-chip-green  { background: rgba(16,185,129,0.10); color: #34d399;  border: 1px solid rgba(16,185,129,0.22); }
.exam-chip-purple { background: rgba(139,92,246,0.10); color: #c4b5fd;  border: 1px solid rgba(139,92,246,0.25); }
.exam-section-label {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-secondary);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 0.55rem;
    margin-top: 0.9rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.exam-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--glass-border);
}
.exam-roadmap-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 0.87rem;
    color: var(--text-dim);
    line-height: 1.6;
    margin-bottom: 0.55rem;
}
.exam-step-num {
    flex-shrink: 0;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.28);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.58rem;
    font-weight: 800;
    color: #60a5fa;
    font-family: 'Space Grotesk', sans-serif;
    margin-top: 2px;
    flex-shrink: 0;
}
.exam-count-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59,130,246,0.07);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: var(--radius-lg);
    padding: 0.8rem 1.4rem;
    margin-bottom: 1.5rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem;
    color: #93c5fd;
    font-weight: 500;
}
.exam-count-badge strong {
    font-weight: 800;
    color: #60a5fa;
    font-size: 1.1rem;
}

/* ══════════════════════════════════════════════════════════════════
   GLASSMORPHIC AUTH MODAL
   ══════════════════════════════════════════════════════════════════ */
.login-glass-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem 0.5rem 1.75rem;
    gap: 0.65rem;
}
.login-logo-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, rgba(139,92,246,0.15) 0%, rgba(59,130,246,0.12) 100%);
    border: 1px solid rgba(139,92,246,0.35);
    border-radius: 100px;
    padding: 7px 22px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    color: #c4b5fd;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}
.login-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.1rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(140deg, #ffffff 0%, #c4b5fd 55%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}
.login-sub {
    font-size: 0.875rem;
    color: var(--text-secondary);
    text-align: center;
    line-height: 1.65;
    max-width: 340px;
    margin: 0 auto;
}

/* ══════════════════════════════════════════════════════════════════
   CAREER DETAILS SIDEBAR
   ══════════════════════════════════════════════════════════════════ */
.sidebar-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.45), rgba(59,130,246,0.35), transparent);
    margin: 1.5rem 0;
}
.sidebar-career-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.025em;
    background: linear-gradient(135deg, #f1f5f9 0%, #93c5fd 60%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.25;
    margin-bottom: 1rem;
}
.sidebar-income-block {
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.22);
    border-radius: var(--radius);
    padding: 0.75rem 1rem;
    margin-bottom: 1.5rem;
}
.sidebar-income-label {
    font-size: 0.56rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-secondary);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 2px;
}
.sidebar-income-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #34d399;
}
.sidebar-section-label {
    font-size: 0.58rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-secondary);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 0.85rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sidebar-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--glass-border);
}
.sidebar-pathway-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 0.85rem;
    font-size: 0.83rem;
    color: var(--text-dim);
    line-height: 1.6;
}
.sidebar-step-badge {
    flex-shrink: 0;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.30);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.58rem;
    font-weight: 800;
    color: #c4b5fd;
    font-family: 'Space Grotesk', sans-serif;
    margin-top: 1px;
}

/* ══════════════════════════════════════════════════════════════════
   SIDEBAR HUD OVERRIDES — Stitch Design Translation
   ══════════════════════════════════════════════════════════════════ */

/* ── Sidebar Base Container ─────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(9, 9, 14, 0.30) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.12) !important;
}

/* ── Slim Custom Scrollbar (4px, purple hover) ──────────────────────────── */
[data-testid="stSidebarContent"]::-webkit-scrollbar { width: 4px; }
[data-testid="stSidebarContent"]::-webkit-scrollbar-track { background: transparent; }
[data-testid="stSidebarContent"]::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.10);
    border-radius: 4px;
}
[data-testid="stSidebarContent"]::-webkit-scrollbar-thumb:hover {
    background: rgba(192, 132, 252, 0.50);
}

/* ── Memory Selectbox — cyber-cyan theme ────────────────────────────────── */
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div[data-baseweb="select"] {
    background: rgba(10, 10, 15, 0.60) !important;
    border: 1px solid rgba(139, 92, 246, 0.30) !important;
    color: #e4e1e9 !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div[data-baseweb="select"]:hover {
    border-color: #22D3EE !important;
    box-shadow: 0 0 15px rgba(34, 211, 238, 0.40) !important;
}

/* ── Notes Textarea — dark coding terminal ──────────────────────────────── */
[data-testid="stSidebar"] [data-baseweb="textarea"] {
    background: rgba(10, 10, 15, 0.80) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #e4e1e9 !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] [data-baseweb="textarea"]:focus-within {
    border-color: #C084FC !important;
    box-shadow: 0 0 15px rgba(192, 132, 252, 0.40) !important;
}
[data-testid="stSidebar"] [data-baseweb="textarea"] textarea {
    color: #e4e1e9 !important;
    background: transparent !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    line-height: 1.7 !important;
}

/* ── Primary Button — Save to Forge (orange→red gradient) ───────────────── */
[data-testid="stSidebar"] button[kind="primary"] {
    background: linear-gradient(to right, #f97316, #fb923c, #ef4444) !important;
    border: none !important;
    border-radius: 12px !important;
    color: black !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    overflow: hidden !important;
}
[data-testid="stSidebar"] button[kind="primary"]:hover {
    box-shadow: 0 0 30px rgba(249, 115, 22, 0.60) !important;
    transform: translateY(-2px) !important;
}
[data-testid="stSidebar"] button[kind="primary"] p {
    color: black !important;
}

/* ── 4-Tab Matrix — neon purple active state ────────────────────────────── */
[data-testid="stSidebar"] [data-testid="stTabs"] button[data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    color: #cfc2d6 !important;
    padding: 12px 0 !important;
    flex: 1 !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] [data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    color: #C084FC !important;
    border-bottom-color: #C084FC !important;
    text-shadow: 0 0 10px rgba(192, 132, 252, 1.0) !important;
}

/* ── Secondary Button (Close / Save Notes) ──────────────────────────────── */
[data-testid="stSidebar"] button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 8px !important;
    color: #cfc2d6 !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] button[kind="secondary"]:hover {
    border-color: rgba(221, 183, 255, 0.50) !important;
    background: rgba(255, 255, 255, 0.10) !important;
    color: #e4e1e9 !important;
}
[data-testid="stSidebar"] button[kind="secondary"] p {
    color: inherit !important;
}
</style>
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATA LAYER
# ═══════════════════════════════════════════════════════════════════════════════
import os

@st.cache_data(show_spinner=False)
def load_careers(mtime: float):
    """Load and parse the JSON career database from information.md."""
    try:
        with open(INFO_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        # Primary: look for ```json block
        match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL | re.IGNORECASE)
        if match:
            json_str = match.group(1)
        else:
            # Fallback: raw array brackets
            start, end = content.find('['), content.rfind(']')
            if start == -1 or end == -1 or end <= start:
                st.error("❌ Could not locate JSON data inside information.md.")
                return []
            json_str = content[start:end + 1]
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        st.error(f"❌ JSON parse error: {e}")
        return []
    except Exception as e:
        st.error(f"❌ File read error: {e}")
        return []


def get_startup_class(potential: str) -> str:
    p = potential.lower()
    if "massive" in p:
        return "startup-massive", "🔥 Massive"
    elif "high" in p:
        return "startup-high", "⚡ High"
    elif "medium" in p:
        return "startup-medium", "📈 Medium"
    return "startup-low", "➡ Low"


def build_career_card(career: dict, idx: int) -> str:
    """Return the full HTML for a single glassmorphic bento career card."""
    name = html.escape(career.get("Career_Name", ""))
    description = career.get("Career_Description", "")
    income = html.escape(career.get("Average_Income", "—"))
    degree = html.escape(career.get("Required_Degree", "—"))
    subjects = html.escape(career.get("Required_Subjects", "—"))
    exams = html.escape(career.get("Required_Exams", "—"))
    startup_potential = career.get("Startup_Potential", "")
    steps = career.get("Pathway_Steps", [])

    # Startup badge
    s_class, s_label = get_startup_class(startup_potential)

    # Description block
    desc_html = ""
    if description:
        desc_html = f'<p class="career-description">{html.escape(description)}</p>'

    # Pathway steps
    steps_html = "".join(
        f'<div class="pathway-step">'
        f'<span class="step-badge">{i + 1}</span>'
        f'<span>{html.escape(step)}</span>'
        f'</div>'
        for i, step in enumerate(steps)
    )

    return f"""
<div class="bento-card">
<div class="bento-accent"></div>
<div class="card-header">
<div style="flex:1;">
<div class="career-name">{name}</div>
</div>
<div class="card-index">CAREER · {str(idx + 1).zfill(2)}</div>
</div>
{desc_html}
<div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.75rem; margin-bottom:1.5rem;">
<div class="income-badge">
<span class="income-dot"></span>
{income}
</div>
<span class="startup-pill {s_class}">🚀 Startup: {s_label}</span>
</div>
<div class="info-grid">
<div class="info-cell">
<span class="info-label">🎓 Required Degree</span>
<span class="info-value">{degree}</span>
</div>
<div class="info-cell">
<span class="info-label">📖 Key Subjects</span>
<span class="info-value">{subjects}</span>
</div>
<div class="info-cell full-width">
<span class="info-label">📝 Required Exams</span>
<span class="info-value">{exams}</span>
</div>
</div>
<div class="pathway-block">
<div class="pathway-title">🚀 Your Pathway to Success</div>
<div class="pathway-steps">{steps_html}</div>
</div>
</div>
"""


# ═══════════════════════════════════════════════════════════════════════════════
# EXAM DATA LAYER
# ═══════════════════════════════════════════════════════════════════════════════
_EXAM_FALLBACK = [
    {
        "Exam_Name": "JEE Advanced",
        "Target_Fields": ["Engineering", "Technology", "Sciences"],
        "Eligibility": "Top 2,50,000 candidates from JEE Main (CRL). Must be in top 20 percentile of respective board. Maximum 2 attempts in consecutive years.",
        "Crucial_Dates": "Registration: January–February | Admit Card: April | Exam: May (Paper 1 & 2) | Results: June",
        "Preparation_Roadmap": [
            "Master NCERT Physics, Chemistry, Math (Class 11 & 12) as the absolute foundation.",
            "Solve 10 years of JEE Advanced Previous Year Papers to understand pattern and difficulty.",
            "Focus on Calculus, Organic Chemistry mechanisms, and Electrostatics — highest-weightage topics.",
            "Take full-length timed mock tests every week in the final 3 months.",
            "Analyse each mock in depth: identify weak chapters and repeat targeted practice."
        ],
        "Official_Link": "https://jeeadv.ac.in"
    },
    {
        "Exam_Name": "CUET UG",
        "Target_Fields": ["Arts & Humanities", "Commerce", "Sciences", "Social Sciences"],
        "Eligibility": "Candidates who have passed or are appearing in Class 12 from any recognised board. No minimum percentage requirement by NTA (university-specific cut-offs apply).",
        "Crucial_Dates": "Registration: February–March | City Intimation: April | Exam: May–June (CBT mode) | Results: July",
        "Preparation_Roadmap": [
            "Choose your Domain Subjects wisely — they must align with the courses you are applying for.",
            "Focus on Class 12 NCERT syllabus — CUET is 80% NCERT-based across all domains.",
            "Practice the General Test section (Critical Reasoning, Quantitative Aptitude, General Knowledge).",
            "Attempt official NTA CUET mock tests on the official portal for interface familiarity.",
            "Prioritise speed and accuracy — each section is strictly time-bounded."
        ],
        "Official_Link": "https://cuet.samarth.ac.in"
    },
    {
        "Exam_Name": "NEET UG",
        "Target_Fields": ["Medicine", "Dental", "Nursing", "Pharmacy", "Veterinary"],
        "Eligibility": "Passed Class 12 with PCB (Physics, Chemistry, Biology) minimum 50% marks (40% for SC/ST/OBC). Age minimum 17 years.",
        "Crucial_Dates": "Registration: December–January | Exam: May (Single Day, Offline) | Results: June",
        "Preparation_Roadmap": [
            "Complete all NCERT Biology chapters (Class 11 & 12) — carries 50% of total marks.",
            "Master Organic Chemistry reaction mechanisms and Physical Chemistry numericals.",
            "Solve minimum 5,000 NEET-standard MCQs before the exam.",
            "Attempt at least 20 full-length mock tests under exam-day conditions.",
            "Revise Human Physiology, Genetics, and Ecology weekly for consistent Biology scoring."
        ],
        "Official_Link": "https://neet.ntaonline.in"
    },
    {
        "Exam_Name": "CLAT",
        "Target_Fields": ["Law", "Legal Services", "Judiciary", "Corporate Law"],
        "Eligibility": "Passed or appearing in Class 12 from any recognised board. Minimum 45% marks (40% for SC/ST). Age limit: No upper age limit.",
        "Crucial_Dates": "Registration: July–November | Exam: December (Offline) | Results: January",
        "Preparation_Roadmap": [
            "Master Comprehension-based English — CLAT is entirely passage-based.",
            "Build Current Affairs habit: read newspapers daily for 6 months before exam.",
            "Practice Legal Reasoning with past CLAT papers to understand passage structure.",
            "Strengthen Quantitative Techniques: data interpretation and basic math up to Class 10.",
            "Attempt 3 full-length mock tests per week in the final 2 months."
        ],
        "Official_Link": "https://consortiumofnlus.ac.in"
    },
    {
        "Exam_Name": "UPSC CSE",
        "Target_Fields": ["Civil Services", "Government Administration", "Foreign Services", "Police"],
        "Eligibility": "Bachelor's degree in any discipline from a recognised university. Age: 21–32 years (relaxation for SC/ST/OBC). Maximum 6 attempts (General).",
        "Crucial_Dates": "Notification: February | Prelims: May–June | Mains: September | Interview: March–April (following year)",
        "Preparation_Roadmap": [
            "Build a 2-year preparation plan covering all GS papers and optional subject simultaneously.",
            "Read NCERT books (Class 6–12) for History, Geography, Polity, Economy as the base layer.",
            "Follow reliable current affairs sources daily — The Hindu, PIB, and Yojana magazine.",
            "Write 5 UPSC-standard answers per day to build Mains answer writing speed.",
            "Attempt 2 full UPSC Prelims mock tests per week in the final 3 months."
        ],
        "Official_Link": "https://upsc.gov.in"
    },
    {
        "Exam_Name": "CAT",
        "Target_Fields": ["Management", "MBA", "Business Administration", "Finance", "HR"],
        "Eligibility": "Bachelor's degree in any discipline with minimum 50% marks (45% for SC/ST/PwD). Final-year students also eligible.",
        "Crucial_Dates": "Registration: August–September | Exam: November (CBT, 3 slots) | Results: January",
        "Preparation_Roadmap": [
            "Focus on Verbal Ability & Reading Comprehension — practice RC passages daily.",
            "Master Data Interpretation sets and Logical Reasoning puzzles for the DILR section.",
            "Practice Quantitative Aptitude with focus on Arithmetic, Algebra, and Geometry.",
            "Attempt sectional mocks for first 4 months, then full-length CAT mocks thereafter.",
            "Analyse accuracy vs. speed tradeoff in each section to optimize your attempt strategy."
        ],
        "Official_Link": "https://iimcat.ac.in"
    },
    {
        "Exam_Name": "GATE",
        "Target_Fields": ["Engineering", "Sciences", "Research", "PSU Jobs", "M.Tech Admissions"],
        "Eligibility": "B.E./B.Tech/B.Sc. (Research)/B.S. in relevant discipline OR in final year. No age limit.",
        "Crucial_Dates": "Registration: August–September | Exam: February (2 weeks, CBT) | Results: March",
        "Preparation_Roadmap": [
            "Download the official GATE syllabus for your paper and create a topic-by-topic study plan.",
            "Dedicate 60% of preparation to subject-specific core topics and 40% to General Aptitude.",
            "Solve GATE PYQs from last 15 years — pattern remains highly consistent.",
            "Practice numerical answer type (NAT) questions which require precision without MCQ guessing.",
            "Take 2 full-length GATE mock tests per week during the final month."
        ],
        "Official_Link": "https://gate2025.iitr.ac.in"
    },
    {
        "Exam_Name": "NDA",
        "Target_Fields": ["Defence", "Armed Forces", "Military Technology", "Naval Science"],
        "Eligibility": "Unmarried male candidates (and female for select entries). Age: 16.5–19.5 years. Class 12 pass/appearing with PCM (for Army/Navy/Air Force technical entries).",
        "Crucial_Dates": "Notification: January & June (twice annually) | Exam: April & September | SSB Interview: 3–6 months post results",
        "Preparation_Roadmap": [
            "Master Mathematics (Algebra, Trigonometry, Calculus, Statistics) — it carries 300 marks.",
            "Build English and General Knowledge simultaneously for the GAT paper (600 marks).",
            "Start physical fitness training in parallel: running, push-ups, swimming for SSB.",
            "Attempt full NDA mock papers under strict time conditions every weekend.",
            "Read current affairs, Indian history, geography, and science daily for GAT preparation."
        ],
        "Official_Link": "https://upsc.gov.in/examinations/active-examinations/nda"
    },
    {
        "Exam_Name": "NATA",
        "Target_Fields": ["Architecture", "Design", "Urban Planning", "Interior Design"],
        "Eligibility": "Passed Class 12 with Mathematics as a subject. Minimum 50% aggregate marks in PCM. No age limit.",
        "Crucial_Dates": "Registration: January–April | Exam: April–May (2 attempts offered) | Results: June",
        "Preparation_Roadmap": [
            "Develop strong freehand sketching skills — architectural drawing is a core section.",
            "Study aesthetic sensitivity: perspective drawing, shadowing, and building materials.",
            "Practice PCM concepts (Physics and Maths) for the analytical portion of the test.",
            "Study famous architectural works globally and in India for visual observation questions.",
            "Attempt NATA past papers and take official CoA mock tests to calibrate performance."
        ],
        "Official_Link": "https://nata.in"
    },
    {
        "Exam_Name": "UGC NET",
        "Target_Fields": ["University Teaching", "Research", "JRF Fellowships", "Academia"],
        "Eligibility": "Master's degree (55% marks, 50% for SC/ST/PwD) in relevant subject. No age limit for Assistant Professor; JRF: max 30 years (relaxation for reserved).",
        "Crucial_Dates": "Registration: March–April (Cycle 1) & August–September (Cycle 2) | Exam: June & December | Results: 1 month post-exam",
        "Preparation_Roadmap": [
            "Paper 1 (Teaching Aptitude, Research Methodology) is common for all subjects — master it first.",
            "Study the complete NTA syllabus for your Paper 2 subject domain thoroughly.",
            "Solve minimum 10 years of UGC NET PYQs for both Paper 1 and Paper 2.",
            "Focus on Research Methodology, Logical Reasoning, and Data Interpretation for Paper 1.",
            "Take subject-specific NET mock tests 3 months before the exam date."
        ],
        "Official_Link": "https://ugcnet.nta.ac.in"
    }
]


@st.cache_data(show_spinner=False)
def load_exams(mtime: float):
    """Load exam data from information2.md. Falls back to built-in sample data if empty/missing."""
    try:
        with open(INFO2_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if not content:
            return _EXAM_FALLBACK
        match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL | re.IGNORECASE)
        if match:
            json_str = match.group(1)
        else:
            start, end = content.find('['), content.rfind(']')
            if start == -1 or end == -1 or end <= start:
                return _EXAM_FALLBACK
            json_str = content[start:end + 1]
        data = json.loads(json_str)
        return data if data else _EXAM_FALLBACK
    except Exception:
        return _EXAM_FALLBACK


# ═══════════════════════════════════════════════════════════════════════════════
# PATHWAY FLOWCHART DIALOG
# ═══════════════════════════════════════════════════════════════════════════════
@st.dialog("🗺️ Career Pathway Flowchart", width="large")
def show_pathway_dialog(career: dict):
    """Render a vertical chronological timeline for a single career's full pathway."""
    name   = career.get("Career_Name", "")
    degree = career.get("Required_Degree", "—")
    exams  = career.get("Required_Exams", "—")
    steps  = career.get("Pathway_Steps", [])
    income = career.get("Average_Income", "—")
    s_class, s_label = get_startup_class(career.get("Startup_Potential", ""))

    # Colour cycle for timeline dots
    dot_classes = ["tl-dot-blue", "tl-dot-purple", "tl-dot-cyan", "tl-dot-green"]
    label_colours = ["color:#93c5fd", "color:#c4b5fd", "color:#67e8f9", "color:#34d399"]

    # --- Build step nodes ---
    step_nodes_html = ""
    for idx, step in enumerate(steps):
        dot_cls   = dot_classes[idx % len(dot_classes)]
        lbl_style = label_colours[idx % len(label_colours)]
        step_nodes_html += f"""
<div class="tl-node">
  <div class="tl-dot {dot_cls}">{idx + 1}</div>
  <div class="tl-label" style="{lbl_style}">Step {idx + 1}</div>
  <div class="tl-content">{html.escape(step)}</div>
</div>"""

    # Exam tag pills
    exam_tags_html = ""
    exam_tag_classes = ["tl-tag-blue", "tl-tag-purple", "tl-tag-blue", "tl-tag-purple"]
    for ei, exam in enumerate(exams.split(",")):
        cls = exam_tag_classes[ei % len(exam_tag_classes)]
        exam_tags_html += f'<span class="tl-tag {cls}">{html.escape(exam.strip())}</span>'

    timeline_html = f"""
<div class="timeline-wrap">
  <div class="timeline-header">{html.escape(name)}</div>
  <div class="timeline-sub">A step-by-step chronological roadmap to reach this career from your current academic stage.</div>
  <div class="timeline-track">
    <div class="tl-node">
      <div class="tl-dot tl-dot-blue">📝</div>
      <div class="tl-label" style="color:#93c5fd">Required Exams</div>
      <div class="tl-content">{html.escape(exams)}</div>
      <div class="tl-tag-row">{exam_tags_html}</div>
    </div>
    <div class="tl-node">
      <div class="tl-dot tl-dot-purple">🎓</div>
      <div class="tl-label" style="color:#c4b5fd">Required Degree</div>
      <div class="tl-content">{html.escape(degree)}</div>
    </div>
    {step_nodes_html}
    <div class="tl-node" style="border-color:rgba(16,185,129,0.35); background:rgba(16,185,129,0.05);">
      <div class="tl-dot tl-dot-green">✓</div>
      <div class="tl-label" style="color:#34d399">Target Income</div>
      <div class="tl-content">{html.escape(income)}</div>
      <div class="tl-tag-row">
        <span class="tl-tag tl-tag-green">🚀 Startup: {html.escape(s_label)}</span>
      </div>
    </div>
  </div>
</div>"""

    st.markdown(timeline_html, unsafe_allow_html=True)

    # ── Grand Connect: Link to Course Guide ──────────────────────────────
    degree_str = career.get("Required_Degree", "")
    if degree_str and degree_str != "—":
        if st.button(f"🎓 Find Top Colleges for: {degree_str}", key=f"link_cg_{career.get('Career_Name','').replace(' ','_')}"):
            st.session_state.search_query = ""
            if "cg_search" in st.session_state:
                st.session_state["cg_search"] = ""
            st.session_state.scroll_to_cg_search = True
            st.session_state.current_page = "Course Guide"
            st.rerun()





# ═══════════════════════════════════════════════════════════════════════════════
# AUTH MODAL DIALOG
# ═══════════════════════════════════════════════════════════════════════════════
@st.dialog("🚀 Welcome to PathForge", width="small")
def show_login_modal():
    """Password-gated auth modal with Register / Login modes."""
    mode = st.session_state.auth_mode

    # ── Header ──────────────────────────────────────────────────
    hero_sub = (
        "Create your account to access Career Details." if mode == "signup"
        else "Sign in to access your personalised dashboard."
    )
    st.markdown(f"""
    <div class="login-glass-wrap">
        <div class="login-logo-badge">✶ Career Intelligence Platform</div>
        <div class="login-title">{'Create Account' if mode == 'signup' else 'Sign In'}</div>
        <div class="login-sub">{hero_sub}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Mode Toggle Tabs ──────────────────────────────────────────
    tab_login, tab_signup = st.tabs(["  🔑  Sign In  ", "  📝  Register  "])

    # ================================================================
    # SIGN IN TAB
    # ================================================================
    with tab_login:
        li_user = st.text_input(
            "Username",
            placeholder="Your username",
            key="_li_username",
        )
        li_pass = st.text_input(
            "Password",
            placeholder="Your password",
            type="password",
            key="_li_password",
        )
        if st.button(
            "⚡ Sign In to PathForge",
            key="_li_submit",
            use_container_width=True,
            type="primary",
        ):
            uname = li_user.strip()
            upass = li_pass.strip()
            if not uname or not upass:
                st.warning("👤 Please fill in both fields.")
            else:
                try:
                    conn = init_db_connection()
                    response = conn.table("users").select("*").eq("username", uname).eq("password", upass).execute()
                    if not response.data:
                        st.error("❌ Invalid username or password. Please try again.")
                    else:
                        user = response.data[0]
                        st.session_state.logged_in = True
                        st.session_state.username  = user["username"]
                        st.session_state.user_id   = user["id"]
                        st.session_state.auth_mode = "login"
                        st.toast(f"✅ Welcome back {uname}!", icon="👋")
                        if st.session_state.get("pending_career"):
                            st.session_state.selected_career     = st.session_state.pending_career
                            st.session_state.show_career_sidebar = True
                            st.session_state.pending_career      = None
                        if st.session_state.get("pending_forge_open"):
                            st.session_state.forge_open = True
                            if st.session_state.get("selected_career"):
                                st.session_state.show_career_sidebar = True
                            st.session_state.pending_forge_open = False
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Database error: {e}")

    # ================================================================
    # REGISTER TAB
    # ================================================================
    with tab_signup:
        su_user = st.text_input(
            "Choose a Username",
            placeholder="e.g. arjun_sharma",
            key="_su_username",
        )
        su_pass = st.text_input(
            "Choose a Password",
            placeholder="Min 6 characters",
            type="password",
            key="_su_password",
        )
        su_pass2 = st.text_input(
            "Confirm Password",
            placeholder="Repeat your password",
            type="password",
            key="_su_password2",
        )
        if st.button(
            "✨ Create My Account",
            key="_su_submit",
            use_container_width=True,
            type="primary",
        ):
            uname = su_user.strip()
            upass = su_pass.strip()
            upass2 = su_pass2.strip()
            if not uname or not upass:
                st.warning("👤 Please fill in all fields.")
            elif len(upass) < 6:
                st.warning("🔒 Password must be at least 6 characters.")
            elif upass != upass2:
                st.error("❌ Passwords do not match.")
            else:
                try:
                    conn = init_db_connection()
                    check = conn.table("users").select("*").eq("username", uname).execute()
                    if check.data:
                        st.error(f"❌ Username **{uname}** is already taken. Try another.")
                    else:
                        import uuid
                        user_id = str(uuid.uuid4())
                        conn.table("users").insert({
                            "id": user_id,
                            "username": uname,
                            "password": upass
                        }).execute()
                        st.session_state.logged_in = True
                        st.session_state.username  = uname
                        st.session_state.user_id   = user_id
                        st.session_state.auth_mode = "login"
                        st.toast(f"✅ Welcome {uname}! Account created.", icon="🚀")
                        if st.session_state.get("pending_career"):
                            st.session_state.selected_career     = st.session_state.pending_career
                            st.session_state.show_career_sidebar = True
                            st.session_state.pending_career      = None
                        if st.session_state.get("pending_forge_open"):
                            st.session_state.forge_open = True
                            if st.session_state.get("selected_career"):
                                st.session_state.show_career_sidebar = True
                            st.session_state.pending_forge_open = False
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Database error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# APP RENDER
# ═══════════════════════════════════════════════════════════════════════════════
# Inject CSS
st.markdown(MASTER_CSS, unsafe_allow_html=True)

# ── FORGE HUD — Blackhole Cosmic CSS (always-global, never gated) ──
st.markdown("""
<style>
/* 1. The Animated Cosmic "Blackhole" Sidebar Background */
[data-testid="stSidebar"] {
    z-index: 999999 !important;
    background: radial-gradient(circle at 50% 150%, #1a0b2e 0%, #09090e 50%, #050508 100%) !important;
    border-right: 1px solid rgba(192, 132, 252, 0.2) !important;
    box-shadow: inset -10px 0 50px rgba(0,0,0,0.9) !important;
    overflow: hidden !important;
    min-width: 340px !important;
    max-width: 400px !important;
    width: 360px !important;
    position: relative !important;
}
/* Pulsing nebula effect */
[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle at center, rgba(34, 211, 238, 0.05) 0%, transparent 40%);
    animation: pulse-hole 8s infinite alternate ease-in-out;
    pointer-events: none;
    z-index: 0;
}
@keyframes pulse-hole {
    0%   { transform: scale(0.8) rotate(0deg);  opacity: 0.5; }
    100% { transform: scale(1.2) rotate(15deg); opacity: 1;   }
}
/* Bottom luminous purple edge */
[data-testid="stSidebar"]::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(to right, transparent, rgba(192,132,252,0.55), transparent);
    box-shadow: 0 0 15px rgba(192,132,252,0.5);
    z-index: 100;
    pointer-events: none;
}
/* Push native widgets above the background */
[data-testid="stSidebar"] > div:first-child {
    z-index: 10 !important;
    background: transparent !important;
    position: relative !important;
}
[data-testid="stSidebarContent"] {
    padding: 1.25rem 1.1rem 2rem !important;
    background: transparent !important;
    position: relative !important;
    z-index: 10 !important;
}
[data-testid="stSidebarCollapseButton"] { display: none !important; }

/* Slim 4px scrollbar */
[data-testid="stSidebarContent"]::-webkit-scrollbar { width: 4px !important; }
[data-testid="stSidebarContent"]::-webkit-scrollbar-track { background: transparent !important; }
[data-testid="stSidebarContent"]::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.10) !important;
    border-radius: 4px !important;
}
[data-testid="stSidebarContent"]::-webkit-scrollbar-thumb:hover {
    background: rgba(192,132,252,0.50) !important;
}

/* 2. Primary Save to Forge Button — orange/red gradient */
[data-testid="stSidebar"] .stButton button[kind="primary"],
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #f97316 0%, #dc2626 100%) !important;
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    letter-spacing: 0.05em !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    padding: 0.9rem 1.5rem !important;
    box-shadow: 0 0 20px rgba(249,115,22,0.5) !important;
    transition: all 0.3s ease !important;
    animation: sb-glow-pulse 3s infinite alternate !important;
}
[data-testid="stSidebar"] .stButton button[kind="primary"]:hover,
[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    box-shadow: 0 0 40px rgba(249,115,22,0.8) !important;
    transform: translateY(-2px) !important;
    animation: none !important;
}
[data-testid="stSidebar"] .stButton button[kind="primary"] p { color: #ffffff !important; }

/* Secondary buttons */
[data-testid="stSidebar"] .stButton button[kind="secondary"],
[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
    background: rgba(255,255,255,0.04) !important;
    color: #cfc2d6 !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 8px !important;
    font-size: 0.78rem !important;
    box-shadow: none !important;
    animation: none !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] .stButton button[kind="secondary"]:hover,
[data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover {
    color: #e4e1e9 !important;
    border-color: rgba(192,132,252,0.40) !important;
    background: rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] .stButton button[kind="secondary"] p { color: inherit !important; }
/* Suppress global animated border on ALL sidebar buttons */
[data-testid="stSidebar"] .stButton button::before,
[data-testid="stSidebar"] .stButton button::after { display: none !important; }

/* 3. Dark terminal Selectbox */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div,
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: rgba(10, 10, 15, 0.8) !important;
    border: 1px solid rgba(192, 132, 252, 0.3) !important;
    color: #e4e1e9 !important;
    border-radius: 8px !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div:hover,
[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
    border-color: #22D3EE !important;
    box-shadow: 0 0 10px rgba(34,211,238,0.2) !important;
}
[data-testid="stSidebar"] .stSelectbox label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.60rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.20em !important;
    text-transform: uppercase !important;
    color: #64748b !important;
}

/* 4. Dark terminal Textarea */
[data-testid="stSidebar"] .stTextArea textarea {
    background-color: rgba(10, 10, 15, 0.8) !important;
    border: 1px solid rgba(192, 132, 252, 0.3) !important;
    color: #e4e1e9 !important;
    border-radius: 8px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    line-height: 1.70 !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}
[data-testid="stSidebar"] .stTextArea textarea:focus {
    border-color: #C084FC !important;
    box-shadow: 0 0 15px rgba(192,132,252,0.4) !important;
    outline: none !important;
}
[data-testid="stSidebar"] .stTextArea textarea::placeholder {
    color: rgba(207,194,214,0.4) !important;
}

/* 5. Tabs — neon purple */
[data-testid="stSidebar"] .stTabs [data-baseweb="tab-list"] {
    background-color: rgba(255,255,255,0.02) !important;
    border-bottom: 1px solid rgba(192,132,252,0.20) !important;
    border-radius: 8px 8px 0 0 !important;
}
[data-testid="stSidebar"] .stTabs [data-baseweb="tab"] {
    color: #cfc2d6 !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    font-family: 'Hanken Grotesk', sans-serif !important;
    font-size: 0.78rem !important;
    flex: 1 !important;
    transition: all 0.3s ease !important;
}
[data-testid="stSidebar"] .stTabs [aria-selected="true"] {
    color: #C084FC !important;
    border-bottom-color: #C084FC !important;
    text-shadow: 0 0 10px rgba(192,132,252,0.8) !important;
}

/* 6. Keyframe animations */
@keyframes sb-glow-pulse {
    0%   { box-shadow: 0 0 20px rgba(249,115,22,0.40), 0 0 60px rgba(245,158,11,0.28); }
    100% { box-shadow: 0 0 40px rgba(249,115,22,0.80), 0 0 90px rgba(245,158,11,0.50); }
}
</style>
""", unsafe_allow_html=True)

# ── WebGL Cyber-Terrain Background ──────────────────────────────────────────
# Uses st.components.v1.html() which creates a sandboxed iframe with scripts
# allowed. The JS escapes the iframe to inject the canvas + Three.js directly
# into the parent Streamlit document body — the only reliable approach.
WEBGL_IFRAME_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  html, body { margin: 0; padding: 0; background: transparent; overflow: hidden; }
</style>
</head>
<body>
<script>
(function() {
  var pDoc, pWin;
  try {
    pDoc = window.parent.document;
    pWin = window.parent;
  } catch(e) { return; } // cross-origin guard

  // ── Remove any stale canvas from prior hot-reloads ──────────────────
  var old = pDoc.getElementById('pf-gl-canvas');
  if (old) old.remove();
  var oldScript = pDoc.getElementById('pf-three-script');
  if (oldScript) oldScript.remove();

  // ── Inject canvas style into parent <head> ──────────────────────────
  var styleEl = pDoc.getElementById('pf-gl-style');
  if (!styleEl) {
    styleEl = pDoc.createElement('style');
    styleEl.id = 'pf-gl-style';
    styleEl.textContent = [
      '#pf-gl-canvas {',
      '  position: fixed !important;',
      '  top: 0 !important; left: 0 !important;',
      '  width: 100vw !important; height: 100vh !important;',
      '  pointer-events: none !important;',
      '  z-index: 0 !important;',
      '  display: block !important;',
      '}'
    ].join('');
    pDoc.head.appendChild(styleEl);
  }

  // ── Create canvas in parent body (before all other children) ────────
  var canvas = pDoc.createElement('canvas');
  canvas.id = 'pf-gl-canvas';
  pDoc.body.insertBefore(canvas, pDoc.body.firstChild);

  // ── Load Three.js r128 into parent document ─────────────────────────
  var three = pDoc.createElement('script');
  three.id  = 'pf-three-script';
  three.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
  three.crossOrigin = 'anonymous';
  three.onload = function() { bootTerrain(canvas, pDoc, pWin); };
  pDoc.head.appendChild(three);

  // ════════════════════════════════════════════════════════════════════
  function bootTerrain(canvas, doc, win) {
    var THREE = win.THREE;
    if (!THREE) return;

    // ── Renderer ──────────────────────────────────────────────────────
    var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(win.devicePixelRatio, 1.5));
    renderer.setSize(win.innerWidth, win.innerHeight);
    renderer.setClearColor(0x03040a, 1);

    // ── Scene & Camera ─────────────────────────────────────────────────
    var scene  = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(55, win.innerWidth / win.innerHeight, 0.1, 2000);
    camera.position.set(0, 24, 85);
    camera.lookAt(0, 0, 0);
    scene.fog = new THREE.FogExp2(0x03040a, 0.009);

    // ── Helper: build terrain mesh from layered sine waves ─────────────
    function buildTerrain(color, opacity, yOffset) {
      var W = 130, SEG = 90;
      var geo = new THREE.PlaneGeometry(W, W, SEG, SEG);
      geo.rotateX(-Math.PI / 2);
      var pos = geo.attributes.position;
      var base = new Float32Array(pos.count);
      for (var i = 0; i < pos.count; i++) {
        var x = pos.getX(i), z = pos.getZ(i);
        var y = Math.sin(x*0.18) * Math.cos(z*0.18) * 6.5
              + Math.sin(x*0.35+0.5) * Math.cos(z*0.28) * 4.2
              + Math.sin(x*0.07+1.2) * Math.cos(z*0.09) * 9.5
              + Math.sin(x*0.55+2.1) * Math.sin(z*0.45+1.3) * 2.8
              + Math.cos(x*0.22+0.8) * Math.cos(z*0.32+0.6) * 3.8;
        pos.setY(i, y + yOffset);
        base[i] = y;
      }
      geo.computeVertexNormals();
      var mat = new THREE.MeshBasicMaterial({
        color: color, wireframe: true, transparent: true, opacity: opacity
      });
      return { mesh: new THREE.Mesh(geo, mat), base: base, geo: geo };
    }

    var t1 = buildTerrain(0x6d28d9, 0.32, 0);     // deep violet
    var t2 = buildTerrain(0x06b6d4, 0.12, 0.15);  // neon cyan offset
    scene.add(t1.mesh);
    scene.add(t2.mesh);

    // ── Particle cloud ─────────────────────────────────────────────────
    var ptCount = 2200;
    var ptBuf = new Float32Array(ptCount * 3);
    for (var i = 0; i < ptCount; i++) {
      ptBuf[i*3]   = (Math.random()-0.5)*150;
      ptBuf[i*3+1] = Math.random()*40 - 3;
      ptBuf[i*3+2] = (Math.random()-0.5)*150;
    }
    var ptGeo = new THREE.BufferGeometry();
    ptGeo.setAttribute('position', new THREE.BufferAttribute(ptBuf, 3));
    var particles = new THREE.Points(ptGeo, new THREE.PointsMaterial({
      color: 0xc4b5fd, size: 0.32, transparent: true, opacity: 0.70
    }));
    scene.add(particles);

    // ── Horizon glow ───────────────────────────────────────────────────
    var glowMesh = new THREE.Mesh(
      new THREE.PlaneGeometry(220, 45),
      new THREE.MeshBasicMaterial({ color:0x4c1d95, transparent:true, opacity:0.14, side:THREE.DoubleSide })
    );
    glowMesh.position.set(0, -4, -58);
    scene.add(glowMesh);

    // ── Input state ────────────────────────────────────────────────────
    var panX=0, panY=0, tPanX=0, tPanY=0;
    var scrollZ=0, tScrollZ=0;

    doc.addEventListener('mousemove', function(e) {
      var mx = (e.clientX / win.innerWidth)  * 2 - 1;
      var my = (e.clientY / win.innerHeight) * 2 - 1;
      tPanX =  mx * 7;
      tPanY = -my * 3;
    });

    function onScroll(e) {
      var el = e.target;
      var top = (el === win) ? win.scrollY
              : (typeof el.scrollTop === 'number' ? el.scrollTop : 0);
      tScrollZ = top / 180;
    }
    win.addEventListener('scroll', onScroll, true);
    doc.addEventListener('scroll', onScroll, true);

    win.addEventListener('resize', function() {
      camera.aspect = win.innerWidth / win.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(win.innerWidth, win.innerHeight);
    });

    // ── Animate ────────────────────────────────────────────────────────
    var clock = new THREE.Clock();
    (function loop() {
      requestAnimationFrame(loop);
      var t = clock.getElapsedTime();

      panX  += (tPanX  - panX)  * 0.04;
      panY  += (tPanY  - panY)  * 0.04;
      scrollZ += (tScrollZ - scrollZ) * 0.05;

      camera.position.x = panX;
      camera.position.y = 24 + panY;
      camera.position.z = 85 - scrollZ * 6;
      camera.lookAt(panX * 0.25, 0, 0);

      // Ripple both terrain meshes
      [t1, t2].forEach(function(obj, idx) {
        var p = obj.geo.attributes.position;
        var off = idx * 0.12;
        for (var i = 0; i < p.count; i++) {
          var x = p.getX(i), z = p.getZ(i);
          var wave = Math.sin(t*0.42 + x*0.26 + z*0.16 + off) * 0.60
                   + Math.sin(t*0.71 + x*0.13 - z*0.21 + off) * 0.38;
          p.setY(i, obj.base[i] + wave + (idx * 0.15));
        }
        p.needsUpdate = true;
      });

      particles.rotation.y = t * 0.013;
      particles.position.y = Math.sin(t * 0.19) * 0.6;

      renderer.render(scene, camera);
    })();
  }
})();
</script>
</body>
</html>
"""
# ── Sidebar WebGL Shader Background ─────────────────────────────────────────
SIDEBAR_WEBGL_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  html, body { margin: 0; padding: 0; background: transparent; overflow: hidden; }
</style>
</head>
<body>
<script>
(function() {
  var pDoc, pWin;
  try {
    pDoc = window.parent.document;
    pWin = window.parent;
  } catch(e) { return; } // cross-origin guard

  var old = pDoc.getElementById('pf-sidebar-gl');
  if (old) old.remove();

  var styleEl = pDoc.getElementById('pf-sidebar-style');
  if (!styleEl) {
    styleEl = pDoc.createElement('style');
    styleEl.id = 'pf-sidebar-style';
    styleEl.textContent = [
      '#pf-sidebar-gl {',
      '  position: absolute !important;',
      '  top: 0 !important; left: 0 !important;',
      '  width: 100% !important; height: 100% !important;',
      '  pointer-events: none !important;',
      '  z-index: 0 !important;', 
      '  mix-blend-mode: screen;',
      '}'
    ].join('');
    pDoc.head.appendChild(styleEl);
  }

  var canvas = pDoc.createElement('canvas');
  canvas.id = 'pf-sidebar-gl';
  
  setTimeout(() => {
     var target = pDoc.querySelector('[data-testid="stSidebar"]');
     if(target) target.insertBefore(canvas, target.firstChild);
  }, 500);

  var three = pDoc.createElement('script');
  three.id  = 'pf-three-sidebar';
  three.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
  three.crossOrigin = 'anonymous';
  three.onload = function() { bootSidebarShader(canvas, pDoc, pWin); };
  if (!pDoc.getElementById('pf-three-sidebar')) {
      pDoc.head.appendChild(three);
  } else {
      setTimeout(() => bootSidebarShader(canvas, pDoc, pWin), 600);
  }

  function bootSidebarShader(canvas, doc, win) {
      if (!win.THREE) return;
      var THREE = win.THREE;
      var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: false, alpha: true });
      renderer.setPixelRatio(Math.min(win.devicePixelRatio, 1.5));
      
      var uniforms = {
          u_time: { value: 0.0 },
          u_resolution: { value: new THREE.Vector2(360, 850) },
          u_mouse: { value: new THREE.Vector2(180, 425) }
      };

      function resize() {
          var rect = canvas.parentElement ? canvas.parentElement.getBoundingClientRect() : {width: 360, height: 850};
          renderer.setSize(rect.width, rect.height);
          uniforms.u_resolution.value.set(rect.width, rect.height);
      }
      
      var scene = new THREE.Scene();
      var camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
      
      var material = new THREE.ShaderMaterial({
          vertexShader: `
            varying vec2 v_texCoord;
            void main() {
                v_texCoord = uv;
                gl_Position = vec4(position, 1.0);
            }
          `,
          fragmentShader: `
            uniform float u_time;
            uniform vec2 u_resolution;
            uniform vec2 u_mouse;
            varying vec2 v_texCoord;

            void main() {
                vec2 st = gl_FragCoord.xy / u_resolution.xy;
                vec2 mouse = u_mouse.xy / u_resolution.xy;
                float dist = distance(st, mouse);
                float glow = 0.05 / max(dist, 0.01);
                
                vec3 color = vec3(0.02, 0.02, 0.05); 
                color += vec3(0.4, 0.1, 0.8) * sin(u_time * 0.5 + st.y * 10.0) * 0.15; 
                color += vec3(0.1, 0.8, 1.0) * glow * 0.4; 
                
                gl_FragColor = vec4(color, 1.0);
            }
          `,
          uniforms: uniforms,
          transparent: true,
          blending: THREE.AdditiveBlending
      });
      
      var mesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
      scene.add(mesh);
      
      resize();
      win.addEventListener('resize', resize);
      doc.addEventListener('mousemove', function(e) {
          if (!canvas.parentElement) return;
          var rect = canvas.parentElement.getBoundingClientRect();
          var x = e.clientX - rect.left;
          var y = e.clientY - rect.top;
          uniforms.u_mouse.value.set(x, rect.height - y);
      });

      var clock = new THREE.Clock();
      function animate() {
          requestAnimationFrame(animate);
          uniforms.u_time.value = clock.getElapsedTime();
          renderer.render(scene, camera);
      }
      animate();
  }
})();
</script>
</body>
</html>
"""

# Inject WebGL background via components.html (iframe with scripts enabled)
# height=0 so it takes no layout space; canvas is injected into parent doc body
components.html(WEBGL_IFRAME_HTML, height=0)

# Load data once (auto-refreshes whenever source files are modified)
db_mtime   = os.path.getmtime(INFO_PATH)  if os.path.exists(INFO_PATH)  else 0.0
exam_mtime = os.path.getmtime(INFO2_PATH) if os.path.exists(INFO2_PATH) else 0.0
all_careers = load_careers(db_mtime)
all_exams   = load_exams(exam_mtime)
total_careers = len(all_careers)
unique_subjects = sorted(set(c["Subject_Interest"] for c in all_careers)) if all_careers else []
unique_styles   = sorted(set(c["Work_Style"]       for c in all_careers)) if all_careers else []

# ── Session State Router ─────────────────────────────────────────────────────
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Career Engine"
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
# ── Auth State ───────────────────────────────────────────────────────────────
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "login"
if 'user_registry' not in st.session_state:
    # Mock in-memory user store: { username: password }.
    # Replace with Supabase queries in the next sprint.
    st.session_state.user_registry = {}
# ── Career Sidebar State ─────────────────────────────────────────────────────
if 'selected_career' not in st.session_state:
    st.session_state.selected_career = None
if 'show_career_sidebar' not in st.session_state:
    st.session_state.show_career_sidebar = False
if 'saved_careers' not in st.session_state:
    st.session_state.saved_careers = []
if 'pending_career' not in st.session_state:
    st.session_state.pending_career = None
# ── Player HUD / Forge State ─────────────────────────────────────────────────
if 'forge_open' not in st.session_state:
    st.session_state.forge_open = False
if 'forge_notes' not in st.session_state:
    st.session_state.forge_notes = ""
if 'forge_memory_selection' not in st.session_state:
    st.session_state.forge_memory_selection = "Currently Exploring"

def change_page(page_name):
    st.session_state.current_page = page_name

current_page = st.session_state.current_page

# ── Navigation Bar ───────────────────────────────────────────────────────────
def render_nav_bar(current_page, unique_key):
    nav_items = [
        ("🚀  Career Engine", "Career Engine"),
        ("📝  Exam Directory", "Exam Directory"),
        ("🎓  Course Guide", "Course Guide"),
    ]
    # 6 columns: 3 nav tabs | spacer | How It Works | Open My Forge
    nav_cols = st.columns([1.5, 1.5, 1.5, 2, 1.5, 1.6])
    
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

    # ── 🛠️ Open My Forge — permanent HUD trigger ────────────────────────────
    with nav_cols[5]:
        st.markdown('<span class="nav-forge-anchor"></span>', unsafe_allow_html=True)
        forge_label = "🔮 Close Forge" if st.session_state.get("forge_open", False) else "🛠️ Open My Forge"
        if st.button(forge_label, key=f"nav_forge_{unique_key}", use_container_width=True):
            if not st.session_state.get("logged_in", False) and not st.session_state.get("forge_open", False):
                st.session_state.pending_forge_open = True
                show_login_modal()
            else:
                st.session_state.forge_open = not st.session_state.get("forge_open", False)
                # Opening the Forge should also show the sidebar if a career is loaded
                if st.session_state.forge_open and st.session_state.get("selected_career"):
                    st.session_state.show_career_sidebar = True
                elif not st.session_state.forge_open:
                    st.session_state.show_career_sidebar = False
                st.rerun()
            
    st.markdown("""
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
    
    div[data-testid="column"]:has(.nav-hiw-anchor) button,
    div[data-testid="column"]:has(.nav-forge-anchor) button {
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
    div[data-testid="column"]:has(.nav-hiw-anchor) button:hover,
    div[data-testid="column"]:has(.nav-forge-anchor) button:hover {
        background: rgba(15, 23, 42, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1) !important;
    }
    /* Forge button gets a distinctive amber/purple glow */
    div[data-testid="column"]:has(.nav-forge-anchor) button {
        background: linear-gradient(135deg, rgba(245,158,11,0.18) 0%, rgba(139,92,246,0.18) 100%) !important;
        border: 1px solid rgba(245,158,11,0.35) !important;
        color: #fcd34d !important;
        box-shadow: 0 0 16px rgba(245,158,11,0.18), inset 0 1px 0 rgba(255,255,255,0.06) !important;
    }
    div[data-testid="column"]:has(.nav-forge-anchor) button:hover {
        background: linear-gradient(135deg, rgba(245,158,11,0.30) 0%, rgba(139,92,246,0.30) 100%) !important;
        border-color: rgba(245,158,11,0.65) !important;
        box-shadow: 0 0 28px rgba(245,158,11,0.35), 0 0 60px rgba(139,92,246,0.20) !important;
    }
    </style>
    <hr style='margin:0.25rem 0 0.5rem 0; border:none; border-top:1px solid rgba(255,255,255,0.08);'>
    """, unsafe_allow_html=True)

# ── Full-Screen Animated Hero Banner ──────────────────────────────────────
HERO_SHADER_HTML = """
<div style="position:relative; width:100%; height:100%; overflow:hidden; background:#03040a;">
    <!-- Shader Canvas Background -->
    <canvas id="pf-shader-canvas" style="position:absolute; inset:0; width:100%; height:100%; opacity:0.6; mix-blend-mode:screen;"></canvas>
    <!-- Dark gradient overlay for text readability -->
    <div style="position:absolute; inset:0; background: linear-gradient(to bottom, rgba(3,4,10,0.8), rgba(3,4,10,0.35), rgba(3,4,10,0.95)); z-index:1;"></div>
    <!-- Hero Content -->
    <div style="position:relative; z-index:10; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; text-align:center; padding:3rem 2rem 0.5rem;">
        <div style="position:absolute; width:520px; height:520px; top:50%; left:50%; transform:translate(-50%,-50%); background:radial-gradient(circle, rgba(208,188,255,0.18) 0%, transparent 70%); border-radius:50%; pointer-events:none; animation: pf-pulse 4s infinite alternate;"></div>
        <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(208,188,255,0.1); border:1px solid rgba(208,188,255,0.25); border-radius:100px; padding:6px 22px; font-family:'Space Grotesk',sans-serif; font-size:0.75rem; font-weight:600; color:#d0bcff; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:1.5rem;">✦ NEXT-GEN CAREER INTELLIGENCE PLATFORM</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:clamp(4.2rem,11vw,8.5rem); font-weight:700; line-height:1.05; letter-spacing:-0.03em; background:linear-gradient(180deg,#ffffff 0%,#d0bcff 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:0 0 1.25rem;">PathForge</h1>
        <p style="font-family:'Inter',sans-serif; font-size:1.3rem; line-height:1.7; color:#e5e2e1; max-width:780px; margin:0 auto 3rem;">The most student oriented platform, to DECIDE and OPERATE one's future!</p>

    </div>
    <!-- Scroll indicator -->
    <div style="position:absolute; bottom:2.5rem; left:50%; transform:translateX(-50%); z-index:10; opacity:0.5; font-size:2rem; color:#cbc3d7; animation: pf-bounce 2s ease-in-out infinite;">&#x25BE;</div>
</div>
<style>
    @keyframes pf-pulse {
        0% { transform: translate(-50%,-50%) scale(1); opacity: 0.5; }
        100% { transform: translate(-50%,-50%) scale(1.2); opacity: 0.8; }
    }
    @keyframes pf-bounce {
        0%, 100% { transform: translateX(-50%) translateY(0); }
        50% { transform: translateX(-50%) translateY(12px); }
    }
</style>
<script>
(function() {
    const canvas = document.getElementById('pf-shader-canvas');
    function syncSize() {
        const w = canvas.clientWidth || 1280;
        const h = canvas.clientHeight || 720;
        if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
    }
    if (typeof ResizeObserver !== 'undefined') { new ResizeObserver(syncSize).observe(canvas); }
    syncSize();
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) return;
    const vs = `attribute vec2 a_position; varying vec2 v_texCoord; void main() { v_texCoord = a_position * 0.5 + 0.5; gl_Position = vec4(a_position, 0.0, 1.0); }`;
    const fs = `precision highp float;
        varying vec2 v_texCoord;
        uniform float u_time;
        uniform vec2 u_resolution;
        float hash(vec2 p) { p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
        float noise(vec2 p) { vec2 i = floor(p); vec2 f = fract(p); f = f * f * (3.0 - 2.0 * f); float a = hash(i); float b = hash(i + vec2(1.0, 0.0)); float c = hash(i + vec2(0.0, 1.0)); float d = hash(i + vec2(1.0, 1.0)); return mix(mix(a, b, f.x), mix(c, d, f.x), f.y); }
        void main() {
            vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / min(u_resolution.x, u_resolution.y);
            float zoom = 1.0 + sin(u_time * 0.2) * 0.5;
            vec2 p = uv * zoom;
            float pattern = 0.0;
            pattern += smoothstep(0.48, 0.5, abs(sin(p.x * 10.0)));
            pattern += smoothstep(0.48, 0.5, abs(sin(p.y * 10.0)));
            float n = noise(p * 5.0 + u_time * 0.1);
            pattern *= 0.3;
            pattern += n * 0.15;
            vec3 black = vec3(0.02, 0.0, 0.05);
            vec3 purple = vec3(0.3, 0.1, 0.6);
            vec3 color = mix(black, purple, pattern + 0.1 * sin(u_time + length(uv)));
            color += 0.05 * purple / length(uv);
            gl_FragColor = vec4(color, 1.0);
        }`;
    function cs(type, src) { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; }
    const prog = gl.createProgram();
    gl.attachShader(prog, cs(gl.VERTEX_SHADER, vs));
    gl.attachShader(prog, cs(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(prog);
    gl.useProgram(prog);
    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, 1,1]), gl.STATIC_DRAW);
    const pos = gl.getAttribLocation(prog, 'a_position');
    gl.enableVertexAttribArray(pos);
    gl.vertexAttribPointer(pos, 2, gl.FLOAT, false, 0, 0);
    const uTime = gl.getUniformLocation(prog, 'u_time');
    const uRes = gl.getUniformLocation(prog, 'u_resolution');
    function render(t) {
        if (typeof ResizeObserver === 'undefined') syncSize();
        gl.viewport(0, 0, canvas.width, canvas.height);
        if (uTime) gl.uniform1f(uTime, t * 0.001);
        if (uRes) gl.uniform2f(uRes, canvas.width, canvas.height);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
        requestAnimationFrame(render);
    }
    render(0);
})();
</script>
"""
components.html(HERO_SHADER_HTML, height=450, scrolling=False)




# ── Auth Gate (Removed - now checked on button click) ─────────────────────────

# ── Player HUD Sidebar — controlled by session state ──
_show_sidebar = st.session_state.get("forge_open", False) or st.session_state.get("show_career_sidebar", False)

if _show_sidebar:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        display: flex !important;
        visibility: visible !important;
        transform: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
with st.sidebar:

    @st.fragment
    def render_sidebar_hud():
        # ── HUD Header ─────────────────────────────────────────────────────────
        st.title("🛠️ My Forge")
        st.caption("PLAYER HUD · CAREER INTELLIGENCE")

        # ── TASK 2: Forge Memory Dropdown ──────────────────────────────────────
        saved_careers_list = []
        if st.session_state.get("logged_in") and st.session_state.get("user_id"):
            try:
                conn = init_db_connection()
                resp = conn.table("saved_careers").select("career_data").eq("user_id", st.session_state.user_id).execute()
                saved_careers_list = [row["career_data"] for row in resp.data]
                st.session_state.saved_careers = saved_careers_list
            except Exception:
                saved_careers_list = st.session_state.get("saved_careers", [])
        else:
            saved_careers_list = st.session_state.get("saved_careers", [])

        saved_labels = [f"{c.get('Career_Name', 'Saved Career')} (Saved)" for c in saved_careers_list]
        forge_memory_options = ["Currently Exploring"] + saved_labels

        if "next_memory_selection" in st.session_state:
            st.session_state.forge_memory_selection = st.session_state.next_memory_selection
            del st.session_state.next_memory_selection

        selected_memory = st.selectbox(
            "Your Forge Memory",
            options=forge_memory_options,
            index=0,
            key="forge_memory_selection",
        )

        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        # ── Derive career_sb based on Dropdown ───────────────────────────────
        career_sb = None
        if selected_memory != "Currently Exploring":
            mem_name = selected_memory.rsplit(" (Saved)", 1)[0]
            for c in saved_careers_list:
                if c.get("Career_Name") == mem_name:
                    career_sb = c
                    break
        else:
            career_sb = st.session_state.get("selected_career") or {}

        # ── TASK 2: Save to Forge Button ──────────────────────────────────────
        sb_name   = career_sb.get("Career_Name", "Career") if career_sb else "Career"
        sb_income = career_sb.get("Average_Income", "—") if career_sb else "—"
        sb_steps  = career_sb.get("Pathway_Steps", []) if career_sb else []
        sb_exams  = career_sb.get("Required_Exams", "") if career_sb else ""
        sb_degree = career_sb.get("Required_Degree", "") if career_sb else ""
        sb_safe   = sb_name.replace(" ", "_").replace("/", "_")

        if st.button(
            "⭐  Save to My Forge",
            key=f"forge_save_{sb_safe}",
            use_container_width=True,
            type="primary",
        ):
            if career_sb:
                if st.session_state.get("logged_in") and st.session_state.get("user_id"):
                    try:
                        conn = init_db_connection()
                        check = conn.table("saved_careers").select("*").eq("user_id", st.session_state.user_id).eq("career_name", sb_name).execute()
                        if check.data:
                            st.toast(f"Already in your Forge: **{sb_name}**", icon="ℹ️")
                        else:
                            conn.table("saved_careers").insert({
                                "user_id": st.session_state.user_id,
                                "career_name": sb_name,
                                "career_data": career_sb
                            }).execute()
                            saved = st.session_state.get("saved_careers", [])
                            saved.append(career_sb)
                            st.session_state.saved_careers = saved
                            st.toast(f"✅ **{sb_name}** saved to your Forge!", icon="⭐")
                            st.session_state.next_memory_selection = f"{sb_name} (Saved)"
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ DB Save Error: {e}")
                else:
                    st.toast("⚠️ Please Sign In to save careers permanently.", icon="🔒")
            else:
                st.toast("Open a Career Details panel first to save!", icon="⚠️")

        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        if not career_sb:
            st.info("Your HUD is empty. Select a saved career from the dropdown, or explore the main database to add one.")
        else:
            # ── TASK 3: 4-Tab Matrix ──────────────────────────────────────────────
            tab_details, tab_exams, tab_courses, tab_notes = st.tabs([
                "Details", "Exams", "Courses", "My Notes"
            ])

            # ================================================================
            # TAB 1 — Details
            # ================================================================
            with tab_details:
                st.markdown(
                    f'<div class="sidebar-career-title">{html.escape(sb_name)}</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(f"""
    <div class="sidebar-income-block">
        <span style="font-size:1.5rem;">💰</span>
        <div>
            <div class="sidebar-income-label">Average Income</div>
            <div class="sidebar-income-value">{html.escape(sb_income)}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
                st.markdown(
                    '<div class="sidebar-section-label">🗺️ Pathway to Success</div>',
                    unsafe_allow_html=True,
                )
                if sb_steps:
                    steps_sb_html = "".join(
                        f'<div class="sidebar-pathway-step">'
                        f'<span class="sidebar-step-badge">{sidx + 1}</span>'
                        f'<span>{html.escape(step)}</span>'
                        f'</div>'
                        for sidx, step in enumerate(sb_steps)
                    )
                    st.markdown(steps_sb_html, unsafe_allow_html=True)
                else:
                    st.markdown('<p style="color:var(--text-secondary);font-size:0.87rem;">No pathway steps available.</p>', unsafe_allow_html=True)

            # ================================================================
            # TAB 2 — Exams
            # ================================================================
            with tab_exams:
                st.markdown('<div class="sidebar-section-label">📝 Required Exams</div>', unsafe_allow_html=True)
                if sb_exams:
                    exam_list = [e.strip() for e in sb_exams.split(",") if e.strip()]
                    for exam in exam_list:
                        st.markdown(
                            f'<div class="sidebar-pathway-step">'
                            f'<span class="sidebar-step-badge">★</span>'
                            f'<span>{html.escape(exam)}</span>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                else:
                    st.markdown('<p style="color:var(--text-secondary);font-size:0.85rem;">No exams listed.</p>', unsafe_allow_html=True)
                st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
                if st.button(
                    "📝  View in Directory",
                    key=f"goto_exam_{sb_safe}",
                    use_container_width=True,
                ):
                    change_page("Exam Directory")
                    st.session_state.show_career_sidebar = False
                    st.session_state.forge_open = False
                    st.rerun()

            # ================================================================
            # TAB 3 — Courses
            # ================================================================
            with tab_courses:
                st.markdown('<div class="sidebar-section-label">🎓 Required Degrees</div>', unsafe_allow_html=True)
                if sb_degree:
                    st.markdown(
                        f'<div class="sidebar-pathway-step">'
                        f'<span class="sidebar-step-badge">★</span>'
                        f'<span>{html.escape(sb_degree)}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown('<p style="color:var(--text-secondary);font-size:0.85rem;">No degrees listed.</p>', unsafe_allow_html=True)
                st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
                if st.button(
                    "🎓  Go to Course Guide",
                    key=f"goto_course_{sb_safe}",
                    use_container_width=True,
                ):
                    change_page("Course Guide")
                    st.session_state.show_career_sidebar = False
                    st.session_state.forge_open = False
                    st.rerun()

            # ================================================================
            # TAB 4 — My Notes
            # ================================================================
            with tab_notes:
                st.markdown('<div class="sidebar-section-label">📓 Personal Notes</div>', unsafe_allow_html=True)

                notes_key = f"notes_{sb_safe}"
                if notes_key not in st.session_state:
                    current_notes = ""
                    if st.session_state.get("logged_in") and st.session_state.get("user_id"):
                        try:
                            conn = init_db_connection()
                            notes_resp = conn.table("career_notes").select("notes").eq("user_id", st.session_state.user_id).eq("career_name", sb_name).execute()
                            if notes_resp.data:
                                current_notes = notes_resp.data[0].get("notes", "")
                        except:
                            pass
                    st.session_state[notes_key] = current_notes

                notes_val = st.text_area(
                    "Personal Notes",
                    placeholder="Jot down your thoughts, goals, exam dates, or personal reflections about this career path...",
                    height=220,
                    label_visibility="collapsed",
                    key=notes_key
                )
                if st.button("💾  Save Notes", key="forge_save_notes", use_container_width=True):
                    if st.session_state.get("logged_in") and st.session_state.get("user_id"):
                        try:
                            conn = init_db_connection()
                            check = conn.table("career_notes").select("*").eq("user_id", st.session_state.user_id).eq("career_name", sb_name).execute()
                            if check.data:
                                conn.table("career_notes").update({"notes": notes_val}).eq("user_id", st.session_state.user_id).eq("career_name", sb_name).execute()
                            else:
                                conn.table("career_notes").insert({
                                    "user_id": st.session_state.user_id,
                                    "career_name": sb_name,
                                    "notes": notes_val
                                }).execute()
                            st.toast("✅ Notes saved to your Forge!", icon="📓")
                        except Exception as e:
                            st.error(f"❌ DB Save Error: {e}")
                    else:
                        st.toast("⚠️ Please Sign In to save notes.", icon="🔒")

        # ── Close Panel — always visible at bottom ──────────────────────────
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        if st.button(
            "✕  Close Forge Panel",
            key=f"sidebar_close_{sb_safe}",
            use_container_width=True,
        ):
            st.session_state.show_career_sidebar = False
            st.session_state.forge_open = False
            st.session_state.selected_career = None
            st.rerun()

    render_sidebar_hud()


render_nav_bar(current_page, "ce")
# ══════════════════════════════════════════════════════════════════════════════
# PAGE: Career Engine
# ══════════════════════════════════════════════════════════════════════════════
if current_page == "Career Engine":


    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)

    # ── "Beyond Engineering" Section (left-aligned, full-width) ──────────────
    st.markdown(f"""
    <div class="hero" style="text-align: left; padding: 0.5rem 0 1.5rem;">
        <div class="hero-eyebrow">
            <div class="hero-dot"></div>
            Career Intelligence Platform &nbsp;·&nbsp; India Edition
        </div>
        <h1 class="hero-title" style="font-size: 2.8rem; line-height: 1.1;">Beyond Engineering:<br>Discover Your True Path</h1>
        <p class="hero-subtitle" style="margin-left: 0; margin-right: 0;">
            Select your academic interest and preferred work style to uncover premium,
            future-proof career paths — curated for India's next-generation innovators.
        </p>
        <div class="hero-stats" style="justify-content: flex-start;">
            <div class="hero-stat">
                <div class="hero-stat-num">{total_careers}+</div>
                <div class="hero-stat-label">Career Paths</div>
            </div>
            <div class="hero-stat-sep"></div>
            <div class="hero-stat">
                <div class="hero-stat-num">{len(unique_subjects)}</div>
                <div class="hero-stat-label">Subject Domains</div>
            </div>
            <div class="hero-stat-sep"></div>
            <div class="hero-stat">
                <div class="hero-stat-num">{len(unique_styles)}</div>
                <div class="hero-stat-label">Work Styles</div>
            </div>
        </div>
    </div>
    <div class="gradient-line"></div>
    """, unsafe_allow_html=True)

    if not all_careers:
        st.error("No career data found. Please ensure `information.md` contains valid JSON.")
        st.stop()

    # ── Input Selection Panel ─────────────────────────────────────────────────
    st.markdown("""
    <div class="selection-section">
        <div class="section-eyebrow">⚙ Configure Your Profile</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display:flex; justify-content:center; margin-bottom: 2rem;">
        <div style="display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg, rgba(139, 92, 246, 0.8) 0%, rgba(56, 189, 248, 0.8) 100%); color:#ffffff; padding:12px 30px; border-radius:100px; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:1rem; letter-spacing:0.05em; text-transform:uppercase; border:1px solid rgba(255,255,255,0.2); box-shadow:0 0 20px rgba(139, 92, 246, 0.3), inset 0 0 10px rgba(56, 189, 248, 0.2); backdrop-filter:blur(8px);">
            🚀 Step 1: Select Your Interests Below
        </div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        selected_subject = st.selectbox(
            "📚  Subject Interest",
            options=["— Choose a domain —"] + unique_subjects,
            help="Select the academic subject you are most passionate about."
        )
    with col2:
        if selected_subject != "— Choose a domain —":
            # Cascading: only show Work Styles that exist for this subject
            filtered_styles = sorted(set(
                c["Work_Style"] for c in all_careers
                if c["Subject_Interest"] == selected_subject
            ))
            selected_style = st.selectbox(
                "💼  Work Style",
                options=["— Choose a style —"] + filtered_styles,
                help="How do you prefer to work day-to-day?"
            )
        else:
            st.info("👈 Select a Subject Interest first to unlock Work Style options.")
            selected_style = "— Choose a style —"

    st.markdown("</div>", unsafe_allow_html=True)  # close selection-section

    # ── Results Engine ─────────────────────────────────────────────────────────
    subject_chosen = selected_subject != "— Choose a domain —"
    style_chosen   = selected_style   != "— Choose a style —"

    if subject_chosen and style_chosen:
        matching = [
            c for c in all_careers
            if c["Subject_Interest"] == selected_subject
            and c["Work_Style"] == selected_style
        ]

        if matching:
            # ── Simulated High-Speed Analysis Loader ─────────────────────────
            with st.status(
                "⚡ Initialising Career Intelligence Matrix...",
                expanded=True
            ) as status:
                st.write("🛰️  Scanning Global High-Yield Opportunity Networks...")
                time.sleep(0.2)
                st.write("🧠  Isolating Non-Traditional Career DNA & Skill Trees...")
                time.sleep(0.2)
                st.write("🔬  Cross-Matching Alternative Degree & Exam Pathways...")
                time.sleep(0.2)
                st.write("⚡  Rendering Interactive 3D Career Matrix...")
                time.sleep(0.2)
                status.update(
                    label="✅ Matrix Successfully Computed!",
                    state="complete",
                    expanded=False
                )

            # Spacer — ensures clean vertical separation between
            # the collapsed status badge and the levitating results banner
            st.markdown('<div style="margin-top:1rem;"></div>', unsafe_allow_html=True)

            # Results banner — rendered independently OUTSIDE st.status
            count = len(matching)
            st.markdown(f"""
            <div class="results-banner">
                <div class="results-left">
                    <div class="results-count">{count}</div>
                    <div class="results-label">
                        High-Paying Path{"s" if count != 1 else ""} Found<br>
                        <strong>{selected_subject}</strong> &nbsp;×&nbsp; <strong>{selected_style}</strong>
                    </div>
                </div>
                <div class="results-tag">✓ Exact Match</div>
            </div>
            """, unsafe_allow_html=True)

            # Render each card
            st.markdown('<div class="bento-grid">', unsafe_allow_html=True)
            for i, career in enumerate(matching):
                # Inject the HTML bento card
                st.markdown(build_career_card(career, i), unsafe_allow_html=True)

                # ── FIX TOGGLE + LATENCY: session_state boolean toggle ──────
                toggle_key = f"show_startup_{i}"
                safe_name  = career['Career_Name'].replace(' ', '_').replace('/', '_')
                btn_key    = f"cta_{i}_{safe_name}"
                fc_key     = f"flowchart_{i}_{safe_name}"

                btn_col, fc_col, exam_col, sidebar_col = st.columns([1, 1, 1, 1], gap="small")
                with btn_col:
                    # Button click flips the toggle — no re-render delay
                    if st.button("💡  View Startup Opportunity", key=btn_key):
                        st.session_state[toggle_key] = not st.session_state.get(toggle_key, False)

                with fc_col:
                    # Pathway flowchart dialog trigger
                    if st.button("🗺️ View Pathway Flowchart", key=f"flowchart_{i}"):
                        show_pathway_dialog(career)

                with exam_col:
                    if st.button("📝 View Exam Details", key=f"exam_details_{i}"):
                        change_page("Exam Directory")
                        st.rerun()

                with sidebar_col:
                    # Open career details in the sidebar panel
                    if st.button("📋 Career Details", key=f"sidebar_{i}"):
                        if not st.session_state.get("logged_in", False):
                            st.session_state.pending_career = career
                            show_login_modal()
                        else:
                            st.session_state.selected_career      = career
                            st.session_state.show_career_sidebar  = True
                            st.session_state.next_memory_selection = "Currently Exploring"
                            st.rerun()

                # Render startup detail panel based on persisted toggle state
                if st.session_state.get(toggle_key, False):
                    startup_text = html.escape(career.get("Startup_Potential", "No data available."))
                    st.markdown(
                        f'<div class="surgical-dark-box"><div class="startup-detail">🚀 <strong>Startup Potential:</strong><br>{startup_text}</div></div>',
                        unsafe_allow_html=True
                    )
            st.markdown("</div>", unsafe_allow_html=True)

        else:
            st.warning(
                "⚡ No careers found for this exact combination. "
                "Try a different Subject or Work Style — the database has many paths!"
            )

    st.markdown("</div>", unsafe_allow_html=True)  # close page-wrapper

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: Exam Directory
# ══════════════════════════════════════════════════════════════════════════════
elif current_page == "Exam Directory":
    # Inject page-specific CSS to style expanders ONLY on this tab
    st.markdown("""
    <style>
    /* Permanent dark background for ALL exam card containers & closed expanders */
    [data-testid="stExpander"], details {
        background: rgba(10, 10, 18, 0.95) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
    }
    /* Permanent dark background for the expanded details pane when opened */
    [data-testid="stExpanderDetails"], details[open] > div {
        background: rgba(8, 8, 14, 0.95) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 0 0 12px 12px !important;
        padding: 16px !important;
    }
    /* Ensure all text inside the Exam Directory expanders is crisp, bright, and readable */
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] h1,
    [data-testid="stExpander"] h2,
    [data-testid="stExpander"] h3,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] a {
        color: #f0f0f5 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)
    # ── Section Header ────────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero" style="padding: 0.5rem 0 1.5rem;">
        <div class="hero-eyebrow">
            <div class="hero-dot"></div>
            Exam Intelligence &nbsp;·&nbsp; India Edition
        </div>
        <div class="exam-section-title">The Exam Directory</div>
        <div class="exam-section-sub">
            Every major Indian entrance exam — eligibility criteria, crucial dates,
            step-by-step preparation roadmaps, and direct links to official portals.
        </div>
    </div>
    <div class="gradient-line"></div>
    """, unsafe_allow_html=True)


    # ── Search & Filter Controls ──────────────────────────────────────────────
    st.markdown("""
    <div class="selection-section">
        <div class="section-eyebrow">🔍 Search & Filter Exams</div>
    """, unsafe_allow_html=True)

    # Extract unique target fields dynamically from loaded exams
    available_fields = sorted(list(set(
        field for ex in all_exams for field in ex.get("Target_Fields", [])
    )))

    search_col, filter_col = st.columns([6, 4], gap="medium")
    with search_col:
        exam_search = st.text_input(
            "🔍 Search Exams (e.g., JEE, CUET, Law)...",
            placeholder="🔍 Search Exams (e.g., JEE, CUET, Law)...",
            label_visibility="collapsed"
        )
    with filter_col:
        selected_fields = st.multiselect(
            "🎯 Filter by Field",
            options=available_fields,
            placeholder="🎯 Filter by Field…",
            label_visibility="collapsed",
            key="exam_filter_widget"
        )

    st.markdown("</div>", unsafe_allow_html=True)  # close selection-section

    # ── Filter Logic ──────────────────────────────────────────────────────────
    filtered_exams = all_exams
    if exam_search.strip():
        q = exam_search.strip().lower()
        filtered_exams = [
            ex for ex in filtered_exams
            if q in ex.get("Exam_Name", "").lower()
            or q in ex.get("Eligibility", "").lower()
            or any(q in tf.lower() for tf in ex.get("Target_Fields", []))
            or any(q in step.lower() for step in ex.get("Preparation_Roadmap", []))
        ]
    if selected_fields:
        filtered_exams = [
            ex for ex in filtered_exams
            if any(
                any(sel.lower() in tf.lower() for tf in ex.get("Target_Fields", []))
                for sel in selected_fields
            )
        ]

    # ── Results Count Badge ───────────────────────────────────────────────────
    total_shown = len(filtered_exams)
    st.markdown(
        f'<div class="exam-count-badge">'
        f'<strong>{total_shown}</strong> exam{"s" if total_shown != 1 else ""} found'
        f'{" · Filtered" if (exam_search or selected_fields) else " · Showing all"}'
        f'</div>',
        unsafe_allow_html=True
    )

    # ── Exam Expanders ────────────────────────────────────────────────────────
    if not filtered_exams:
        st.warning("No exams found matching your criteria.")
    else:
        for ex in filtered_exams:
            exam_name = ex.get("Exam_Name", "Unknown Exam")
            fields    = ex.get("Target_Fields", [])
            eligib    = ex.get("Eligibility", "—")
            dates     = ex.get("Crucial_Dates", "—")
            roadmap   = ex.get("Preparation_Roadmap", [])
            link      = ex.get("Official_Link", "")

            # Field chips for the expander label preview
            field_preview = "  ·  ".join(fields[:3])

            with st.expander(f"📋  {exam_name}   —   {field_preview}"):
                # Field chips
                field_chip_colours = [
                    "exam-chip-blue", "exam-chip-purple",
                    "exam-chip-amber", "exam-chip-green"
                ]
                chips_html = "".join(
                    f'<span class="exam-chip {field_chip_colours[fi % len(field_chip_colours)]}">{html.escape(f)}</span>'
                    for fi, f in enumerate(fields)
                )
                st.markdown(
                    f'<div class="exam-meta-row">{chips_html}</div>',
                    unsafe_allow_html=True
                )

                # Eligibility
                st.markdown(
                    '<div class="exam-section-label">✅ Eligibility Criteria</div>'
                    f'<div style="font-size:0.9rem;color:#94a3b8;line-height:1.65;margin-bottom:0.5rem;">'
                    f'{html.escape(eligib)}</div>',
                    unsafe_allow_html=True
                )

                # Crucial Dates
                st.markdown(
                    '<div class="exam-section-label">📅 Crucial Dates</div>'
                    f'<div style="font-size:0.9rem;color:#fbbf24;line-height:1.65;margin-bottom:0.5rem;">'
                    f'{html.escape(dates)}</div>',
                    unsafe_allow_html=True
                )

                # Preparation Roadmap
                if roadmap:
                    steps_html = "".join(
                        f'<div class="exam-roadmap-step">'
                        f'<span class="exam-step-num">{si + 1}</span>'
                        f'<span>{html.escape(step)}</span>'
                        f'</div>'
                        for si, step in enumerate(roadmap)
                    )
                    st.markdown(
                        '<div class="exam-section-label">🗺️ Preparation Roadmap</div>'
                        f'<div style="padding-bottom: 24px;">{steps_html}</div>',
                        unsafe_allow_html=True
                    )

                # Official Portal Link
                if link:
                    st.link_button(
                        "🌐  Open Official Portal",
                        url=link,
                        use_container_width=False
                    )

    st.markdown("</div>", unsafe_allow_html=True)  # close page-wrapper

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: Course Guide
# ══════════════════════════════════════════════════════════════════════════════
elif current_page == "Course Guide":
    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)

    # ── Course Guide CSS (Premium Bento Cards — matches Career Engine) ────────
    st.markdown("""
    <style>
    /* ── Course Guide Hero ── */
    .cg-hero {
        text-align: center;
        padding: 0.5rem 1rem 1.5rem;
    }
    .cg-hero h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 800;
        background: linear-gradient(135deg, #2dd4bf 0%, #38bdf8 50%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    .cg-hero p {
        color: #94a3b8;
        font-size: 1.05rem;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.65;
    }

    /* ── Stats Chips ── */
    .cg-stats-bar {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.8rem;
        flex-wrap: wrap;
    }
    .cg-stat-chip {
        background: rgba(45, 212, 191, 0.10);
        border: 1px solid rgba(45, 212, 191, 0.28);
        border-radius: 100px;
        padding: 5px 16px;
        font-size: 0.82rem;
        color: #5eead4;
        font-weight: 600;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* ── Premium Multiselect & Search Bar ── */
    div[data-baseweb="select"] > div,
    input[type="text"] {
        background-color: #0f172a !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 12px !important;
        color: #f8fafc !important;
        transition: all 0.3s ease !important;
    }
    div[data-baseweb="select"] > div:hover,
    input[type="text"]:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 14px rgba(56, 189, 248, 0.18) !important;
    }
    span[data-baseweb="tag"] {
        background-color: rgba(56, 189, 248, 0.12) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.35) !important;
        border-radius: 8px !important;
    }

    /* ── Course Bento Card ── */
    .course-card {
        position: relative;
        background: linear-gradient(
            145deg,
            rgba(255,255,255,0.055) 0%,
            rgba(255,255,255,0.025) 50%,
            rgba(45,212,191,0.015) 100%
        );
        border: 1px solid rgba(255,255,255,0.07);
        border-top-color: rgba(255,255,255,0.12);
        border-left-color: rgba(255,255,255,0.10);
        border-bottom-color: rgba(0,0,0,0.20);
        border-right-color: rgba(0,0,0,0.15);
        border-radius: 22px;
        padding: 2.25rem 2.5rem;
        margin-bottom: 0.25rem;
        backdrop-filter: blur(32px) saturate(180%);
        -webkit-backdrop-filter: blur(32px) saturate(180%);
        overflow: visible !important;
        height: auto !important;
        min-height: fit-content !important;
        transform-style: preserve-3d;
        transform: perspective(1200px) rotateX(0deg) rotateY(0deg) translateZ(0px);
        transition:
            transform     0.4s cubic-bezier(0.23, 1, 0.32, 1),
            border-color  0.4s ease,
            box-shadow    0.4s ease;
        cursor: default;
        box-shadow: 0 4px 24px rgba(0,0,0,0.4), 0 1px 4px rgba(0,0,0,0.3);
    }
    .course-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg,
            transparent 0%,
            rgba(255,255,255,0.35) 30%,
            rgba(255,255,255,0.55) 50%,
            rgba(255,255,255,0.35) 70%,
            transparent 100%
        );
        border-radius: 22px 22px 0 0;
        pointer-events: none;
        z-index: 2;
    }
    .course-card::after {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 22px;
        background: linear-gradient(135deg,
            rgba(45,212,191,0.04) 0%,
            transparent 45%,
            rgba(56,189,248,0.03) 100%);
        pointer-events: none;
        z-index: 1;
    }
    .course-card:hover {
        transform: perspective(1200px)
                   translateY(-6px)
                   translateZ(10px)
                   scale(1.006);
        border-top-color: rgba(255,255,255,0.22);
        border-left-color: rgba(255,255,255,0.18);
        border-bottom-color: rgba(45,212,191,0.35);
        border-right-color: rgba(56,189,248,0.25);
        box-shadow:
            0 40px 100px rgba(0,0,0,0.70),
            0 20px 60px  rgba(0,0,0,0.50),
            0 0  60px rgba(45,212,191,0.22),
            0 0 120px rgba(56,189,248,0.10),
            0 0  30px rgba(139,92,246,0.08);
    }

    /* Accent top line */
    .course-accent {
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, #2dd4bf, #38bdf8, #818cf8);
        border-radius: 22px 22px 0 0;
        opacity: 0;
        transition: opacity 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
        z-index: 3;
    }
    .course-card:hover .course-accent { opacity: 1; }

    /* Card header */
    .course-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.75rem;
        position: relative;
        z-index: 2;
    }
    .course-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(1.2rem, 2.5vw, 1.6rem);
        font-weight: 700;
        color: #f1f5f9;
        line-height: 1.3;
        letter-spacing: -0.02em;
    }
    .course-index {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        color: #2d3a52;
        text-transform: uppercase;
        white-space: nowrap;
        margin-top: 4px;
        flex-shrink: 0;
    }

    /* Field badge */
    .field-badge {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        border-radius: 100px;
        padding: 4px 14px;
        font-size: 0.72rem;
        font-weight: 700;
        font-family: 'Space Grotesk', sans-serif;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
        position: relative;
        z-index: 2;
        transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s ease;
        cursor: default;
    }
    .field-badge:hover {
        transform: scale(1.08) translateY(-3px);
    }
    .field-tech     { background: rgba(45,212,191,0.10); border: 1px solid rgba(45,212,191,0.25); color: #2dd4bf; }
    .field-tech:hover { box-shadow: 0 8px 22px rgba(45,212,191,0.25); }
    .field-law      { background: rgba(245,158,11,0.10); border: 1px solid rgba(245,158,11,0.25); color: #fbbf24; }
    .field-law:hover { box-shadow: 0 8px 22px rgba(245,158,11,0.25); }
    .field-design   { background: rgba(236,72,153,0.10); border: 1px solid rgba(236,72,153,0.25); color: #f472b6; }
    .field-design:hover { box-shadow: 0 8px 22px rgba(236,72,153,0.25); }
    .field-bio      { background: rgba(16,185,129,0.10); border: 1px solid rgba(16,185,129,0.25); color: #34d399; }
    .field-bio:hover { box-shadow: 0 8px 22px rgba(16,185,129,0.25); }
    .field-mgmt     { background: rgba(99,102,241,0.10); border: 1px solid rgba(99,102,241,0.25); color: #a5b4fc; }
    .field-mgmt:hover { box-shadow: 0 8px 22px rgba(99,102,241,0.25); }
    .field-medical  { background: rgba(239,68,68,0.10); border: 1px solid rgba(239,68,68,0.25); color: #f87171; }
    .field-medical:hover { box-shadow: 0 8px 22px rgba(239,68,68,0.25); }
    .field-arch     { background: rgba(168,85,247,0.10); border: 1px solid rgba(168,85,247,0.25); color: #c084fc; }
    .field-arch:hover { box-shadow: 0 8px 22px rgba(168,85,247,0.25); }
    .field-default  { background: rgba(56,189,248,0.10); border: 1px solid rgba(56,189,248,0.25); color: #38bdf8; }
    .field-default:hover { box-shadow: 0 8px 22px rgba(56,189,248,0.25); }

    /* Fees badge */
    .fees-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16,185,129,0.08);
        border: 1px solid rgba(16,185,129,0.22);
        border-radius: 100px;
        padding: 5px 14px;
        font-size: 0.78rem;
        font-weight: 600;
        color: #34d399;
        font-family: 'Space Grotesk', sans-serif;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 2;
        transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s ease;
    }
    .fees-badge:hover {
        transform: scale(1.06) translateY(-2px);
        box-shadow: 0 6px 20px rgba(16,185,129,0.25);
    }
    .fees-dot {
        width: 7px; height: 7px;
        background: #10b981;
        border-radius: 50%;
        flex-shrink: 0;
        box-shadow: 0 0 10px #10b981;
    }

    /* Info grid (colleges, exams, coaching) */
    .course-info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.1rem 2rem;
        margin-bottom: 1.6rem;
        position: relative;
        z-index: 2;
    }
    @media (max-width: 640px) { .course-info-grid { grid-template-columns: 1fr; } }
    .course-info-cell { display: flex; flex-direction: column; gap: 5px; }
    .course-info-label {
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #64748b;
        font-family: 'Space Grotesk', sans-serif;
    }
    .course-info-value {
        font-size: 0.88rem;
        color: #94a3b8;
        line-height: 1.55;
    }
    .course-full-width { grid-column: 1 / -1; }

    /* College list items */
    .college-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 3px 0;
        font-size: 0.86rem;
        color: #94a3b8;
        line-height: 1.5;
    }
    .college-dot {
        width: 5px; height: 5px;
        background: #38bdf8;
        border-radius: 50%;
        flex-shrink: 0;
        opacity: 0.6;
    }
    .college-dot-global {
        background: #818cf8;
    }
    .college-dot-coaching {
        background: #2dd4bf;
    }

    /* Linked exams section */
    .exams-block {
        border-top: 1px solid rgba(255,255,255,0.07);
        padding-top: 1.2rem;
        margin-top: 0.5rem;
        position: relative;
        z-index: 2;
    }
    .exam-tag {
        display: inline-block;
        background: rgba(56,189,248,0.08);
        border: 1px solid rgba(56,189,248,0.20);
        border-radius: 8px;
        padding: 4px 12px;
        font-size: 0.76rem;
        font-weight: 600;
        color: #7dd3fc;
        font-family: 'Space Grotesk', sans-serif;
        margin: 3px 6px 3px 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .exam-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(56,189,248,0.18);
    }

    /* Coaching platforms section */
    .coaching-block {
        border-top: 1px solid rgba(255,255,255,0.07);
        padding-top: 1.2rem;
        margin-top: 0.8rem;
        position: relative;
        z-index: 2;
    }
    .coaching-tag {
        display: inline-block;
        background: rgba(45,212,191,0.08);
        border: 1px solid rgba(45,212,191,0.20);
        border-radius: 8px;
        padding: 4px 12px;
        font-size: 0.76rem;
        font-weight: 600;
        color: #5eead4;
        font-family: 'Space Grotesk', sans-serif;
        margin: 3px 6px 3px 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .coaching-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(45,212,191,0.18);
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero heading ──────────────────────────────────────────────────────────
    st.markdown("""
    <div class="cg-hero">
        <h1>🎓 Course Guide</h1>
        <p>Curated, premium degree programs in India &amp; globally — ranked by 
        institution, fees, entrance exams, and online coaching platforms.</p>
    </div>
    """, unsafe_allow_html=True)


    # ── Load data ─────────────────────────────────────────────────────────────
    try:
        info3_mtime = os.path.getmtime(INFO3_PATH)
    except OSError:
        info3_mtime = 0.0
    courses_data = load_course_data(info3_mtime)

    # ── Search + Filter Controls (3-column cascading) ─────────────────────────
    st.markdown('<div id="cg-search-anchor"></div>', unsafe_allow_html=True)
    all_branches = sorted(list(set(c.get("Degree_Branch", "Other") for c in courses_data)))
    search_col, branch_col, spec_col = st.columns([4, 3, 3])

    with search_col:
        prefill = st.session_state.search_query
        search_course = st.text_input(
            "🔍 Search Degrees or Colleges...",
            value=prefill,
            placeholder="e.g. IIT, MBBS, Architecture…",
            key="cg_search",
        ).lower()
        st.session_state.search_query = ""  # Clear after loading

    # Auto-scroll directly next to the search bar when teleported from Pathway Flowchart
    if st.session_state.get("scroll_to_cg_search", False):
        st.session_state.scroll_to_cg_search = False
        components.html(
            """
            <script>
                setTimeout(function() {
                    const el = window.parent.document.getElementById('cg-search-anchor');
                    if (el) {
                        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                    const inputEl = window.parent.document.querySelector('input[key="cg_search"]') || window.parent.document.querySelector('input[data-testid="stTextInput"]');
                    if (inputEl) {
                        inputEl.focus();
                    }
                }, 150);
            </script>
            """,
            height=0,
            width=0,
        )
    with branch_col:
        selected_branches = st.multiselect("🎓 Degree Branch", all_branches, key="cg_branch")

    # Cascading specialization filter
    avail_specs = sorted(list(set(
        c.get("Specialization_Field", "Other") for c in courses_data
        if not selected_branches or c.get("Degree_Branch") in selected_branches
    )))
    with spec_col:
        selected_specs = st.multiselect("🎯 Specialization", avail_specs, key="cg_spec")

    # ── Filter logic ──────────────────────────────────────────────────────────
    # Smart tokenized search: splits compound queries on + , /
    # then does WORD-LEVEL matching (not substring) so that
    # "B.Tech in Civil Engineering" matches "B.Tech in Civil & Structural Engineering"
    import re as _re
    _STOP_WORDS = {"in", "of", "the", "and", "or", "a", "an", "for", "&", "to", "with"}

    raw_tokens = [t.strip() for t in _re.split(r'[+,]', search_course) if t.strip() and len(t.strip()) >= 2]
    # For each token, extract significant words
    search_word_sets = []
    for tok in raw_tokens:
        words = {w for w in tok.split() if w not in _STOP_WORDS and len(w) >= 2}
        if words:
            search_word_sets.append(words)

    filtered_courses = []
    for c in courses_data:
        text_blob = f"{c.get('Degree_Name','')} {c.get('Degree_Branch','')} {c.get('Specialization_Field','')} {' '.join(c.get('Top_Colleges_India',[]))}".lower()
        blob_words = set(text_blob.split())
        if search_word_sets:
            # A course matches if ALL significant words of ANY token are found in the blob
            match_search = any(all(w in text_blob for w in word_set) for word_set in search_word_sets)
        else:
            match_search = True
        match_branch = c.get("Degree_Branch") in selected_branches if selected_branches else True
        match_spec = c.get("Specialization_Field") in selected_specs if selected_specs else True

        if match_search and match_branch and match_spec:
            filtered_courses.append(c)

    # ── Stats bar ─────────────────────────────────────────────────────────────
    unique_branches = len(set(c.get("Degree_Branch", "") for c in filtered_courses))
    unique_specs = len(set(c.get("Specialization_Field", "") for c in filtered_courses))
    st.markdown(
        f'<div class="cg-stats-bar">'
        f'<span class="cg-stat-chip">📚 {len(filtered_courses)} Degrees</span>'
        f'<span class="cg-stat-chip">🎓 {unique_branches} Branches</span>'
        f'<span class="cg-stat-chip">🎯 {unique_specs} Specializations</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Field-to-CSS-class mapping ────────────────────────────────────────────
    def get_field_class(branch):
        mapping = {
            "B.Tech": "field-tech",
            "Integrated Law": "field-law",
            "B.Des": "field-design",
            "B.Sc.": "field-bio",
            "Integrated Management": "field-mgmt",
            "Medical & Healthcare": "field-medical",
            "B.Arch": "field-arch",
            "B.A.": "field-default",
            "B.Sc. / B.A.": "field-default",
            "B.Com": "field-default",
        }
        return mapping.get(branch, "field-default")

    # ── Build course card HTML ────────────────────────────────────────────────
    def build_course_card(course: dict, idx: int) -> str:
        name = html.escape(course.get("Degree_Name", "Unknown Degree"))

        # Combine the new keys into one string for the existing UI badge
        branch = course.get("Degree_Branch", "")
        spec = course.get("Specialization_Field", "")
        field = html.escape(f"{branch} • {spec}" if branch and spec else branch or "N/A")

        field_cls = get_field_class(course.get("Degree_Branch", ""))

        # India colleges
        india_colleges = course.get("Top_Colleges_India", [])
        india_html = "".join(
            f'<div class="college-item"><span class="college-dot"></span>{html.escape(c)}</div>'
            for c in india_colleges
        )

        # Global colleges
        global_colleges = course.get("Top_Colleges_Global", [])
        global_html = "".join(
            f'<div class="college-item"><span class="college-dot college-dot-global"></span>{html.escape(c)}</div>'
            for c in global_colleges
        )

        # Linked exams as tags
        exams = course.get("Linked_Exams", [])
        if isinstance(exams, str):
            exams = [exams]
        exams_html = "".join(
            f'<span class="exam-tag">{html.escape(e)}</span>' for e in exams
        )

        return f"""
<div class="course-card">
<div class="course-accent"></div>
<div class="course-header">
<div style="flex:1;">
<div class="course-name">{name}</div>
</div>
<div class="course-index">DEGREE · {str(idx + 1).zfill(2)}</div>
</div>
<div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.75rem; margin-bottom:1.5rem;">
<span class="field-badge {field_cls}">📌 {field}</span>
</div>
<div class="course-info-grid">
<div class="course-info-cell">
<span class="course-info-label">🇮🇳 TOP COLLEGES (INDIA)</span>
<div>{india_html}</div>
</div>
<div class="course-info-cell">
<span class="course-info-label">🌍 TOP INSTITUTIONS (GLOBAL)</span>
<div>{global_html}</div>
</div>
</div>
<div class="exams-block">
<div class="course-info-label">📝 LINKED ENTRANCE EXAMS</div>
<div style="margin-top:8px;">{exams_html}</div>
</div>
</div>
"""

    # ── Render cards (single column, generous vertical spacing) ────────────────
    if not filtered_courses:
        st.warning("No degrees found matching your criteria.")
    else:
        st.markdown('<div class="bento-grid">', unsafe_allow_html=True)
        for idx, course in enumerate(filtered_courses):
            st.markdown(build_course_card(course, idx), unsafe_allow_html=True)
            
            # ── Dynamic Interactive Buttons (Matching Career Engine) ──────────
            btn_key_fees = f"btn_cg_fees_{idx}"
            btn_key_coach = f"btn_cg_coach_{idx}"
            toggle_fees = f"toggle_cg_fees_{idx}"
            toggle_coach = f"toggle_cg_coach_{idx}"

            btn_col1, btn_col2, _ = st.columns([1, 1.2, 1], gap="small")
            with btn_col1:
                if st.button("💰 View Average Fees", key=btn_key_fees):
                    st.session_state[toggle_fees] = not st.session_state.get(toggle_fees, False)
            with btn_col2:
                if st.button("💻 View Online Platforms", key=btn_key_coach):
                    st.session_state[toggle_coach] = not st.session_state.get(toggle_coach, False)

            # Conditional Details Rendering
            if st.session_state.get(toggle_fees, False):
                fees_text = html.escape(course.get("Average_Fees", "No data available."))
                st.markdown(
                    f'<div class="surgical-dark-box"><div class="startup-detail" style="border-color:rgba(16,185,129,0.3); background:rgba(16,185,129,0.06); color:#34d399;">'
                    f'💰 <strong>Average Fee Structure:</strong><br>{fees_text}</div></div>',
                    unsafe_allow_html=True
                )
            
            if st.session_state.get(toggle_coach, False):
                platforms = course.get("Online_Coaching_Platforms", [])
                if platforms:
                    platform_tags = "".join(f'<span class="coaching-tag">{html.escape(p)}</span>' for p in platforms)
                    st.markdown(
                        f'<div class="surgical-dark-box"><div class="startup-detail" style="border-color:rgba(45,212,191,0.3); background:rgba(45,212,191,0.06); color:#5eead4;">'
                        f'💻 <strong>Recommended Online Coaching:</strong><br><div style="margin-top:6px;">{platform_tags}</div></div></div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown('<div class="surgical-dark-box">', unsafe_allow_html=True)
                    st.info("No recommended platforms available.")
                    st.markdown('</div>', unsafe_allow_html=True)

            # Spacer to prevent the buttons from overlapping the next card's glowing top border
            st.markdown('<div style="margin-bottom: 3.5rem;"></div>', unsafe_allow_html=True)
                    
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close page-wrapper

