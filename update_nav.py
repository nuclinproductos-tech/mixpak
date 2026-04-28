import re

def update_file(filepath, is_index):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    with open('nav.html', 'r', encoding='utf-8') as f:
        nav_html = f.read()

    if is_index:
        nav_html = nav_html.replace('<header class="site-header"', '<header class="site-header header--transparent"')
    
    # 1. Add <link> to <head>
    if '<link rel="stylesheet" href="css/nav.css">' not in html:
        html = html.replace('</head>', '  <link rel="stylesheet" href="css/nav.css">\n</head>')

    # 2. Add <script> before </body>
    if '<script src="js/nav.js"></script>' not in html:
        # Add before the last <script> or before </body>
        html = html.replace('</body>', '<script src="js/nav.js"></script>\n</body>')

    # 3. Remove old HTML
    html = re.sub(r'<!-- ===================== NAVBAR ===================== -->.*?</nav>\s*<!-- Mobile menu -->.*?</nav>', nav_html, html, flags=re.DOTALL)
    
    # In copacking.html, we don't have the "<!-- ===================== NAVBAR ===================== -->" if it was generated differently.
    # Let's check if the generic replace works.
    if not is_index:
        html = re.sub(r'<nav class="nav" id="nav">.*?</nav>\s*<nav class="mob-menu" id="mob">.*?</nav>', nav_html, html, flags=re.DOTALL)
        # Add spacer after header
        html = html.replace('</header>', '</header>\n<div class="header-spacer"></div>')

    # 4. Remove old CSS
    css_pattern = r'/\*\s*={50}\s*NAVBAR\s*={50}\s*\*/.*?/\*\s*={50}\s*HERO\s*={50}\s*\*/'
    html = re.sub(css_pattern, r'/* ===================================================\n   HERO =================================================== */', html, flags=re.DOTALL)

    # copacking.html has its own CSS, so it might not have the NAVBAR block.

    # 5. Remove old JS logic
    js_pattern1 = r'/\* Navbar scroll \+ Efecto 2 \(progreso\) \+ Efecto 4 \(nav-active\) \*/.*?\}\);'
    replacement1 = """/* Efecto 2 (progreso lateral) */
      let _sTick = null;
      window.addEventListener('scroll', () => {
        if (_sTick) return;
        _sTick = setTimeout(() => {
          _sTick = null;
          if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            const pct = (scrollY / (document.body.scrollHeight - innerHeight) * 100).toFixed(1);
            const sp = document.getElementById('scroll-progress');
            if (sp) sp.style.setProperty('--p', pct + '%');
          }
        }, 100);
      });"""
    html = re.sub(js_pattern1, replacement1, html, flags=re.DOTALL)

    js_pattern2 = r'/\* Mobile menu \*/.*?\}\n\n'
    html = re.sub(js_pattern2, '', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_file('index.html', True)
update_file('copacking.html', False)
print("Updated successfully!")
