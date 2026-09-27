# Validación de ejecución — Del acero al algoritmo

**Fecha:** 27-09-2026

## Resultado técnico

La versión final del notebook fue validada de principio a fin con el Excel real mediante GitHub Actions.

- Celdas de código: **39**
- Celdas ejecutadas correctamente: **39**
- Errores: **0**
- Registros originales: **106.555**
- Matrículas de pregrado: **101.093**
- Matrículas de pregrado con arancel > $0: **101.067**
- Ofertas académicas únicas: **1.273**
- Duplicados completos: **0**
- Registros con arancel $0 excluidos del análisis de precios: **26**
- Valores nulos: concentrados en variables de acreditación, no utilizadas para responder las tres preguntas.

## Frecuencias

El notebook calcula:

- frecuencia absoluta;
- frecuencia relativa;
- frecuencia acumulada y relativa acumulada en los intervalos ordenados de edad y arancel, usando `cumsum()`.

## Resultado central

| Bloque | Matrículas | % sobre pregrado |
|---|---:|---:|
| Motores productivos | 20.368 | 20,15% |
| Capacidades transformadoras | 7.000 | 6,92% |
| Otros campos | 73.725 | 72,93% |

Relación aproximada: **2,9 a 1**.

## Pregunta 3 — validación definitiva

La evaluación solicita diseñar un criterio reproducible para identificar aranceles sustantivamente altos. El criterio vigente es **percentil 90 (P90)** con `quantile(0.90)`, herramienta trabajada en el Laboratorio 4.

- P90: **$4.106.400**
- Ofertas sobre P90: **128**
- Porcentaje: **10,1%**
- CRUCH: **73**
- Privadas: **55**
- Concepción: **123**
- Biobío: **5**
- Salud: **38**
- Tecnología: **38**
- Duración mediana del grupo alto: **10 semestres**
- Duración mediana del resto: **5 semestres**

No se usa RIC ni la regla `Q3 + 1,5 × RIC` en la respuesta final.

## Interpretación permitida

La base permite describir patrones, diferencias y asociaciones. No demuestra causalidad, déficit profesional ni evolución temporal.

El bloque de dispersión general utiliza **rango, desviación estándar y coeficiente de variación**. La Pregunta 3 utiliza **P90** como medida de posición.

## Estado de validación

El workflow `.github/workflows/validar_notebook.yml` terminó con **SUCCESS** después de:

1. alinear el notebook con los controles de calidad y frecuencias acumuladas;
2. ejecutar todas las celdas;
3. verificar ausencia de errores;
4. comprobar `duplicated()`, `isna()`, `cumsum()` y `quantile(0.90)`;
5. comprobar que no aparezcan la fórmula RIC/Tukey ni `var()`.
