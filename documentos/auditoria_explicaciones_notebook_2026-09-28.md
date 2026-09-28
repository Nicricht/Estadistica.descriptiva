# Auditoría final de explicaciones del notebook

Fecha: 2026-09-28  
Notebook revisado: `notebooks/Estadistica_Descriptiva_Biobio.ipynb`

## Alcance

Se revisaron una por una las 39 celdas de código, sus salidas y las celdas Markdown asociadas. El notebook contiene 107 celdas en total. Las 39 celdas de código están ejecutadas y no presentan errores de ejecución.

## 0. Carga y preparación de la base — OK

- Carga con `pandas.read_excel()`: explicación consistente con el código.
- `head()`, `shape` e `info()`: explicaciones ajustadas a los resultados observados.
- Control de calidad: 0 duplicados completos y 3.715 valores faltantes en cada una de las dos variables de acreditación.
- Filtro de pregrado: 101.093 matrículas.
- Arancel positivo: 101.067 registros; se aclaró que la base no permite conocer la causa de los 26 valores cero.
- Ofertas únicas: 1.273; se explicó por qué esta unidad evita ponderar un mismo precio por número de estudiantes.

## 1. Población, base de análisis y variables — OK

- Se precisó que no se extrajo una muestra aleatoria adicional.
- Se distingue la unidad de análisis de matrícula de la unidad de análisis de oferta académica única.
- Se revisó la clasificación de variables y se agregó una justificación breve para cada una.
- La edad se presenta como continua conceptualmente aunque se registre en años enteros.

## 2. Descripción general — OK

- Género: 54,3% femenino y 45,7% masculino.
- Área del conocimiento: Tecnología 27,6% y Salud 24,3%; juntas suman 51,9%.
- Edad agrupada: se corrigió el segundo intervalo como mayor de 23 y hasta 29 años; los dos primeros intervalos acumulan 83,4%.
- Arancel agrupado: interpretación coherente con las frecuencias relativas y acumuladas.
- Gráficos: cada interpretación se mantiene descriptiva y no atribuye causalidad.

## 3. Medidas descriptivas — OK

- Arancel: media $3.224.895, mediana $3.133.750 y moda $3.373.000.
- Se aclaró que estas medidas generales están calculadas a nivel de matrícula con arancel positivo.
- Edad: media 24,4; mediana 23; moda 19.
- Dispersión: rango $8.133.670, desviación estándar $1.518.991 y CV 47,1%.
- Se explica el CV como relación entre desviación estándar y media, evitando depender de un umbral externo no definido.

## 4. Del acero al algoritmo — OK

- Se deja explícito que la clasificación es propia del proyecto y no oficial.
- Motores productivos: 20.368 matrículas, 20,15%.
- Capacidades transformadoras: 7.000 matrículas, 6,92%.
- Otros campos: 73.725, 72,93%.
- Razón productivas/transformadoras: 2,9 a 1.
- Las interpretaciones no convierten esta diferencia en evidencia de déficit laboral o atraso tecnológico.

## 5. Pregunta 1 — CORREGIDA Y OK

Criterio: comparar la mediana de cada área con la mediana global de las 1.273 ofertas únicas.

Se detectó y corrigió un problema de interpretación: anteriormente se nombraban solo Derecho, Ciencias Básicas y Agropecuaria como áreas sobre la mediana global. Con una mediana global de $2.030.000, también Tecnología ($2.122.000) y Salud ($2.080.000) están por encima.

La respuesta final reconoce cinco áreas sobre la mediana global:
1. Derecho: $3.586.000
2. Ciencias Básicas: $3.290.000
3. Agropecuaria: $2.981.500
4. Tecnología: $2.122.000
5. Salud: $2.080.000

La tabla bivariada por tipo de institución se mantiene como análisis complementario y no reemplaza el criterio principal basado en medianas.

## 5. Pregunta 2 — OK

- Universidades CRUCH: edad media 22,8.
- Institutos Profesionales: edad media 26,5.
- En 15–19 años: CRUCH 46,2%, privadas 24,5%, IP 19,3%, CFT 10,0%.
- En 40+ años: IP 52,9%, privadas 18,4%, CFT 17,7%, CRUCH 10,9%, convenio 0,2%.
- Se mantiene correctamente la conclusión de asociación descriptiva y no causalidad.

## 5. Pregunta 3 — OK

- P90: $4.106.400.
- Ofertas sobre P90: 128, equivalentes a 10,1%.
- Las 128 ofertas pertenecen a universidades: 73 CRUCH y 55 privadas.
- Salud y Tecnología reúnen 38 ofertas cada una; juntas representan 59,4% del grupo.
- Concepción concentra 123 de las 128 ofertas, 96,1%.
- Duración mediana: 10 semestres en el grupo sobre P90 y 5 en el resto.
- Se corrigió la interpretación del ranking por carrera para dejar claro que se trata de medianas por carrera sobre las 1.273 ofertas únicas y no de que todas las ofertas individuales tengan el mismo valor.
- Medicina: 3 ofertas, mediana aproximada $7.490.000.
- Odontología: 5 ofertas, mediana $7.290.000.

## 6. Conclusiones y 7. Limitaciones — OK

Las conclusiones fueron ampliadas para responder explícitamente las tres preguntas y diferenciar las unidades de análisis.

Las limitaciones indican:
- un solo año, 2021;
- clasificación propia del proyecto;
- análisis descriptivo, sin causalidad;
- provincia de sede no equivale a residencia del estudiante;
- ausencia de salarios, vacantes, productividad, demanda laboral y motivaciones de elección.

## Revisión de estilo

Se eliminaron expresiones tutoriales o impropias de un informe, entre ellas:
- “Según el laboratorio”
- “según el profesor”
- “Esta celda...”
- “Aquí usamos...”
- “Cómo recordarlo”
- “Explicación:” como fórmula repetitiva

Las interpretaciones quedaron redactadas como parte de un informe académico del grupo: método, resultado, significado, conclusión y limitación cuando corresponde.

## Validación técnica final

- 107 celdas totales.
- 39 celdas de código.
- 39 celdas de código ejecutadas.
- 0 errores de ejecución.
