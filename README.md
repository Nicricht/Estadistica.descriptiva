# Estadística descriptiva

# **DEL ACERO AL ALGORITMO**
## *¿Desde qué base de capital humano parte el Biobío para transformar su histórica vocación industrial hacia una economía de manufactura avanzada e Industria 4.0?*

## Idea central

El proyecto utiliza las matrículas de Educación Superior del Biobío de 2021 como una **línea base descriptiva** del capital humano que se estaba formando en la región.

### “Acero”: motores productivos
- Industria y manufactura
- Construcción e infraestructura
- Logística y puertos
- Forestal y madera
- Pesca y acuicultura
- Agroalimentario

### “Algoritmo”: capacidades transformadoras
- Digital y TIC
- Automatización y robótica
- Energía, sustentabilidad y biotecnología

La idea no es “Acero vs. Algoritmo”, sino **Acero + Algoritmo**: transformar una base industrial histórica incorporando digitalización, automatización, datos, energía e innovación.

## Hallazgo principal

Sobre **101.093 matrículas de pregrado**:

- Motores productivos: **20.368 matrículas, 20,15%**.
- Capacidades transformadoras: **7.000 matrículas, 6,92%**.
- Otros campos: **73.725 matrículas, 72,93%**.
- Relación aproximada: **2,9 a 1**.

La interpretación correcta es descriptiva: en la fotografía educativa de 2021, el componente formativo asociado a motores productivos tenía un peso cercano a tres veces el componente clasificado como capacidades transformadoras.

Esto **no demuestra déficit laboral ni causalidad**.

## Bases de análisis

- Base original: **106.555 registros**.
- Pregrado para análisis de personas, edad e “Acero/Algoritmo”: **101.093 matrículas**.
- Pregrado con arancel > $0 para análisis de precio: **101.067 matrículas**.
- Ofertas académicas únicas para comparar precios: **1.273 ofertas**.

Una oferta académica única evita contar el mismo precio una vez por cada estudiante matriculado.

## Preguntas obligatorias

### 1. ¿Hay áreas del conocimiento donde las carreras sean más caras?
Criterio principal: **mediana del arancel por área** sobre ofertas únicas.

- Mediana global: **$2.030.000**.
- Derecho: **$3.586.000**.
- Ciencias Básicas: **$3.290.000**.
- Agropecuaria: **$2.981.500**.

### 2. Edad y tipo de institución
Se interpreta como **asociación**, no causalidad.

- 15–19 años: CRUCH **46,24%**, IP **19,30%**.
- 40 años o más: IP **52,93%**, CRUCH **10,88%**.

### 3. ¿Hay carreras cuyo arancel sea sustantivamente más caro que la mayoría?
Criterio definitivo: **Q3 + 1,5 × RIC**.

- Q1: **$1.616.000**.
- Q3: **$2.580.000**.
- RIC: **$964.000**.
- Límite superior: **$4.026.000**.
- Ofertas sobre el límite: **135 de 1.273 (10,6%)**.
- CRUCH: **73**; privadas: **62**.
- Concepción: **129**; Biobío: **6**.
- Salud: **39**; Tecnología: **39**.
- Duración mediana: **10 semestres** en ofertas altas vs. **5** en el resto.

## Contenidos estadísticos cubiertos

El notebook aplica los laboratorios 0 al 5 del profesor y la pauta:

- Pandas y filtros;
- población, muestra y clasificación de variables;
- frecuencias absoluta, relativa y acumuladas cuando corresponde;
- gráficos circular, barras, histogramas, subplots y dispersión;
- media, mediana, moda y percentiles;
- `describe()`, `groupby()`, `agg()` y `crosstab()`;
- rango, desviación estándar y coeficiente de variación, como en el Laboratorio 5;
- Q1, Q3 y `quantile()` del Laboratorio 4, usados como base para construir el **RIC** en la Pregunta 3.

## Contexto regional

La línea base 2021 se conecta con señales y procesos posteriores del Biobío: dificultades de contratación reportadas por ENADEL, el cierre siderúrgico de Huachipato como punto de inflexión regional, el Plan de Fortalecimiento Industrial, manufactura avanzada, Industria 4.0, sistemas inteligentes, mantenimiento predictivo, capital humano avanzado y la estrategia Biobío 2050.

Estas conexiones se presentan como **contexto e hipótesis de investigación**, nunca como causalidad demostrada por la matrícula 2021.

## Hallazgos secundarios

- Industria y manufactura: **11,10%** de la matrícula.
- Digital y TIC: **3,33%**.
- Automatización y robótica: **2,58%**.
- Energía, sustentabilidad y biotecnología: **1,02%**.
- Mujeres en Digital y TIC: **11,50%**.
- Mujeres en Automatización y robótica: **5,79%**.

## Estado

- ✅ Un único notebook oficial: `notebooks/Estadistica_Descriptiva_Biobio.ipynb`.
- ✅ Notebook alineado con los laboratorios del profesor.
- ✅ Preguntas obligatorias 1, 2 y 3 preservadas.
- ✅ Criterio Q3 + 1,5 × RIC restaurado y documentado.
- ✅ Dispersión alineada con el Laboratorio 5: rango, desviación estándar y coeficiente de variación.
- ✅ RIC conservado solo como aplicación de los cuartiles del Laboratorio 4 para responder la Pregunta 3.
- ✅ Validación local final: **38/38 celdas de código, 0 errores**.
- ✅ Narrativa regional “Del acero al algoritmo” documentada.
- ✅ Auditoría crítica del PowerPoint guardada en `documentos/auditoria_powerpoint_final.md`.
- ✅ PowerPoint final auditado y corregido: **20 diapositivas con 19 transiciones Morph**.
- ⏳ Preparar defensa oral individual.

## Documentación principal

- `documentos/criterio_metodologico.md`
- `documentos/adn_profesional_biobio.md`
- `documentos/contexto_regional_acero_algoritmo.md`
- `documentos/auditoria_notebook_vs_profesor.md`
- `documentos/validacion_ejecucion.md`
- `documentos/auditoria_powerpoint_final.md`

## Gráficos

- `graficos/acero_vs_algoritmo.svg`
- `graficos/familias_adn_profesional.svg`
- `graficos/transformacion_por_provincia.svg`

## Regla de trabajo del repositorio

Este repositorio es la **fuente oficial del proyecto**. Cada cambio debe quedar guardado en GitHub.
