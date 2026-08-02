#!/usr/bin/env python3
"""Replaces the MASTER_CSS block in app.py with the upgraded 3D premium version."""

NEW_CSS = '''MASTER_CSS = """
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
    margin-bottom: 2rem;
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
    overflow: hidden;
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

/* ── 3D HOVER — tilt + translateZ pop + heavy diffused glow ──────────── */
.bento-card:hover {
    transform: perspective(var(--perspective))
               rotateX(-4deg)
               rotateY(3deg)
               translateZ(28px)
               scale(1.018);
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

/* Startup Detail */
.startup-detail {
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: var(--radius);
    padding: 1rem 1.25rem;
    margin-top: 1rem;
    font-size: 0.88rem;
    color: #c4b5fd;
    line-height: 1.65;
    position: relative;
    z-index: 2;
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
</style>
"""'''

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the MASTER_CSS block boundaries
start_marker = 'MASTER_CSS = """'
end_marker = '"""\n'

start_idx = content.index(start_marker)
# Find the closing triple-quote AFTER the opening one
end_idx = content.index('\n"""\n', start_idx + len(start_marker)) + len('\n"""\n')

old_block = content[start_idx:end_idx]
print(f"Found block: chars {start_idx} to {end_idx}, length {len(old_block)}")

new_content = content[:start_idx] + NEW_CSS + '\n' + content[end_idx:]

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: MASTER_CSS replaced.")