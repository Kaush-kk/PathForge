import streamlit as st
import json
import re
import html
import time
import os


# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Beyond Engineering | Discover Your True Path",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════════════
# MASTER CSS — Enterprise Dark Mode Design System
# ═══════════════════════════════════════════════════════════════════════════════
MASTER_CSS = """
<style>
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
html, body, [data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"] {
    background-color: var(--void) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-primary) !important;
}
[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
}
[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}
section.main > div {
    padding: 0 !important;
}
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"] { display: none !important; }

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
    padding: 0 2rem 4rem;
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
    padding: 4.5rem 2rem 3.5rem;
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
        with open("information.md", "r", encoding="utf-8") as f:
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
        with open("information2.md", "r", encoding="utf-8") as f:
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





# ═══════════════════════════════════════════════════════════════════════════════
# APP RENDER
# ═══════════════════════════════════════════════════════════════════════════════
# Inject CSS
st.markdown(MASTER_CSS, unsafe_allow_html=True)

# Inject background orbs
st.markdown("""
<div class="orb-bg">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)

# Load data once (auto-refreshes whenever source files are modified)
db_mtime   = os.path.getmtime("information.md")  if os.path.exists("information.md")  else 0.0
exam_mtime = os.path.getmtime("information2.md") if os.path.exists("information2.md") else 0.0
all_careers = load_careers(db_mtime)
all_exams   = load_exams(exam_mtime)
total_careers = len(all_careers)
unique_subjects = sorted(set(c["Subject_Interest"] for c in all_careers)) if all_careers else []
unique_styles   = sorted(set(c["Work_Style"]       for c in all_careers)) if all_careers else []

# ── Session State Router ─────────────────────────────────────────────────────
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Career Engine"

def change_page(page_name):
    st.session_state.current_page = page_name

current_page = st.session_state.current_page

# ── Navigation Bar ───────────────────────────────────────────────────────────
nav_items = [
    ("🚀  Career Engine", "Career Engine"),
    ("📝  Exam Directory", "Exam Directory"),
    ("🎓  Course Guide", "Course Guide"),
]
nav_cols = st.columns(len(nav_items))
for col, (label, page_key) in zip(nav_cols, nav_items):
    with col:
        is_active = (current_page == page_key)
        if st.button(
            label,
            key=f"nav_{page_key}",
            use_container_width=True,
            type="primary" if is_active else "secondary",
        ):
            if not is_active:
                change_page(page_key)
                st.rerun()

st.markdown("<hr style='margin:0.5rem 0 1.5rem 0; border:none; border-top:1px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: Career Engine
# ══════════════════════════════════════════════════════════════════════════════
if current_page == "Career Engine":
    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)

    # ── Hero ─────────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="hero">
        <div class="hero-eyebrow">
            <div class="hero-dot"></div>
            Career Intelligence Platform &nbsp;·&nbsp; India Edition
        </div>
        <h1 class="hero-title">Beyond Engineering:<br>Discover Your True Path</h1>
        <p class="hero-subtitle">
            Select your academic interest and preferred work style to uncover premium,
            future-proof career paths — curated for India's next-generation innovators.
        </p>
        <div class="hero-stats">
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

                btn_col, fc_col, exam_col = st.columns([1, 1, 1], gap="small")
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

                # Render startup detail panel based on persisted toggle state
                if st.session_state.get(toggle_key, False):
                    startup_text = html.escape(career.get("Startup_Potential", "No data available."))
                    st.markdown(
                        f'<div class="startup-detail">🚀 <strong>Startup Potential:</strong><br>{startup_text}</div>',
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
    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)
    # ── Section Header ────────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero" style="padding-bottom:2rem;">
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
                        f'{steps_html}',
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
# PAGE: Course Guide (Placeholder)
# ══════════════════════════════════════════════════════════════════════════════
elif current_page == "Course Guide":
    st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="placeholder-pane">
        <div class="placeholder-icon">🎓</div>
        <div class="placeholder-badge">Coming Soon</div>
        <div class="placeholder-title">Course Guide</div>
        <div class="placeholder-sub">
            Curated, ranked lists of the best B.Sc., B.Des., B.A., and B.Tech programs
            in India and globally for every career path in our database. Including
            college rankings, fee structures, and scholarship opportunities.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


