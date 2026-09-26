# Auditoría final — Notebook vs. contenidos completos del profesor

**Fecha:** 26-09-2026

## Objetivo

Verificar que el notebook principal no solo obtenga resultados correctos, sino que recorra **todos los contenidos presentes en los laboratorios 0 al 5** y utilice una forma de desarrollo equivalente a la del profesor.

## Laboratorio 0 — Introducción a Pandas

Aplicado en el notebook:
- importación de Pandas;
- read_excel();
- head() y tail();
- shape;
- type();
- info();
- selección de una o varias columnas;
- value_counts();
- creación de una nueva columna;
- filtros por condición;
- filtros con más de una condición.

## Laboratorio 1 — Población, muestra y variables

Aplicado:
- definición de población;
- definición de muestra;
- clasificación de las variables utilizadas;
- distinción entre cualitativas nominales, ordinales y cuantitativas.

## Laboratorio 2 — Tablas de frecuencia

Aplicado:
- unique();
- groupby().size();
- frecuencia absoluta;
- frecuencia relativa;
- frecuencia absoluta acumulada;
- frecuencia relativa acumulada;
- pd.cut();
- observed=True;
- sort_values();
- tablas para variables nominales, discretas y cuantitativas agrupadas.

## Laboratorio 3 — Gráficos

Aplicado:
- gráfico circular;
- gráfico de barras;
- histogramas construidos con intervalos;
- etiquetas en barras;
- rotación de categorías;
- subplots;
- gráfico de dispersión.

## Laboratorio 4 — Tendencia central y percentiles

Aplicado:
- mean();
- median();
- mode();
- quantile();
- percentiles 25, 50, 75 y 90;
- describe();
- cálculos agrupados;
- DataFrame con media, mediana y percentiles;
- agg();
- crosstab() para análisis bivariado.

## Laboratorio 5 — Dispersión

Aplicado:
- máximo y mínimo;
- rango;
- desviación estándar;
- coeficiente de variación;
- comparación de dispersión entre grupos;
- groupby().agg(['mean','median','std']);
- filtrado de categorías mediante isin().

## Preguntas obligatorias

### Pregunta 1
Se comparan los aranceles de las áreas usando ofertas únicas, mediana, media, percentiles 25 y 75, gráfico de barras y una tabla bivariada con crosstab().

### Pregunta 2
Se analiza la edad por tipo de institución con groupby(), media, mediana, crosstab(), tablas de frecuencia y gráficos.

### Pregunta 3
Se define “sustantivamente caro” mediante **Percentil 90**, siguiendo el mismo enfoque que el Laboratorio 4 para estudiar el 10% superior.

Resultados:
- P90: **$4.106.400**.
- Máximo: **$8.783.670**.
- Ofertas sobre P90: **128 de 1.273 (10,1%)**.
- CRUCH: **73**.
- Privadas: **55**.
- Concepción: **123**.
- Biobío: **5**.
- Duración mediana de ofertas altas: **10 semestres**.
- Duración mediana del resto: **5 semestres**.

## Aplicación regional

“Del acero al algoritmo” se mantiene como aplicación propia, pero su desarrollo utiliza herramientas vistas en clases, principalmente listas, isin(), groupby(), tablas de frecuencia y gráficos.

Resultado:
- Motores productivos: **20.368 matrículas (20,15%)**.
- Capacidades transformadoras: **7.000 (6,92%)**.
- Relación aproximada: **2,9 a 1**.

## Validación técnica

- Celdas de código: **71**.
- Celdas ejecutadas: **71**.
- Errores: **0**.

## Criterio final

El notebook queda estructurado en el mismo orden pedagógico del curso:

**Pandas → conceptos básicos → tablas de frecuencia → gráficos → tendencia central y percentiles → dispersión → aplicación → preguntas obligatorias.**
