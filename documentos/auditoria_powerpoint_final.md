# Auditoría final del PowerPoint — Del acero al algoritmo

**Fecha:** 27-09-2026

## PowerPoint oficial

`presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`

La presentación sigue la lógica visual mostrada por el profesor: títulos directos, tarjetas de indicadores, gráficos simples, una idea principal por diapositiva y una interpretación breve.

## Estructura final

La exposición principal queda en **14 diapositivas** y la defensa dispone de **3 anexos**, para un total de **17 diapositivas**.

| # | Contenido | Objetivo |
|---|---|---|
| 1 | Portada | Instalar la pregunta central “Del acero al algoritmo”. |
| 2 | Contexto del análisis y muestra | Explicar 106.555, 101.093, 101.067 y 1.273, además del control de calidad. |
| 3 | Áreas de estudio | Mostrar frecuencias relativas y concentración principal. |
| 4 | Género | Mostrar distribución global y diferencias en familias seleccionadas. |
| 5 | Edad promedio por institución | Visualizar CRUCH, privadas, CFT e IP. |
| 6 | Clasificación Acero/Algoritmo | Presentar las nueve familias y aclarar que la taxonomía es propia. |
| 7 | Hallazgo central | Destacar 20,15% vs. 6,92% y ≈2,9:1. |
| 8 | Pregunta 1 | Comparar mediana de arancel por área. |
| 9 | Pregunta 2 | Comparar grupos 15–19 y 40+ por tipo de institución. |
| 10 | Pregunta 3 | Explicar el criterio P90, 128 ofertas y 10,1%. |
| 11 | Perfil del grupo P90 | Resumir institución, área, provincia y duración. |
| 12 | Territorio | Diferenciar proporción y volumen absoluto. |
| 13 | Conclusiones | Responder el objetivo sin causalidad. |
| 14 | Cierre | Dejar la pregunta futura Acero + Algoritmo. |
| 15 | Anexo: herramientas | Relacionar el trabajo con herramientas realmente presentes en el notebook. |
| 16 | Anexo: preguntas probables | Preparar la defensa individual. |
| 17 | Anexo: conceptos clave | Frecuencia relativa, mediana, P90 y desviación estándar. |

## Correcciones de alineación realizadas

1. La diapositiva 2 muestra ahora control de calidad: **0 duplicados completos**, nulos en variables de acreditación y **26 aranceles $0 excluidos** del análisis de precios.
2. La diapositiva 10 aclara que la evaluación pide **diseñar un criterio reproducible** y que el criterio elegido es **P90**, trabajado mediante percentiles del Laboratorio 4.
3. La diapositiva 15 dejó de atribuir al notebook gráficos o funciones que no aparecen en la versión final.
4. El anexo de herramientas ahora declara únicamente:
   - Pandas: `read_excel`, `head`, `info`, filtros;
   - frecuencias: `groupby().size()`, relativas y `cumsum()`;
   - gráficos: barras y `subplots`;
   - tendencia/percentiles: `mean`, `median`, `mode`, `quantile`, `crosstab`;
   - dispersión/comparaciones: rango, `std`, CV, `agg`, `isin`.
5. La defensa de P90 explica que se trata de un **criterio diseñado**, no de una fórmula impuesta por la pauta.

## Pregunta 3

La presentación usa exclusivamente:

- **P90 = $4.106.400**;
- **128 de 1.273 ofertas**;
- **10,1%**;
- **73 CRUCH**;
- **55 privadas**;
- **123 Concepción**;
- **5 Biobío**;
- **38 Salud**;
- **38 Tecnología**.

No aparecen RIC, `Q3 + 1,5 × RIC`, varianza ni `var()`.

## Coherencia con el notebook

El PowerPoint se limita a resultados que tienen respaldo en el notebook actual. Los detalles técnicos completos permanecen en el `.ipynb`; la presentación actúa como síntesis visual y no como copia del notebook.

## Interpretación

Se mantiene la regla:

**resultado observado o asociación ≠ causa demostrada**.

La presentación evita afirmar que edad, territorio, duración o tipo de institución causan los patrones observados.

## Validación técnica

El workflow `.github/workflows/generar_presentacion.yml` validó automáticamente:

- **17 diapositivas**;
- presencia de P90 y resultados principales;
- presencia de `cumsum()` y del control de calidad;
- ausencia de RIC/Tukey, `var()`, 10,6% y el listado antiguo de gráficos no utilizados.

Resultado del workflow: **SUCCESS**.

## Arquitectura del repositorio

- Generador: `presentacion/generar_presentacion_profesor.py`
- Salida: `presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`
- Workflow: `.github/workflows/generar_presentacion.yml`

## Criterio final de defensa

El estudiante debe poder explicar:

1. por qué existen distintas unidades de análisis;
2. cómo se preparó y revisó la base;
3. qué significa la clasificación Acero/Algoritmo;
4. cómo se responden las tres preguntas obligatorias;
5. por qué P90 es el criterio elegido en la Pregunta 3;
6. qué resultados son descriptivos y qué conclusiones no permite la base.
