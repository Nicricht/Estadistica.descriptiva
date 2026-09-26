# Alineación del proyecto con el método del profesor

**Fecha:** 26-09-2026

## Regla principal

El notebook distingue dos capas:

1. **Contenido enseñado por el profesor**, reproducido con las mismas herramientas y un nivel de código similar.
2. **Decisiones propias del proyecto**, necesarias para responder las preguntas con la base del Biobío.

## Laboratorio 0 — Introducción a Pandas

Profesor: `read_excel()`, `head()`, `tail()`, `shape`, `info()`, selección, `value_counts()`, filtros y `groupby()`.

Proyecto: carga del Excel, revisión de dimensiones, tipos de datos, niveles de carrera y filtro de pregrado.

## Laboratorio 1 — Conceptos básicos de estadística

Profesor: población, muestra y clasificación de variables.

Proyecto: identificación de la población de matrículas y clasificación de variables relevantes.

## Laboratorio 2 — Tablas de frecuencia

Profesor: `groupby().size()`, frecuencia absoluta, relativa, acumulada, `pd.cut()` y ordenamiento.

Proyecto: frecuencias de género, área, edad y arancel.

## Laboratorio 3 — Gráficos

Profesor: barras, circular, agrupaciones, `subplots`, etiquetas y gráficos de distribución.

Proyecto: barras por área, edad, arancel y comparaciones entre grupos.

## Laboratorio 4 — Tendencia central y percentiles

Profesor: `mean()`, `median()`, `mode()`, `quantile()`, `describe()`, `groupby()`, `agg()` y `crosstab()`.

Proyecto: media, mediana y moda de edad/arancel; cuartiles; comparación por área e institución.

## Laboratorio 5 — Medidas de dispersión

Profesor: máximo, mínimo, rango, desviación estándar, coeficiente de variación, `groupby()`, `agg()` e `isin()`.

Proyecto: el bloque general de dispersión usa ahora esas mismas medidas.

**No se presenta `var()` como contenido del profesor**, porque no aparece en el Laboratorio 5 entregado.

## Aplicaciones propias del proyecto

Estas operaciones no se atribuyen al profesor:

- `drop_duplicates()` para construir 1.273 ofertas académicas únicas. Se usa para no repetir el mismo precio una vez por cada estudiante.
- La clasificación “Del acero al algoritmo”. Es una taxonomía creada para este análisis.
- La Pregunta 3 usa el **percentil 90**, calculado con `quantile(0.90)`, aplicando el trabajo con percentiles del Laboratorio 4.
- La selección de carreras en familias productivas y transformadoras.

## Conclusión de la auditoría

El núcleo estadístico del notebook usa herramientas presentes en los laboratorios del profesor. Las técnicas adicionales quedan explícitamente identificadas como decisiones metodológicas del proyecto, en lugar de presentarse como si hubieran sido enseñadas literalmente en clase.
