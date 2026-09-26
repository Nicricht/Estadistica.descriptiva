# Auditoría final — Notebook vs. contenidos completos del profesor

**Fecha:** 26-09-2026

## Objetivo

Verificar que el notebook principal obtenga resultados correctos, recorra los contenidos de los laboratorios 0 al 5 y mantenga una forma de desarrollo equivalente a la del profesor: **pregunta → código visible → resultado → interpretación**.

## Laboratorio 0 — Introducción a Pandas

Aplicado: `read_excel()`, `head()`, `tail()`, `shape`, `type()`, `info()`, selección de columnas, `value_counts()`, creación de columnas y filtros.

## Laboratorio 1 — Población, muestra y variables

Aplicado: población, muestra y clasificación de variables cualitativas y cuantitativas.

## Laboratorio 2 — Tablas de frecuencia

Aplicado: `unique()`, `groupby().size()`, frecuencia absoluta, relativa, acumuladas cuando corresponden, `pd.cut()`, `observed=True` y `sort_values()`.

## Laboratorio 3 — Gráficos

Aplicado: circular, barras, histogramas, etiquetas, rotación de categorías, `subplots` y dispersión.

## Laboratorio 4 — Tendencia central y percentiles

Aplicado: `mean()`, `median()`, `mode()`, `quantile()`, percentiles, `describe()`, cálculos agrupados, `agg()` y `crosstab()`.

## Laboratorio 5 — Dispersión

Aplicado según el material del profesor: máximo, mínimo, rango, desviación estándar, coeficiente de variación, comparación de grupos e `isin()`.

**Aclaración:** el Laboratorio 5 completo no utiliza `var()`, por lo que la varianza se retiró del bloque principal. La Pregunta 3 utiliza un percentil con `quantile()`, herramienta trabajada en el Laboratorio 4.

## Preguntas obligatorias

### Pregunta 1
Se comparan 1.273 ofertas académicas únicas mediante mediana por área, complementada con percentiles y cantidad de ofertas.

### Pregunta 2
Se estudia la asociación entre edad y tipo de institución con `groupby()`, `crosstab()`, frecuencias, porcentajes y gráficos. No se interpreta causalidad.

### Pregunta 3
Se utiliza el **percentil 90**, calculado con `quantile(0.90)`.

Resultados verificados:
- P90: **$4.106.400**.
- Ofertas sobre P90: **128 de 1.273 (10,1%)**.
- CRUCH: **73**.
- Universidades privadas: **55**.
- Concepción: **123**.
- Biobío: **5**.
- Salud: **38**.
- Tecnología: **38**.
- Duración mediana de ofertas altas: **10 semestres**.
- Duración mediana del resto: **5 semestres**.

## Aplicación regional “Del acero al algoritmo”

- Motores productivos: **20.368 matrículas (20,15%)**.
- Capacidades transformadoras: **7.000 (6,92%)**.
- Otros campos: **73.725 (72,93%)**.
- Relación aproximada: **2,9 a 1**.

La interpretación es descriptiva: la fotografía 2021 muestra una base formativa productiva considerablemente mayor que la transformadora. No demuestra déficit profesional ni causalidad laboral.

## Validación técnica

La versión corregida fue ejecutada localmente con el Excel real:
- celdas de código: **38**;
- celdas ejecutadas: **38**;
- errores: **0**.

Después de recuperar el Laboratorio 5 completo del profesor, el notebook se volvió a alinear para distinguir estrictamente el contenido enseñado de las aplicaciones adicionales del proyecto.
