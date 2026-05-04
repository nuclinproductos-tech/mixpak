import glob, re, os

html_files = glob.glob('*.html')
nav_html = open('nav.html').read()

for filepath in html_files:
    if filepath == 'nav.html' or filepath == 'index.html' or filepath == 'copacking.html':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Check if we have the old nav
    if '<nav class="nav" id="nav">' in html:
        # Replace nav
        html = re.sub(r'<nav class="nav" id="nav">.*?</nav>\s*<nav class="mob-menu" id="mob">.*?</nav>', nav_html + '\n<div class="header-spacer"></div>', html, flags=re.DOTALL)
        
        # Add CSS/JS
        if '<link rel="stylesheet" href="css/nav.css">' not in html:
            html = html.replace('</head>', '  <link rel="stylesheet" href="css/nav.css">\n</head>')
        if '<script src="js/nav.js"></script>' not in html:
            html = html.replace('</body>', '<script src="js/nav.js"></script>\n</body>')
            
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")
