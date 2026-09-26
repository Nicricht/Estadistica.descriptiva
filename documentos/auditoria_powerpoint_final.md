# Auditoría crítica del PowerPoint — Del acero al algoritmo

Fecha: 26-09-2026

## PowerPoint auditado

Versión de 14 diapositivas previa a la corrección final.

## Resultado diapositiva por diapositiva

| # | Estado | Auditoría |
|---|---|---|
| 1 | PARCIAL | El tema “Del acero al algoritmo” estaba correcto, pero la pregunta central no utilizaba todavía la formulación definitiva de capital humano + transformación industrial del Biobío. |
| 2 | PARCIAL | El recorrido por laboratorios demostraba metodología, pero ocupaba demasiado protagonismo al inicio y no instalaba primero el problema regional. |
| 3 | PARCIAL | Presentaba 106.555, 101.093, 101.067 y 1.273 correctamente, pero faltaba explicar con mayor claridad por qué existen tres unidades de análisis y por qué se crean ofertas únicas. |
| 4 | PARCIAL | Clasificación de variables correcta, pero demasiado cercana a una clase teórica para la exposición final. Debía condensarse dentro de la radiografía estadística general. |
| 5 | PARCIAL | Frecuencias correctas, pero faltaba integrarlas a resultados relevantes del proyecto. |
| 6 | PARCIAL | Mostraba tipos de gráficos, pero la presentación final debe priorizar qué descubrimos con ellos y no solo enumerar técnicas. |
| 7 | CUMPLE | La Pregunta 3 utiliza P90, un percentil calculado con `quantile()`, coherente con el contenido del Laboratorio 4. |
| 8 | CUMPLE | Mostraba rango, desviación y CV, que coinciden con las medidas de dispersión del Laboratorio 5. |
| 9 | CUMPLE | La clasificación Acero/Algoritmo y las nueve familias estaba correctamente representada. |
| 10 | CUMPLE | Resultado central actualizado: 20.368 (20,15%) vs 7.000 (6,92%), relación aproximada 2,9:1, sin afirmar déficit. |
| 11 | CUMPLE | Pregunta 1 correcta en mediana y ofertas únicas, con percentiles como complemento descriptivo. |
| 12 | PARCIAL | Los resultados extremos de edad estaban correctos, pero faltaba hacer visible la lógica de tabla de contingencia / porcentajes y reforzar “asociación, no causalidad”. |
| 13 | CUMPLE | Pregunta 3 alineada con P90: 128 ofertas; 10,1%; 55 privadas; 123 en Concepción; 5 en Biobío; Salud 38 y Tecnología 38. |
| 14 | FALTA | Cerraba demasiado pronto. Faltaban ENADEL 2021, dimensión territorial, género, Huachipato, respuesta regional 2024–2026, Acero + Algoritmo, hipótesis futura, línea temporal y fuentes. |

## A. Contenido obligatorio que faltaba

- No corresponde exigir varianza en la síntesis general: no aparece en el Laboratorio 5 entregado por el profesor.
- Explicación clara de oferta académica única.
- Criterio de Pregunta 3: percentil 90 mediante `quantile(0.90)`.
- Contexto regional verificable y fuentes visibles.

## B. Partes desactualizadas

La Pregunta 3 queda alineada con el criterio P90 del notebook y de `documentos/criterio_metodologico.md`.

## C. Cifras utilizadas en la Pregunta 3

- P90: **$4.106.400**.
- 128 ofertas altas.
- 10,1%.
- 73 CRUCH y 55 privadas.
- 123 en Concepción y 5 en Biobío.
- Salud 38 y Tecnología 38.

## D. Riesgos de causalidad

La presentación corregida evita afirmar que:
- el 6,92% cause dificultades laborales;
- la edad cause la elección institucional;
- Huachipato cerrara por falta de talento tecnológico;
- institución, duración o territorio causen el arancel;
- exista un déficit profesional demostrado.

## E. Contexto regional incorporado

- ENADEL 2021 Biobío.
- Huachipato como punto de inflexión posterior a la línea base.
- Plan de Fortalecimiento Industrial.
- Manufactura avanzada e Industria 4.0.
- Sistemas inteligentes y mantenimiento predictivo.
- Capital humano avanzado en IA.
- Estrategia Biobío 2050.

## F–I. Decisiones visuales

Se mantienen los gráficos estadísticos útiles y el contraste 20,15% vs 6,92%. Se reducen las diapositivas puramente pedagógicas y se integran los contenidos del curso dentro de resultados del proyecto. La presentación corregida utiliza imágenes y objetos independientes, fondos variables y transición Morph por objeto.

## J. Historia final

La versión corregida sigue el recorrido:

**Biobío industrial → matrícula 2021 → radiografía estadística → Acero/Algoritmo → preguntas obligatorias → señal laboral → territorio/género → Huachipato → respuesta industrial/tecnológica → hipótesis futura → 2050.**

## Criterio de cierre

El resultado central se expresa como línea base descriptiva:

> En la fotografía educativa de 2021, la formación asociada a motores productivos tenía un peso cercano a tres veces la formación clasificada como capacidades transformadoras. Esto no demuestra una brecha laboral, pero adquiere relevancia frente a la posterior agenda de fortalecimiento industrial, manufactura avanzada e Industria 4.0 del Biobío.
