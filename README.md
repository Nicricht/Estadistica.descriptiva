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

## Bases de análisis y calidad de datos

- Base original: **106.555 registros y 28 columnas**.
- Pregrado para análisis de personas, edad y “Acero/Algoritmo”: **101.093 matrículas**.
- Pregrado con arancel > $0 para análisis de precio: **101.067 matrículas**.
- Registros con arancel $0 excluidos del análisis de precios: **26**.
- Ofertas académicas únicas para comparar precios: **1.273 ofertas**.
- Duplicados completos: **0**.
- Los valores nulos se concentran en variables de acreditación que no son necesarias para responder las tres preguntas.

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
Para operacionalizar la expresión **“sustantivamente más caro que la mayoría”**, el proyecto define un criterio reproducible: **percentil 90 (P90)**, calculado con `quantile(0.90)`. Esta decisión metodológica usa percentiles trabajados en el Laboratorio 4 del profesor.

- P90: **$4.106.400**.
- Ofertas sobre P90: **128 de 1.273 (10,1%)**.
- CRUCH: **73**; privadas: **55**.
- Concepción: **123**; Biobío: **5**.
- Salud: **38**; Tecnología: **38**.
- Duración mediana: **10 semestres** en ofertas altas vs. **5** en el resto.

El proyecto **no utiliza RIC ni la regla Q3 + 1,5 × RIC** en la respuesta final de la Pregunta 3.

## Contenidos estadísticos realmente presentes en el notebook

El notebook actual utiliza únicamente herramientas que aparecen en su desarrollo visible:

- carga con `read_excel()`, revisión con `head()`, `shape` e `info()`;
- control de calidad con nulos, duplicados completos y filtro de aranceles mayores que $0;
- población, muestra y clasificación de variables;
- frecuencia absoluta y relativa;
- frecuencia acumulada con `cumsum()` en intervalos ordenados de edad y arancel;
- agrupación de intervalos con `pd.cut()`;
- gráficos de barras y comparaciones con `subplots()`;
- media, mediana y moda;
- percentiles con `quantile()`;
- `groupby()`, `agg()` y `crosstab()`;
- rango, desviación estándar y coeficiente de variación;
- `isin()` para filtros de grupos;
- **P90** como criterio reproducible de la Pregunta 3.

No se declara en la presentación el uso de gráficos o funciones que el notebook actual no ejecuta.

## PowerPoint oficial

El repositorio tiene **una sola presentación oficial**:

`presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx`

La versión actual sigue la lógica visual mostrada por el profesor: una idea principal por diapositiva, gráficos o tarjetas grandes, interpretación breve y detalle técnico en anexos.

Estructura:

- **14 diapositivas de exposición principal**.
- **3 anexos de defensa individual**.
- **17 diapositivas en total**.

La presentación se genera únicamente desde:

`presentacion/generar_presentacion_profesor.py`

El workflow oficial es:

`.github/workflows/generar_presentacion.yml`

## Alineación con la pauta

La presentación y el notebook mantienen las tres preguntas obligatorias. Para cada resultado se busca la secuencia:

**pregunta → herramienta → cálculo → resultado → interpretación → límite de lo que se puede concluir**.

La Pregunta 3 conserva P90 como **decisión metodológica final del proyecto**. Un documento maestro interno anterior propuso IQR/Tukey como una posible estrategia, pero esa propuesta no corresponde al desarrollo final acordado ni a una técnica enseñada en los laboratorios revisados. Para evitar atribuir a la pauta una fórmula que no hemos verificado como obligatoria, el repositorio ya no afirma que la evaluación imponga IQR ni que imponga P90: simplemente documenta y defiende el criterio elegido, P90.

## Contexto regional

La documentación conserva contexto adicional sobre ENADEL, Huachipato, fortalecimiento industrial, manufactura avanzada e Industria 4.0. Ese material se mantiene como **contexto e hipótesis de investigación**, pero no domina la presentación principal, que se concentra en los resultados descriptivos de 2021.

## Hallazgos secundarios

- Industria y manufactura: **11,10%** de la matrícula.
- Digital y TIC: **3,33%**.
- Automatización y robótica: **2,58%**.
- Energía, sustentabilidad y biotecnología: **1,02%**.
- Mujeres en Digital y TIC: **11,50%**.
- Mujeres en Automatización y robótica: **5,79%**.

## Estado

- ✅ Un único notebook oficial: `notebooks/Estadistica_Descriptiva_Biobio.ipynb`.
- ✅ Preguntas obligatorias 1, 2 y 3 preservadas.
- ✅ Control explícito de nulos y duplicados completos.
- ✅ Frecuencias acumuladas incorporadas donde corresponde.
- ✅ Pregunta 3 resuelta con P90, sin RIC ni fórmula adicional.
- ✅ Dispersión: rango, desviación estándar y coeficiente de variación.
- ✅ Un único PowerPoint oficial, con 14 diapositivas principales + 3 anexos.
- ✅ Anexo de herramientas limitado a funciones y gráficos realmente presentes en el notebook.
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
