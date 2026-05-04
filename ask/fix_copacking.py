import re
html = open('copacking.html').read()
nav_html = open('nav.html').read()
html = re.sub(r'<nav class="nav" id="nav">.*?</nav>\s*<nav class="mob-menu" id="mob">.*?</nav>', nav_html + '\n<div class="header-spacer"></div>', html, flags=re.DOTALL)
open('copacking.html', 'w').write(html)
print("Fixed copacking!")
