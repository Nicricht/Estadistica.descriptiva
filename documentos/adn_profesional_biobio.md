# Metodología — ADN profesional del Biobío

## 1. Propósito

Construir una lectura regional de la base de matrículas 2021 que permita describir qué capital humano se está formando en carreras potencialmente vinculadas con los motores productivos del Biobío y con capacidades de transformación tecnológica.

La clasificación **no es una taxonomía oficial de carreras** y no mide demanda laboral. Es una herramienta analítica diseñada para el trabajo de Estadística Descriptiva.

## 2. Fundamento regional

El Gobierno Regional del Biobío identifica de forma recurrente sectores productivos como pesca, forestal/maderero, agricultura, industria/manufactura, construcción, logística-transporte-puertos y actividades vinculadas a energía y comercio. La estrategia regional de ciencia, tecnología, conocimiento e innovación también plantea fortalecer la innovación en sectores tractores y conectar educación e investigación con servicios tecnológicos.

Fuentes:
- https://gorebiobio.cl/wp-content/uploads/2025/01/Ejes-Estrategicos.pdf
- https://actas.gorebiobio.cl/actasfiles/Acta-Sesi%C3%B3n-Ordinaria-N%C2%B021-de-fecha-08-11-2023.pdf
- https://gorebiobio.cl/estrategia-regional-de-desarrollo-2015-2030/

## 3. Familias creadas

### Motores productivos
1. Industria y manufactura
2. Construcción e infraestructura
3. Logística y puertos
4. Forestal y madera
5. Pesca y acuicultura
6. Agroalimentario

### Capacidades transformadoras
7. Digital y TIC
8. Automatización y robótica
9. Energía, sustentabilidad y biotecnología

Las carreras que no poseen una relación suficientemente clara según su nombre se clasifican como **Otros campos**.

## 4. Criterio de clasificación

Se utiliza `NOMBRE CARRERA` y un conjunto transparente de palabras clave.

Ejemplos:
- `INGENIERIA CIVIL INDUSTRIAL` → Industria y manufactura.
- `INGENIERIA FORESTAL` → Forestal y madera.
- `TECNICO EN LOGISTICA MARITIMA PORTUARIA` → Logística y puertos.
- `INGENIERIA CIVIL INFORMATICA` → Digital y TIC.
- `INGENIERIA CIVIL EN AUTOMATIZACION` → Automatización y robótica.
- `INGENIERIA EN ENERGIA Y SUSTENTABILIDAD AMBIENTAL` → Energía, sustentabilidad y biotecnología.
- `INGENIERIA EN BIOTECNOLOGIA MARINA Y ACUICULTURA` → Pesca y acuicultura, porque se prioriza el sector específico.

El código completo está en el notebook y asigna cada carrera a **una sola familia** para evitar doble conteo.

## 5. Resultados sobre 101.067 matrículas

| Familia | Matrículas | % del total | % mujeres | Edad mediana |
|---|---:|---:|---:|---:|
| Industria y manufactura | 11.221 | 11,10% | 17,17% | 23 |
| Construcción e infraestructura | 6.916 | 6,84% | 27,30% | 23 |
| Digital y TIC | 3.365 | 3,33% | 11,50% | 22 |
| Automatización y robótica | 2.608 | 2,58% | 5,79% | 22 |
| Energía, sustentabilidad y biotecnología | 1.027 | 1,02% | 44,50% | 23 |
| Logística y puertos | 1.028 | 1,02% | 42,70% | 24 |
| Agroalimentario | 863 | 0,85% | 46,93% | 23 |
| Forestal y madera | 171 | 0,17% | 33,33% | 22 |
| Pesca y acuicultura | 151 | 0,15% | 57,62% | 22 |

Totales por bloque:
- **Motores productivos:** 20.350 matrículas, **20,14%**.
- **Capacidades transformadoras:** 7.000 matrículas, **6,93%**.
- **Nueve familias estratégicas:** 27.350 matrículas, **27,07%**.
- **Otros campos:** 73.717 matrículas, **72,94%**.

## 6. Hallazgos que sostienen el relato

### A. El ADN industrial existe, pero domina sobre el ADN transformador
Industria y manufactura por sí sola representa 11,10% de toda la base, mientras Digital + Automatización + Energía/Sustentabilidad/Biotecnología suman 6,93%.

### B. La transformación tecnológica presenta una fuerte brecha de género
Solo 11,50% de las matrículas clasificadas como Digital y TIC corresponden a mujeres. En Automatización y robótica el porcentaje baja a 5,79%.

### C. Las provincias no muestran exactamente el mismo perfil
Las capacidades transformadoras representan:
- Concepción: 6,77% de su matrícula.
- Biobío: 7,61%.
- Arauco: 8,55%.

Sin embargo, Arauco no registra matrículas clasificadas como Digital y TIC en la base 2021; su componente transformador se concentra principalmente en Automatización/Robótica y Sustentabilidad.

### D. Los precios extremos no son exclusivos del ADN estratégico
De las 135 ofertas sobre el umbral IQR de $4.026.000:
- 25 pertenecen a motores productivos.
- 10 a capacidades transformadoras.
- 100 a otros campos.

## 7. Conclusión metodológicamente válida

**El Biobío forma una base importante de talento industrial, pero las capacidades asociadas a transformación digital, automatización y sustentabilidad representan una porción mucho menor de la matrícula y exhiben diferencias marcadas de género y composición territorial.**

No se afirma que exista déficit laboral ni que la región esté formando “mal” a sus estudiantes. Para responder eso harían falta datos de empleo, vacantes, salarios y demanda de competencias.
