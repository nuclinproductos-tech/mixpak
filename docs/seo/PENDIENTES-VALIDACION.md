# Pendientes de validación · afirmaciones NO publicadas

Rama `seo-geo-v2`, 05-11-2026. Nada de lo que aparece aquí se ha publicado en la web. Antes de publicarlo hace falta una prueba documental o la aprobación de la persona responsable.

## 1. No publicado por falta de pruebas o de aprobación

| Tema | Situación | Qué hace falta |
|---|---|---|
| Pedidos mínimos por formato | Excel sin aprobación final de Producción (celdas amarillas) | Ver `BORRADOR-pedidos-minimos-NO-PUBLICAR.md` |
| Titularidad de fórmulas / propiedad intelectual del cliente | No documentada | Política escrita aprobada por Dirección/Legal |
| Condiciones de exportación / países / mercados | No documentadas (por eso se quitó `areaServed` del JSON-LD) | Lista de mercados y condiciones |
| Plazos de producción y desarrollo | No documentados | Plazos orientativos aprobados por Producción |
| Capacidades no documentadas (uds/hora, turnos, tamaños de lote) | No documentadas | Datos de Producción |
| Sachet bicompartimento «patentado» | El Excel pide confirmar el n.º de patente. Se ha retirado «patentado», «Patented» y «el único envase del mercado» en ES/EN/PT | N.º de patente u OEPM/EPO |
| Clientes concretos, logos, testimonios, cifras de clientes | NDA | Solo se usa la frase autorizada: «Fabricamos para grandes cadenas de distribución y marcas líderes internacionales.» |

## 2. Certificaciones: alcance que hay que confirmar

- **Verificado en el repo:** `assets/img/certificado-iso22716-gmp.avif` es el sello URS «ISO 22716 · Certified Cosmetics Good Manufacturing Practices». Por tanto **GMP = ISO 22716 (GMP cosmética)**, un solo sistema y no dos certificados. La web ahora lo nombra así y ha dejado de presentarlo en contextos de alimentación, complementos e higiene doméstica.
- **IFS Food:** en el repo solo está el logo (`logo-IFS-clean.png`), no el certificado. Hay que confirmar con el certificado vigente:
  - el alcance (qué familias de producto y qué planta o plantas cubre);
  - si cubre **complementos alimenticios** y **nutrición deportiva** (la web lo da a entender en esos sectores);
  - si cubre **cuidado animal**: la página de pet care sigue mostrando «IFS Food» en dos sellos. El alcance de IFS Food para pet food no está verificado.
- **ISO 22716:** hay que confirmar qué planta o plantas y qué actividades cubre (fabricación, llenado, acondicionamiento).
- Las etiquetas «Sala blanca / Cleanroom / Sala branca» se mantienen sin «GMP». Si la sala blanca tiene una clasificación (ISO 14644), se puede añadir.

## 3. Cifras ya publicadas que no estaban en la lista de hechos confirmados

Siguen publicadas porque ya lo estaban, pero convendría validarlas: **+130 empleados**, **+14.000 m²** (y el hito **+8.000 m²** de la línea del tiempo), **+20 años**, premios (DuPont Innovation Award, PYME más innovadora, UCAM, premio europeo 2015). Que +8.000 m² y +14.000 m² convivan no es una incoherencia: son hitos sucesivos de la línea del tiempo.

## 4. Fuera del alcance del repositorio (servidor / Plesk)

- `http://` no redirige a `https://` y `www.` sirve la web con 200 sin redirigir: hay contenido duplicado. Hay que configurar en Plesk una redirección 301 a `https://mixpaksystem.com`.
- Las URLs sin `.html` (`/copacking`) dan 404. El canonical y el sitemap ya usan `.html`. Si en el futuro se quieren URLs limpias, hay que configurar la reescritura en el servidor **antes** de cambiar canonicals y sitemap.
- La carpeta `preview-linea-envasado/` (no versionada) no debe subirse al servidor.

## 5. Detectado y no corregido (no es SEO / riesgo visual)

- En móvil (390 px) hay 8 px de desbordamiento horizontal causado por `.mobile-panel` del menú. Ya ocurría en `main`.
- En `desarrollo.html` hay un error de JavaScript en consola que ya existía en `main`: `Identifier 'io' has already been declared` (dos scripts inline declaran `io`). Puede impedir que se ejecute uno de esos bloques.
- El inglés mezcla grafía británica y americana (analyse/analyze).
- Imágenes OG (`assets/img/og/*.jpg`): revisar que ninguna muestre producto real de clientes (NDA).
