# Auditoría final del PowerPoint — Del acero al algoritmo

Fecha: 26-09-2026

## PowerPoint oficial

`presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`

La presentación fue rediseñada tomando como referencia visual los ejemplos del profesor proporcionados por el estudiante: títulos directos, tarjetas de indicadores, gráficos simples, una sola idea principal por diapositiva y una caja final de interpretación.

## Estructura final

La exposición principal queda en **14 diapositivas** y la defensa dispone de **3 anexos**, para un total de **17 diapositivas**.

| # | Contenido | Objetivo |
|---|---|---|
| 1 | Portada | Instalar la pregunta central “Del acero al algoritmo”. |
| 2 | Contexto del análisis y muestra | Explicar 106.555, 101.093, 101.067 y 1.273 sin tecnicismos innecesarios. |
| 3 | Áreas de estudio | Mostrar frecuencias relativas y concentración principal. |
| 4 | Género | Mostrar distribución global y diferencias en familias seleccionadas. |
| 5 | Edad promedio por institución | Visualizar CRUCH, privadas, CFT e IP. |
| 6 | Clasificación Acero/Algoritmo | Presentar las nueve familias y aclarar que la taxonomía es propia. |
| 7 | Hallazgo central | Destacar 20,15% vs. 6,92% y ≈2,9:1. |
| 8 | Pregunta 1 | Comparar mediana de arancel por área. |
| 9 | Pregunta 2 | Comparar grupos 15–19 y 40+ por tipo de institución. |
| 10 | Pregunta 3 | Explicar P90, 128 ofertas y 10,1%. |
| 11 | Perfil del grupo P90 | Resumir institución, área, provincia y duración. |
| 12 | Territorio | Diferenciar proporción y volumen absoluto. |
| 13 | Conclusiones | Responder el objetivo sin causalidad. |
| 14 | Cierre | Dejar la pregunta futura Acero + Algoritmo. |
| 15 | Anexo: herramientas | Relacionar el trabajo con laboratorios 0–5. |
| 16 | Anexo: preguntas probables | Preparar la defensa individual. |
| 17 | Anexo: conceptos clave | Frecuencia relativa, mediana, P90 y desviación estándar. |

## Cambios clave respecto de versiones anteriores

1. La presentación deja de funcionar como una clase de estadística y pasa a comunicar resultados.
2. Cada diapositiva tiene una sola idea principal.
3. Los detalles técnicos se mueven a anexos.
4. La Pregunta 3 usa exclusivamente **P90 = $4.106.400**, coherente con el notebook y el Laboratorio 4.
5. No aparecen RIC, `Q3 + 1,5 × RIC`, varianza ni `var()`.
6. Los valores de Pregunta 3 quedan en **128 ofertas, 10,1%, 73 CRUCH, 55 privadas, 123 Concepción, 5 Biobío, 38 Salud y 38 Tecnología**.
7. El contexto posterior a 2021 se conserva en la documentación, pero se retira del cuerpo principal para evitar que eclipse el análisis estadístico obligatorio.
8. Se mantiene la regla interpretativa: **asociación o diferencia observada no equivale a causalidad**.

## Validación visual

La versión generada fue renderizada completa y validada sin elementos fuera del lienzo. El diseño utiliza una paleta consistente de azul oscuro, turquesa, blanco y acentos naranjas, cercana a los ejemplos del profesor sin copiar su contenido.

## Arquitectura del repositorio

Existe una sola ruta de generación oficial:

- Generador: `presentacion/generar_presentacion_profesor.py`
- Salida: `presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`
- Workflow: `.github/workflows/generar_presentacion.yml`

Los generadores y workflows antiguos de la presentación Morph se eliminan para evitar que el repositorio vuelva a producir una versión distinta.

## Criterio final de defensa

El estudiante debe poder explicar cuatro ideas antes que cualquier fórmula:

1. Qué representa cada unidad de análisis.
2. Qué significa la clasificación Acero/Algoritmo.
3. Cómo se responden las tres preguntas obligatorias.
4. Qué conclusiones son descriptivas y cuáles no puede sostener la base.
