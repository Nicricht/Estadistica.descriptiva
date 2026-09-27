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
- Pregrado para análisis de personas, edad y “Acero/Algoritmo”: **101.093 matrículas**.
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
- Edad media por tipo: CRUCH **22,8**, privadas **24,0**, CFT **25,7**, IP **26,5** años.

### 3. ¿Hay carreras cuyo arancel sea sustantivamente más caro que la mayoría?
Criterio: **percentil 90 (P90)**, utilizando `quantile(0.90)`.

- P90: **$4.106.400**.
- Ofertas sobre P90: **128 de 1.273 (10,1%)**.
- CRUCH: **73**; privadas: **55**.
- Concepción: **123**; Biobío: **5**.
- Salud: **38**; Tecnología: **38**.
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
- percentiles y `quantile()` del Laboratorio 4, usando **P90** en la Pregunta 3.

## PowerPoint oficial

El repositorio tiene **una sola presentación oficial**:

`presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`

La versión actual fue rediseñada siguiendo la lógica visual mostrada por el profesor: una idea principal por diapositiva, gráficos o tarjetas grandes, una interpretación breve y el detalle técnico movido a anexos.

Estructura:

- **14 diapositivas de exposición principal**.
- **3 anexos de defensa individual**.
- **17 diapositivas en total**.

La presentación se genera únicamente desde:

`presentacion/generar_presentacion_profesor.py`

El workflow oficial es:

`.github/workflows/generar_presentacion.yml`

No existen generadores paralelos para otra versión del PowerPoint.

## Contexto regional

La documentación del proyecto conserva contexto adicional sobre ENADEL, Huachipato, fortalecimiento industrial, manufactura avanzada e Industria 4.0. Ese material se mantiene como **contexto e hipótesis de investigación**, pero no domina la presentación principal, que se concentra en los resultados descriptivos de 2021.

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
- ✅ Pregunta 3 resuelta con percentil 90, sin RIC ni fórmula adicional.
- ✅ Dispersión alineada con el Laboratorio 5: rango, desviación estándar y coeficiente de variación.
- ✅ PowerPoint oficial rediseñado con estilo visual cercano al ejemplo del profesor.
- ✅ 14 diapositivas principales + 3 anexos de defensa.
- ✅ Un solo generador y un solo workflow para la presentación.
- ✅ Presentación validada sin desbordes visuales.
- ⏳ Preparar y practicar la defensa oral individual.

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
