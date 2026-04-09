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
   FOOTER COMPLETO Y UNIFICADO
=================================================== */
.footer-unified {
  background: var(--navy);
  padding: 60px 0 30px;
  color: rgba(255,255,255,0.6);
  font-size: 0.85rem;
}
.footer-unified-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}
.footer-unified-logo img {
  height: 64px; /* Mucho mayor */
  width: auto;
  filter: brightness(0) invert(1);
  margin-bottom: 20px;
}
.brand-col p {
  line-height: 1.6;
  margin-bottom: 12px;
}
.footer-col h4 {
  font-family: 'Inter', sans-serif;
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 20px;
}
.footer-col-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.footer-col-nav a {
  color: rgba(255,255,255,0.7);
  transition: color 0.2s;
}
.footer-col-nav a:hover {
  color: var(--gold);
}
.footer-unified-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.1);
  font-size: 0.75rem;
}
.footer-unified-legal {
  display: flex;
  gap: 16px;
}
.footer-unified-legal a {
  color: rgba(255,255,255,0.5);
  transition: color 0.2s;
}
.footer-unified-legal a:hover {
  color: #fff;
}
@media (max-width: 992px) {
  .footer-unified-top {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 768px) {
  .footer-unified-top {
    grid-template-columns: 1fr;
  }
  .footer-unified-bottom {
    flex-direction: column;
    text-align: center;
  }
  .footer-unified-legal {
    justify-content: center;
    width: 100%;
  }
}
"""

new_html = """<footer class="footer-unified">
  <div class="container">
    <div class="footer-unified-top">
      <!-- Columna 1 -->
      <div class="footer-col brand-col">
        <div class="footer-unified-logo">
          <img src="IMG/logo_mixpak_new.png" alt="Mix Pak System" onerror="this.outerHTML='<span style=\\'color:#fff; font-family:\\\\'DM Serif Display\\\\', serif; font-size:1.5rem;\\'>Mix Pak System</span>'">
        </div>
        <p>Partner estratégico en envasado industrial. Especialistas en copacking, formulación y packaging innovador para empresas del sector alimentario, nutricional y cosmético.</p>
        <p><strong>Tel:</strong> 968 418 215 / 968 638 732<br><strong>Email:</strong> mixpak@mixpaksystem.com<br>Alhama de Murcia, España</p>
      </div>
      
      <!-- Columna 2 -->
      <div class="footer-col">
        <h4>Menú Principal</h4>
        <nav class="footer-col-nav">
          <a href="index.html#inicio">Inicio</a>
          <a href="index.html#servicios">Servicios Generales</a>
          <a href="index.html#envases">Formatos</a>
          <a href="index.html#sectores">Sectores</a>
          <a href="index.html#historia">Historia</a>
          <a href="index.html#certificaciones">Calidad y Regulatorio</a>
          <a href="index.html#contacto">Contacto</a>
        </nav>
      </div>
      
      <!-- Columna 3 -->
      <div class="footer-col">
        <h4>Servicios de Envasado</h4>
        <nav class="footer-col-nav">
          <a href="desarrollo-producto.html">Desarrollo de Producto</a>
          <a href="envasado-avanzado.html">Envasado Avanzado</a>
          <a href="diseno-packaging.html">Diseño de Packaging</a>
          <a href="fabricacion-propia.html">Fabricación Propia</a>
          <a href="calidad-regulatorio.html">Calidad &amp; Regulatorio</a>
          <a href="idi-continuo.html">I+D+i Continuo</a>
        </nav>
      </div>
    </div>
    
    <div class="footer-unified-bottom">
      <div class="footer-unified-copy-bot">© 2025 Mix Pak System S.L. · Todos los derechos reservados</div>
      <div class="footer-unified-legal">
        <a href="#" onclick="openM('aviso');return false">Aviso Legal</a>
        <a href="#" onclick="openM('privacidad');return false">Política de Privacidad</a>
        <a href="#" onclick="openM('cookies');return false">Política de Cookies</a>
      </div>
    </div>
  </div>
</footer>"""

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reemplazar CSS antiguo
        css_pattern = re.compile(r'/\* ===================================================\n   FOOTER UNIFICADO[\s\S]*?margin-top: 8px;\n  \}\n\}')
        if css_pattern.search(content):
            content = css_pattern.sub(new_css, content)

        # Reemplazar HTML antiguo
        html_pattern = re.compile(r'<footer class="footer-unified">[\s\S]*?</footer>')
        if html_pattern.search(content):
            content = html_pattern.sub(new_html, content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

