with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()
checks = ['levitate', 'gradient-rotate', '3D HOVER', 'translateZ', 'orb-float',
          'income-badge:hover', 'startup-pill:hover', 'gradient-rotate 3s', 'rotateX(-4deg)']
for c in checks:
    found = c in content
    status = 'OK' if found else 'MISSING'
    print(status + ' : ' + c)
print('Total file size: ' + str(len(content)) + ' bytes')