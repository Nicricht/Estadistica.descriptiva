# Auditoría final — Notebook vs. contenidos del profesor

**Fecha:** 27-09-2026

## Objetivo

Verificar que el notebook principal obtenga resultados correctos, use herramientas compatibles con los laboratorios del profesor y mantenga una forma de desarrollo defendible: **pregunta → código visible → resultado → interpretación**.

## Laboratorio 0 — Introducción a Pandas

Presente en el notebook: `read_excel()`, `head()`, `shape`, `info()`, filtros y creación de subbases.

Además se incorporó un control explícito de calidad con `isna()` y `duplicated()` para dejar evidencia de nulos y duplicados completos.

## Laboratorio 1 — Población, muestra y variables

Presente: población, base disponible, subbase principal y clasificación de variables cualitativas y cuantitativas.

## Laboratorio 2 — Tablas de frecuencia

Presente: `groupby().size()`, frecuencia absoluta, frecuencia relativa, `pd.cut()` y `cumsum()`.

La frecuencia acumulada se utiliza donde tiene sentido estadístico: **intervalos ordenados de edad y arancel**.

## Laboratorio 3 — Gráficos

El notebook vigente utiliza **gráficos de barras** y `subplots()` para comparar distribuciones y grupos.

No se declara el uso de gráficos circulares, histogramas o scatter porque esas visualizaciones no aparecen actualmente en el notebook final.

## Laboratorio 4 — Tendencia central y percentiles

Presente: `mean()`, `median()`, `mode()`, `quantile()`, `agg()` y `crosstab()`.

La Pregunta 3 utiliza **P90 con `quantile(0.90)`**, herramienta consistente con el trabajo de percentiles del Laboratorio 4.

## Laboratorio 5 — Dispersión

Presente: máximo, mínimo, rango, desviación estándar, coeficiente de variación, comparación de grupos e `isin()`.

No se utiliza `var()` ni se incorpora una fórmula RIC/Tukey en el desarrollo final.

## Calidad y preparación de los datos

La versión final deja evidencia explícita de:

- tamaño de la base con `shape`;
- estructura y valores no nulos con `info()`;
- **0 duplicados completos**;
- valores nulos concentrados en variables de acreditación;
- **26 registros con arancel igual a $0**, excluidos del análisis de precios;
- construcción verificable de **1.273 ofertas académicas únicas**.

## Preguntas obligatorias

### Pregunta 1

Se comparan **1.273 ofertas académicas únicas** mediante mediana de arancel por área, complementada con media, P25, P75 y cantidad de ofertas.

Resultados principales:

- mediana global: **$2.030.000**;
- Derecho: **$3.586.000**;
- Ciencias Básicas: **$3.290.000**;
- Agropecuaria: **$2.981.500**.

### Pregunta 2

Se estudia la asociación entre edad y tipo de institución con `groupby()`, `crosstab()`, frecuencias, porcentajes y gráficos.

- 15–19 años: CRUCH **46,24%**, IP **19,30%**;
- 40 años o más: IP **52,93%**, CRUCH **10,88%**.

La interpretación es descriptiva y no causal.

### Pregunta 3

Para operacionalizar la expresión **“arancel sustantivamente alto”**, el proyecto define un criterio reproducible: **percentil 90**, calculado con `quantile(0.90)`.

Resultados verificados:

- P90: **$4.106.400**;
- ofertas sobre P90: **128 de 1.273 (10,1%)**;
- CRUCH: **73**;
- universidades privadas: **55**;
- Concepción: **123**;
- Biobío: **5**;
- Salud: **38**;
- Tecnología: **38**;
- duración mediana de ofertas altas: **10 semestres**;
- duración mediana del resto: **5 semestres**.

Un documento metodológico interno anterior propuso IQR/Tukey como posible estrategia. Esa propuesta fue descartada del desarrollo final porque no aparece en los laboratorios del profesor revisados. La versión vigente conserva P90 porque utiliza percentiles trabajados en clase. Esta auditoría no presenta IQR como exigencia confirmada de la pauta.

## Aplicación regional “Del acero al algoritmo”

- Motores productivos: **20.368 matrículas (20,15%)**.
- Capacidades transformadoras: **7.000 (6,92%)**.
- Otros campos: **73.725 (72,93%)**.
- Relación aproximada: **2,9 a 1**.

La interpretación es descriptiva. No demuestra déficit profesional ni causalidad laboral.

## Validación técnica

El workflow final ejecutó el notebook completo después de aplicar los ajustes de rúbrica:

- celdas de código: **39**;
- celdas ejecutadas: **39**;
- errores: **0**;
- validación de `duplicated()`, `isna()`, `cumsum()` y `quantile(0.90)`: **correcta**;
- presencia de fórmula RIC/Tukey o `var()`: **0**.

Resultado del workflow: **SUCCESS**.
