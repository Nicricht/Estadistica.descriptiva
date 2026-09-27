from pathlib import Path

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
print('Generador del PowerPoint alineado con la rúbrica y el notebook.')
