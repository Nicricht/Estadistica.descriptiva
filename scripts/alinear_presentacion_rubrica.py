from pathlib import Path
import json

# -----------------------------------------------------------------------------
# 1) Alinear el generador del PowerPoint con la pauta y el notebook.
# -----------------------------------------------------------------------------
p = Path('presentacion/generar_presentacion_profesor.py')
s = p.read_text(encoding='utf-8')

# Mostrar control de calidad de datos en la diapositiva 2.
old = "note(s,6.88,3.42,4.82,2.55,'DECISIÓN METODOLÓGICA','No repetimos el mismo arancel una vez por cada estudiante. Las 1.273 ofertas únicas permiten comparar precios sin que una carrera con más matrícula pese artificialmente más.',ORG)"
new = old + "\ntext(s,.78,6.28,11.92,.34,'Control de calidad: 0 duplicados completos · nulos solo en acreditación · 26 registros con arancel $0 excluidos del análisis de precios.',8.5,MUT,True,PP_ALIGN.CENTER)"
if old in s and '0 duplicados completos' not in s:
    s = s.replace(old, new)

# Explicar por qué P90 es el criterio metodológico final, sin atribuir una fórmula específica a la pauta.
s = s.replace(
    "s=base('Pregunta 3 · ¿Qué aranceles están entre los más altos?',10,'Usamos el percentil 90 (P90) para estudiar aproximadamente el 10% superior de las ofertas.')",
    "s=base('Pregunta 3 · ¿Qué aranceles están entre los más altos?',10,'Para operacionalizar “sustantivamente más caro”, usamos el percentil 90 (P90), trabajado en el Laboratorio 4.')"
)
s = s.replace(
    "s=base('Pregunta 3 · ¿Qué aranceles están entre los más altos?',10,'La pauta pide diseñar un criterio reproducible; usamos el percentil 90 (P90), trabajado en el Laboratorio 4.')",
    "s=base('Pregunta 3 · ¿Qué aranceles están entre los más altos?',10,'Para operacionalizar “sustantivamente más caro”, usamos el percentil 90 (P90), trabajado en el Laboratorio 4.')"
)

# Pregunta 1: hacer visible el criterio diseñado, porque la pauta lo solicita explícitamente.
s = s.replace(
    "card(s,9.55,1.8,2.45,'$2.030M','mediana global'); note(s,9.2,3.45,3.15,2.08,'RESPUESTA','Sí. Derecho, Ciencias Básicas y Agropecuaria presentan medianas por encima de la mediana global. Usamos mediana porque los valores extremos la afectan menos.',ORG)",
    "card(s,9.55,1.8,2.45,'$2.030M','mediana global'); note(s,9.2,3.45,3.15,2.08,'CRITERIO Y RESPUESTA','Criterio: comparar la mediana por área con la mediana global, porque la mediana es menos sensible a valores extremos. Resultado: Derecho, Ciencias Básicas, Agropecuaria, Tecnología y Salud quedan por encima de $2.030.000; las tres primeras presentan las mayores diferencias.',ORG)"
)

# Pregunta 3: responder de forma explícita la parte de la pauta que pide una explicación
# y considerar variables de la base y el contexto territorial de la región.
s = s.replace(
    "note(s,.78,5.42,11.62,.88,'LECTURA','Las ofertas altas se concentran en determinados tipos de institución, áreas y territorio, y tienen mayor duración mediana. La base no demuestra que estas variables causen el precio.')",
    "note(s,.78,5.28,11.62,1.15,'EXPLICACIÓN ENCONTRADA','Las ofertas sobre P90 se concentran en universidades, Salud y Tecnología, carreras de mayor duración y especialmente en Concepción. La concentración territorial aporta contexto regional; estas asociaciones no demuestran causalidad.',ORG)"
)

# El anexo debe enumerar solo herramientas que realmente aparecen en el notebook vigente.
old_rows = "rows=[('Laboratorio','Contenido aplicado','Uso en el proyecto'),('0 · Pandas','read_excel, head, tail, info, filtros','Carga y preparación de la base'),('1 · Conceptos','población, muestra, tipos de variables','Definición de unidades de análisis'),('2 · Frecuencias','groupby().size(), relativas, acumuladas','Áreas, género, edad y arancel'),('3 · Gráficos','barras, circular, histogramas, scatter','Visualización de distribuciones'),('4 · Tendencia y percentiles','mean, median, mode, quantile, crosstab','Preguntas 1, 2 y P90'),('5 · Dispersión','rango, std, CV, agg, isin','Dispersión general y comparaciones')]"
new_rows = "rows=[('Laboratorio','Contenido aplicado','Uso en el proyecto'),('0 · Pandas','read_excel, head, info, filtros','Carga, revisión y preparación'),('1 · Conceptos','población, muestra, tipos de variables','Definición de unidades de análisis'),('2 · Frecuencias','groupby().size(), relativas, cumsum()','Áreas, género, edad y arancel'),('3 · Gráficos','barras y subplots','Distribuciones y comparación'),('4 · Tendencia y percentiles','mean, median, mode, quantile, crosstab','Preguntas 1, 2 y P90'),('5 · Dispersión','rango, std, CV, agg, isin','Dispersión general y comparaciones')]"
if old_rows in s:
    s = s.replace(old_rows, new_rows)

s = s.replace(
    "('¿Por qué usamos P90?','Porque permite separar aproximadamente el 10% superior usando percentiles trabajados en clase.')",
    "('¿Por qué usamos P90?','Porque necesitábamos un umbral reproducible y P90 usa percentiles trabajados en el Laboratorio 4.')"
)

p.write_text(s, encoding='utf-8')

# -----------------------------------------------------------------------------
# 2) Reforzar las respuestas del notebook con las dos exigencias literales de la pauta.
#    Solo se modifican celdas Markdown; los cálculos y resultados quedan intactos.
# -----------------------------------------------------------------------------
nb_path = Path('notebooks/Estadistica_Descriptiva_Biobio.ipynb')
nb = json.loads(nb_path.read_text(encoding='utf-8'))

p1_text = """## Pregunta 1
### ¿Hay áreas del conocimiento donde las carreras sean más caras?

El análisis se realiza sobre las **1.273 ofertas académicas únicas**, de manera que cada oferta tenga un peso comparable.

**Criterio diseñado:** se compara la **mediana del arancel de cada área** con la **mediana global** de las ofertas. Se utiliza la mediana porque es menos sensible a valores extremos y representa mejor el arancel típico de un área.
"""

p3_extra = (
    "\n"
    "**Explicación encontrada:** dentro de la base, las ofertas sobre P90 se concentran en universidades, especialmente en las áreas de **Salud** y **Tecnología**, presentan una duración mediana mayor y se ubican casi por completo en la provincia de **Concepción**. Estas características ayudan a describir el perfil del grupo de mayor arancel y la concentración en Concepción aporta el contexto territorial de la región. Sin embargo, son asociaciones descriptivas y **no demuestran que estas variables sean la causa directa del precio**.\n"
)

changed = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') != 'markdown':
        continue
    txt = ''.join(cell.get('source', []))

    if txt.startswith('## Pregunta 1\n### ¿Hay áreas del conocimiento donde las carreras sean más caras?'):
        if txt != p1_text:
            cell['source'] = p1_text.splitlines(keepends=True)
            changed = True

    if txt.startswith('### Respuesta') and 'El **percentil 90** de las 1.273 ofertas' in txt:
        if '**Explicación encontrada:**' not in txt and '**Interpretación:**' not in txt:
            txt = txt.rstrip() + '\n' + p3_extra
            cell['source'] = txt.splitlines(keepends=True)
            changed = True

if changed:
    nb_path.write_text(
        json.dumps(nb, ensure_ascii=False, indent=1) + '\n',
        encoding='utf-8'
    )

print('Notebook y generador del PowerPoint alineados con la pauta oficial.')
