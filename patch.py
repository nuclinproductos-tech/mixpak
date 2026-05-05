import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Corrección 1
content = content.replace(
    '  <!-- Sección "Catálogo de Formatos" movida a copacking.html → id="formatos" -->\n\n  </section>',
    '  <!-- Sección "Catálogo de Formatos" movida a copacking.html → id="formatos" -->'
)

# Corrección 2
content = content.replace(
    '© 2025 Mix Pak System S.L.',
    '© 2026 Mix Pak System S.L.'
)

# Corrección 3
content = content.replace(
    '<a href="/sectores/higiene">Limpieza</a>',
    '<a href="/sectores/higiene">Higiene</a>'
)

# Corrección 4 - Desktop
content = content.replace(
    '''              <a href="/formulacion-desarrollo" role="listitem">
                Formulación y Desarrollo
                <span class="dd-sub">Idea, fórmula y validación</span>
              </a>''',
    '''              <a href="/formulacion-desarrollo" role="listitem">
                Desarrollo de Producto
                <span class="dd-sub">De la idea a la fórmula validada</span>
              </a>'''
)

# Corrección 4 - Mobile
content = content.replace(
    '''            <li><a href="/formulacion-desarrollo">Formulación y Desarrollo<span class="dd-sub">Idea, fórmula y
                  validación</span></a></li>''',
    '''            <li><a href="/formulacion-desarrollo">Desarrollo de Producto<span class="dd-sub">De la idea a la fórmula validada</span></a></li>'''
)

# Corrección 5
content = content.replace(
    '<h2>De la fórmula al producto terminado</h2>',
    '<h2>Un único partner para todo el proceso industrial</h2>'
)

# Corrección 6
stats_block = '''  <!-- ===================== STATS CAPACIDAD ===================== -->
  <section class="stats-capacity">
    <div class="container">
      <div class="stats-row">

        <div class="stat-item">
          <span class="stat-num" data-target="20">0</span>
          <span class="stat-suffix">+</span>
          <span class="stat-label">Años de experiencia</span>
        </div>

        <div class="stat-divider" aria-hidden="true"></div>

        <div class="stat-item">
          <span class="stat-num" data-target="200">0</span>
          <span class="stat-suffix">+</span>
          <span class="stat-label">Clientes activos</span>
        </div>

        <div class="stat-divider" aria-hidden="true"></div>

        <div class="stat-item">
          <span class="stat-num" data-target="30">0</span>
          <span class="stat-suffix">+</span>
          <span class="stat-label">Líneas de producción</span>
        </div>

        <div class="stat-divider" aria-hidden="true"></div>

        <div class="stat-item">
          <span class="stat-num">IFS</span>
          <span class="stat-suffix"> · GMP</span>
          <span class="stat-label">Calidad certificada</span>
        </div>

      </div>
    </div>
  </section>\n\n'''

content = content.replace(stats_block, '')

content = content.replace(
    '''  </section>\n\n  <!-- ===================== CAPACIDAD MULTISECTOR ===================== -->''',
    '''  </section>\n\n''' + stats_block + '''  <!-- ===================== CAPACIDAD MULTISECTOR ===================== -->'''
)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
