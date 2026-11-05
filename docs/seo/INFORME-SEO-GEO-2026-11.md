# Informe SEO + GEO/AEO · mixpaksystem.com · rama `seo-geo-v2`

05-11-2026. Sitio estático, ES en la raíz, EN en `/en/`, PT-PT en `/pt/`, 34 URLs indexables. No se ha hecho push ni despliegue.
Documentos relacionados: `PENDIENTES-VALIDACION.md` y `BORRADOR-pedidos-minimos-NO-PUBLICAR.md`.

## 1. Resumen de la auditoría

**Problemas críticos (corregidos)**
1. **Los canonicals y el sitemap apuntaban a URLs que dan 404.** ES usaba `/copacking`, `/sectores/cosmetica`, etc. sin `.html`, y en producción esas URLs devuelven 404 (comprobado con curl). Google recibía como URL canónica una página inexistente.
2. **Las páginas EN se canonicalizaban hacia ES** (p. ej. `en/copacking.html` tenía como canonical `/copacking`). Algunas apuntaban además a slugs inventados (`/development`, `/sectores/supplements-alimenticios`, `/sectores/hygiene`). Resultado: la versión inglesa quedaba fuera del índice.
3. **El sitemap solo listaba 12 URLs ES, y todas daban 404.** Faltaban las 22 URLs de EN y PT.
4. **Hreflang**: PT declarado como `pt` (no `pt-PT`), y en contacto las alternativas EN/PT apuntaban a la home.

**Contenido y afirmaciones (corregido)**
- «GMP» aparecía como certificación genérica en alimentación, complementos, pet care e higiene. El certificado del repo es **ISO 22716 (GMP cosmética, URS)**: es el mismo sistema, no un segundo certificado, y solo cubre cosmética.
- El sachet bicompartimento aparecía como «patentado» y «el único envase del mercado», sin prueba (el propio Excel pide el n.º de patente).
- La home publicaba pedidos mínimos («desde X uds por referencia») que el Excel no tiene aprobados.
- `desarrollo.html` (ES) tenía las preguntas 1 y 2 de la FAQ en inglés.
- El marco regulatorio de complementos citaba el Reglamento 1925/2006 (adición de vitaminas a alimentos) en lugar de la Directiva 2002/46/CE / RD 1487/2009.
- Había JSON-LD heterogéneo: Service con `areaServed: ES` (mercados no documentados), FAQPage en fabricación sin FAQ visible y 4 bloques sueltos en desarrollo.
- EN usaba «Third-party packing/manufacturing» en lugar de los términos del sector («contract packaging/manufacturing»). PT usaba el calco «a terceiros».
- En EN copacking había un `id` con espacio (`die-cut packs-title`).

**Aspectos que ya estaban bien:** un H1 por página, todas las imágenes con `alt`, enlaces internos sin roturas, `robots.txt` correcto y contenido principal en HTML (las fichas de formatos de la home están en el HTML, no generadas con JS).

## 2. Mapa URL → keyword → intención → acción

Las keywords son objetivos editoriales, no datos de volumen ni de ranking: no se han inventado métricas. Hay que validarlas con Search Console y Keyword Planner.

| URL (ES) | Keyword principal ES / EN / PT | Intención | Sector | Oportunidad | Acción en esta rama |
|---|---|---|---|---|---|
| `/` | fabricación a terceros y copacking / contract manufacturing and co-packing Spain / fabrico para terceiros e copacking | Comercial (encontrar proveedor) | Transversal | Explicar qué hace la empresa, en qué se diferencian copacking y fabricación, y certificaciones | Title/description nuevos, FAQ (6), JSON-LD Organization + WebSite |
| `/desarrollo.html` | formulación y desarrollo de producto / product formulation and development / formulação e desenvolvimento de produto | Comercial-informacional | Transversal | La FAQ ya existía | FAQ ES traducida, marco regulatorio corregido, Service + Breadcrumb |
| `/fabricacion.html` | fabricación a terceros (por contrato) / contract manufacturing / fabrico para terceiros | Comercial | Transversal | Definir el término y aclarar lote piloto y fórmula propia | FAQ (6) visible, Service + Breadcrumb |
| `/copacking.html` | copacking y envasado a terceros / contract packaging, co-packing / copacking e embalamento para terceiros | Comercial | Transversal | Formatos, tipos de producto, pedido mínimo | FAQ (6), retirada de «patentado», Service + Breadcrumb |
| `/empresa.html` | Mix Pak System fabricante Alhama de Murcia | Navegacional / confianza | — | Certificaciones bien nombradas | Tarjeta ISO 22716, AboutPage |
| `/contacto.html` | presupuesto fabricación a terceros | Transaccional | — | — | Title/description, ContactPage, sin hreflang falso |
| `/sectores/complementos-alimenticios.html` | fabricación de complementos alimenticios a terceros / food supplement contract manufacturer / fabrico de suplementos alimentares para terceiros | Comercial | Complementos | Formatos, normativa, lote piloto | FAQ (5), retirado GMP, Service |
| `/sectores/nutricion-deportiva.html` | fabricación de nutrición deportiva a terceros / sports nutrition contract manufacturer | Comercial | Nutrición deportiva | Proteína, creatina, geles, formatos | FAQ (5), Service |
| `/sectores/cosmetica.html` | fabricación de cosmética a terceros / cosmetics contract manufacturing | Comercial | Cosmética | Es el sector donde ISO 22716 sí aplica | FAQ (6), ISO 22716 explícita, Service |
| `/sectores/alimentacion.html` | fabricación y envasado de alimentos a terceros | Comercial | Alimentación | IFS Food, monodosis | FAQ (5), Service |
| `/sectores/higiene.html` | envasado de productos de limpieza e higiene | Comercial | Higiene | Muestras promocionales | FAQ (5), retirado GMP, Service |
| `/sectores/cuidado-animal.html` | envasado de productos para mascotas a terceros | Comercial | Cuidado animal | Formatos pet care | FAQ (5), Service |

Las versiones EN/PT siguen el mismo mapa con la keyword localizada de la columna 2.

## 3. Archivos modificados

- **HTML (las 34 páginas; empresa y contacto solo en el head y en textos de certificación):** `index.html`, `desarrollo.html`, `fabricacion.html`, `copacking.html`, `empresa.html`, `contacto.html`, `sectores/*.html` (6) y sus equivalentes en `en/` y `pt/`.
- **Nuevo:** `css/seo-faq.css`.
- **Reescrito:** `sitemap.xml`.
- **Documentación (no se sube al servidor):** `docs/seo/*.md`.
- **Sin cambios:** todo `js/`, `css/formatos-tunnel.css`, `css/empresa-timeline.css`, `css/shared-*.css`, `css/premium-polish.css`, `robots.txt`.

## 4. Páginas nuevas

**Ninguna**, por decisión deliberada:
- *Formatos y pedidos mínimos*: los mínimos no están aprobados, y sin ellos la página repetiría la sección «Elige tu formato» de copacking (canibalización). Hay un borrador listo para cuando Producción los apruebe.
- *Cómo trabajamos*: el proceso ya está en desarrollo (6 pasos), copacking y cada sector (4 pasos). Una página aparte competiría con ellas sin aportar datos nuevos; habría que tener antes plazos o condiciones aprobadas (pendientes).
- *Páginas sectoriales de fabricación a terceros*: las 6 páginas de sector ya cubren «fabricación de X a terceros». Crear otras canibalizaría. Lo que se ha hecho es reforzar su title, H2 de FAQ y Service con esa keyword.

## 5. FAQs

- 27 secciones nuevas (9 páginas × 3 idiomas) con 147 pares pregunta/respuesta. Más la FAQ de desarrollo, que ya existía y se ha corregido.
- La primera frase de cada respuesta es la respuesta. Ninguna pregunta se repite entre páginas: la del pedido mínimo solo está en copacking y la del NDA solo en desarrollo.
- Usan `<details>/<summary>` nativo con `h3`: el contenido está en el HTML, se abren sin JavaScript y no usan clases de animación (`fi`).
- Solo contienen hechos confirmados o ya publicados en la web. Cuando procede, usan las frases autorizadas sobre clientes y NDA.
- **No** se ha marcado con `FAQPage`: Google limita desde 2023 los resultados enriquecidos de FAQ a webs gubernamentales y sanitarias de autoridad, y esta marca no aportaría ese resultado. Los motores generativos leen el HTML visible.

## 6. Datos estructurados

Un único bloque `@graph` por página:
- `Organization` (`@id` común, legalName, dirección, teléfono, email y logo; descripción en el idioma de la página). En todas las páginas.
- `WebSite`. Solo en las 3 home.
- `WebPage`, `AboutPage` (empresa) o `ContactPage` (contacto), con `inLanguage` (`es`, `en`, `pt-PT`).
- `BreadcrumbList` (Inicio → página). En las 31 páginas interiores.
- `Service`, con `provider` → Organization. En desarrollo, fabricación, copacking y los 6 sectores. **Sin** `areaServed` (mercados no documentados) y sin precios.

Retirado: FAQPage (desarrollo y fabricación) y los bloques duplicados.

Validación: los 34 bloques son JSON válido. Las `@id` y URLs coinciden con el canonical. Queda pendiente pasar el Rich Results Test y el Schema Validator con la web ya publicada.

## 7. Cambios por idioma

- **ES:** FAQ de desarrollo traducida, terminología de certificaciones, titles con «fabricación a terceros».
- **EN:** «contract manufacturing», «contract packaging», «co-packing», «minimum order quantity». Se eliminan «Third-party packing/manufacturing» (menú, empresa, fabricación). Se corrige el `id` con espacio.
- **PT-PT:** `lang="pt-PT"` y `hreflang="pt-PT"`. Terminología «fabrico para terceiros», «embalamento», «saquetas», «frascos-ampola», «boiões», «encomenda mínima». «Embalamento a terceiros» pasa a «para terceiros». No se han encontrado brasileñismos (você, equipe, contato, arquivo…).

## 8. Validación

| Comprobación | Resultado |
|---|---|
| Titles únicos | 34/34 |
| Descriptions únicas y de 158 caracteres o menos | 34/34 |
| Un H1 por página | 34/34. El H1 de la home no ha cambiado |
| Canonical autorreferente que apunta a un archivo existente | 34/34 |
| hreflang recíproco (es/en/pt-PT/x-default), incluido el propio idioma | 33 páginas con equivalentes; contacto, solo ES, sin alternates |
| JSON-LD que parsea | 34/34 |
| Enlaces internos y anclas (`#contacto`, `#contact`…) | 0 rotos |
| Imágenes con alt y archivo existente | 0 errores |
| `sitemap.xml` | XML válido (xmllint), 34 `<loc>` con alternates |
| Tracking y formularios iguales que en `main` | GTM-M3JCQJFR, Consent Mode, `generate_lead`, web3forms (endpoint, `access_key`, `subject`) y HubSpot, mismo número de apariciones. `js/` sin cambios. Bookings pasa de 1 a 4 enlaces, por los enlaces de la FAQ de las 3 home |
| Cambios visuales accidentales | Medición con Chrome headless de la altura de cada sección, `main` frente a la rama, a 1440 px y 390 px: solo crece la nueva sección FAQ (detalle en el apartado 8.1) |

### 8.1 Resultado del barrido visual
34 páginas medidas a 1440 px y 390 px. Fuera de la nueva sección FAQ, las únicas variaciones de altura vienen de cambios de texto intencionados:
- copacking ES: −23 px en el bloque del sachet bicompartimento, al retirar «El único envase del mercado».
- desarrollo ES/EN/PT: +24 a +48 px en la introducción, por la cita regulatoria corregida (Directiva 2002/46/CE / RD 1487/2009).
- empresa EN/PT: ±25 px, por el nuevo texto de la tarjeta ISO 22716.
- Bloque «facilities» de complementos y nutrición: −29 px, por un texto de certificación más corto.
- Contacto EN/PT: +2 px.
- EN copacking: la sección `cp-custom` sale como «nueva» en la medición solo porque se corrigió su `id`; no hay cambio visual.
El hero de la home, la sección de formatos (túnel), el carrusel y la línea del tiempo de Empresa no cambian de altura. No hay errores JS nuevos (el de desarrollo ya existía en `main`).
Las capturas se tomaron con Chrome headless: el panel de navegador integrado no carga localhost.

## 9. Lista de archivos para subir por FileZilla/Plesk

```
index.html  desarrollo.html  fabricacion.html  copacking.html  empresa.html  contacto.html
sectores/alimentacion.html  sectores/complementos-alimenticios.html  sectores/cosmetica.html
sectores/cuidado-animal.html  sectores/higiene.html  sectores/nutricion-deportiva.html
en/index.html  en/desarrollo.html  en/fabricacion.html  en/copacking.html  en/empresa.html
en/sectores/ (los 6 .html)
pt/index.html  pt/desarrollo.html  pt/fabricacion.html  pt/copacking.html  pt/empresa.html
pt/sectores/ (los 6 .html)
css/seo-faq.css   (NUEVO, imprescindible)
sitemap.xml
```
**No subir:** `docs/`, `preview-linea-envasado/`, `.claude/`.
Después de subir: enviar de nuevo el sitemap en Search Console y pedir la indexación de `/en/` y `/pt/`.

## 10. KPIs recomendados (sin línea base: hay que tomarla en Search Console/GA4 antes de publicar)

- Impresiones y clics orgánicos por idioma (filtro de página `/en/`, `/pt/`, raíz) y por grupo de URLs (servicios y sectores).
- Páginas indexadas por idioma (informe de indexación de Search Console). Es el indicador directo de la corrección de canonicals.
- Consultas relevantes: número de consultas distintas con impresiones que contienen «a terceros», «copacking», «contract manufacturing», «fabrico para terceiros» y nombres de formato.
- Formularios enviados (evento `generate_lead` en GA4/GTM) por página de origen e idioma.
- Reuniones reservadas en Microsoft Bookings (clics salientes al enlace de Bookings y reservas confirmadas en Bookings).
- Leads cualificados en HubSpot (negocios creados en el pipeline a partir de formularios web), por sector.
- Opcional GEO: menciones o citas de la marca en respuestas de asistentes de IA, con un panel fijo de preguntas que se revisa cada mes de forma manual.
