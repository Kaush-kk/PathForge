import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the block we want to extract
pattern = r'(    # ── Full-Screen Animated Hero Banner ──────────────────────────────────────\n    HERO_SHADER_HTML = """\n    <div style="position:relative; width:100%; height:92vh; overflow:hidden; background:#03040a;">.*?render_nav_bar\(current_page, "ce"\)\n)'
match = re.search(pattern, content, re.DOTALL)
if not match:
    print("Failed to find HERO block!")
    exit(1)

hero_block = match.group(1)

# Remove the hero block from its current location
content = content.replace(hero_block, "")

# Find the insertion point: right before "if current_page == 'Career Engine':"
insertion_point = r'(# ══════════════════════════════════════════════════════════════════════════════\n# PAGE: Career Engine\n# ══════════════════════════════════════════════════════════════════════════════\nif current_page == "Career Engine":\n)'
match_ins = re.search(insertion_point, content)
if not match_ins:
    print("Failed to find insertion point!")
    exit(1)

# Dedent the hero block since it's moving outside the if statement
dedented_hero_block = "\n".join([line[4:] if line.startswith("    ") else line for line in hero_block.split("\n")])

new_content = content[:match_ins.start()] + dedented_hero_block + match_ins.group(1) + content[match_ins.end():]

# Remove render_nav_bar from Exam Directory
new_content = new_content.replace('    render_nav_bar(current_page, "exam_directory")\n', '')

# Remove render_nav_bar from Course Guide
new_content = new_content.replace('    render_nav_bar(current_page, "course_guide")\n', '')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully moved Hero block and removed redundant nav bars.")
