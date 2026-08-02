import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inner Hero Content div inside HERO_SHADER_HTML
old_hero_content = '''    <!-- Hero Content -->
    <div style="position:relative; z-index:10; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; text-align:center; padding:2rem;">
        <div style="position:absolute; width:300px; height:300px; top:50%; left:50%; transform:translate(-50%,-50%); background:radial-gradient(circle, rgba(208,188,255,0.15) 0%, transparent 70%); border-radius:50%; pointer-events:none; animation: pf-pulse 4s infinite alternate;"></div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:clamp(3.5rem,10vw,7.5rem); font-weight:700; line-height:1.1; letter-spacing:-0.02em; background:linear-gradient(180deg,#ffffff 0%,#d0bcff 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:0 0 1rem;">PathForge</h1>
        <p style="font-family:'Inter',sans-serif; font-size:1.1rem; line-height:1.6; color:#cbc3d7; max-width:620px; margin:0 auto 2.5rem;">The most powerful AI ever deployed in talent acquisition and career navigation.</p>
        <div style="display:flex; flex-wrap:wrap; gap:1rem; justify-content:center;">
            <a href="#" style="display:inline-flex; align-items:center; gap:8px; background:linear-gradient(135deg,#d0bcff 0%,#4cd7f6 100%); color:#23005c; font-family:'Space Grotesk',sans-serif; font-size:0.78rem; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; padding:14px 32px; border-radius:8px; text-decoration:none; transition:all 0.3s;">Schedule a Consult &#x2192;</a>
            <a href="#" style="display:inline-flex; align-items:center; gap:8px; background:transparent; color:#d0bcff; font-family:'Space Grotesk',sans-serif; font-size:0.78rem; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; padding:14px 32px; border-radius:8px; border:1px solid #d0bcff; text-decoration:none; transition:all 0.3s;">Explore Platform</a>
        </div>
    </div>'''

new_hero_content = '''    <!-- Hero Content -->
    <div style="position:relative; z-index:10; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; text-align:center; padding:3rem 2rem;">
        <div style="position:absolute; width:520px; height:520px; top:50%; left:50%; transform:translate(-50%,-50%); background:radial-gradient(circle, rgba(208,188,255,0.18) 0%, transparent 70%); border-radius:50%; pointer-events:none; animation: pf-pulse 4s infinite alternate;"></div>
        <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(208,188,255,0.1); border:1px solid rgba(208,188,255,0.25); border-radius:100px; padding:6px 22px; font-family:'Space Grotesk',sans-serif; font-size:0.75rem; font-weight:600; color:#d0bcff; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:1.5rem;">✦ NEXT-GEN CAREER INTELLIGENCE PLATFORM</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:clamp(4.2rem,11vw,8.5rem); font-weight:700; line-height:1.05; letter-spacing:-0.03em; background:linear-gradient(180deg,#ffffff 0%,#d0bcff 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:0 0 1.25rem;">PathForge</h1>
        <p style="font-family:'Inter',sans-serif; font-size:1.3rem; line-height:1.7; color:#e5e2e1; max-width:780px; margin:0 auto 3rem;">The most powerful AI ever deployed in talent acquisition and career navigation.</p>
        <div style="display:flex; flex-wrap:wrap; gap:1.5rem; justify-content:center;">
            <a href="#" style="display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg,#d0bcff 0%,#4cd7f6 100%); color:#23005c; font-family:'Space Grotesk',sans-serif; font-size:0.85rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:18px 40px; border-radius:10px; text-decoration:none; box-shadow: 0 8px 30px rgba(208,188,255,0.3); transition:all 0.3s;">Schedule a Consult &#x2192;</a>
            <a href="#" style="display:inline-flex; align-items:center; gap:10px; background:rgba(255,255,255,0.04); color:#d0bcff; font-family:'Space Grotesk',sans-serif; font-size:0.85rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:18px 40px; border-radius:10px; border:1px solid rgba(208,188,255,0.4); text-decoration:none; transition:all 0.3s;">Explore Platform</a>
        </div>
    </div>'''

if old_hero_content in content:
    content = content.replace(old_hero_content, new_hero_content)
    print("Hero content expanded.")
else:
    print("WARNING: Could not find exact old_hero_content.")

# Also adjust iframe margin so the nav bar sits right below the hero buttons
content = content.replace('components.html(HERO_SHADER_HTML, height=700, scrolling=False)', 'components.html(HERO_SHADER_HTML, height=640, scrolling=False)')
content = content.replace('margin-bottom: -48px !important;', 'margin-bottom: -32px !important;')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch hero scale applied.")
