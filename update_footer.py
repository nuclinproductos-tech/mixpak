import re
import glob

html_files = [
    'index.html',
    'desarrollo-producto.html',
    'envasado-avanzado.html',
    'diseno-packaging.html',
    'fabricacion-propia.html',
    'calidad-regulatorio.html',
    'idi-continuo.html'
]

new_css = """/* ===================================================
   FOOTER UNIFICADO
=================================================== */
.footer-unified {
  background: var(--navy);
  padding: 40px 0;
}
.footer-unified-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 24px;
}
.footer-unified-left {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.footer-unified-logo img {
  height: 32px;
  width: auto;
  filter: brightness(0) invert(1);
}
.footer-unified-copy {
  font-size: 0.75rem;
  color: rgba(255,255,255,0.35);
  margin: 0;
}
.footer-unified-nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
}
.footer-unified-nav a {
  color: rgba(255,255,255,0.5);
  transition: color 0.2s;
}
.footer-unified-nav a:hover {
  color: #fff;
}
.footer-unified-nav .sep {
  color: rgba(255,255,255,0.2);
}
.footer-unified-right {
  text-align: right;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.footer-unified-contact {
  font-size: 0.8rem;
  color: rgba(255,255,255,0.5);
  margin: 0;
}
.footer-unified-legal {
  font-size: 0.72rem;
}
.footer-unified-legal a {
  color: rgba(255,255,255,0.3);
  transition: color 0.2s;
}
.footer-unified-legal a:hover {
  color: #fff;
}
.footer-unified-legal .sep {
  color: rgba(255,255,255,0.15);
  margin: 0 4px;
}

@media (max-width: 768px) {
  .footer-unified-inner {
    flex-direction: column;
    text-align: center;
  }
  .footer-unified-left {
    align-items: center;
  }
  .footer-unified-nav {
    justify-content: center;
  }
  .footer-unified-right {
    text-align: center;
    align-items: center;
  }
  .footer-unified-legal {
    display: block;
    margin-top: 8px;
  }
}
"""

new_html = """<footer class="footer-unified">
  <div class="container footer-unified-inner">
    <div class="footer-unified-left">
      <div class="footer-unified-logo">
        <img src="IMG/logo_mixpak_new.png" alt="Mix Pak System" height="32" onerror="this.outerHTML='<span style=\\'color:#fff; font-family:\\\\'DM Serif Display\\\\', serif; font-size:1rem;\\'>Mix Pak System</span>'">
      </div>
      <p class="footer-unified-copy">© 2025 Mix Pak System S.L. · Alhama de Murcia, España</p>
    </div>
    <div class="footer-unified-center">
      <nav class="footer-unified-nav">
        <a href="index.html#servicios">Servicios</a> <span class="sep">·</span>
        <a href="index.html#envases">Formatos</a> <span class="sep">·</span>
        <a href="index.html#sectores">Sectores</a> <span class="sep">·</span>
        <a href="index.html#historia">Historia</a> <span class="sep">·</span>
        <a href="index.html#certificaciones">Calidad</a> <span class="sep">·</span>
        <a href="index.html#contacto">Contacto</a>
      </nav>
    </div>
    <div class="footer-unified-right">
      <p class="footer-unified-contact">968 418 215 · mixpak@mixpaksystem.com</p>
      <div class="footer-unified-legal">
        <a href="#" onclick="openM('aviso');return false">Aviso Legal</a> <span class="sep">·</span>
        <a href="#" onclick="openM('privacidad');return false">Privacidad</a> <span class="sep">·</span>
        <a href="#" onclick="openM('cookies');return false">Cookies</a>
      </div>
    </div>
  </div>
</footer>"""

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # REPLACE CSS
        # from .fund-chip to .foot-legal-sep{...}
        # In case .fund-chip is not there, we can just replace from .foot-main to .foot-legal-sep{...}
        # Actually .fund-chip might be needed by index.html but user said to remove it: "Elimina todos los estilos CSS del footer anterior que ya no se usan (.foot-main, .foot-grid... .fund-chip...)"
        # So I will use regex: r'\.fund-chip[\s\S]*?\.foot-legal-sep\{[^}]*\}'
        css_pattern_1 = re.compile(r'\.fund-chip[\s\S]*?\.foot-legal-sep\s*\{[^}]*\}')
        css_pattern_2 = re.compile(r'\.foot-main[\s\S]*?\.foot-legal-sep\s*\{[^}]*\}')
        css_replaced = False
        
        if css_pattern_1.search(content):
            content = css_pattern_1.sub(new_css, content)
            css_replaced = True
        elif css_pattern_2.search(content):
            content = css_pattern_2.sub(new_css, content)
            css_replaced = True
            
        # REPLACE HTML
        # In index.html, it starts with 
        #   <!-- Footer principal -->
        #   <div class="foot-main">
        # and ends with </footer>
        
        # In subpages, it might start with <!-- FOOTER -->
        html_pattern = re.compile(r'<!--\s*Footer\s*principal\s*-->[\s\S]*?</footer>', re.IGNORECASE)
        html_pattern_2 = re.compile(r'<div class="foot-main">[\s\S]*?</footer>')
        
        if html_pattern.search(content):
            content = html_pattern.sub(new_html, content)
        elif html_pattern_2.search(content):
            content = html_pattern_2.sub(new_html, content)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Failed to update {file_path}: {e}")

