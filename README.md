# Estadística descriptiva — Educación Superior del Biobío 2021

## Objetivo

Aplicar únicamente los contenidos enseñados en los laboratorios 0 al 5 del profesor a la base de matrículas de Educación Superior del Biobío 2021.

## Regla del proyecto

**No se utiliza ninguna técnica estadística ni procedimiento de análisis que no aparezca en el material entregado por el profesor.**

## Contenidos utilizados

### Laboratorio 0 — Introducción a Pandas
- `read_excel()`
- `head()`
- `tail()`
- `shape`
- `info()`
- `value_counts()`
- filtros y `groupby()`

### Laboratorio 1 — Conceptos básicos de estadística
- población
- muestra
- variables cualitativas y cuantitativas

### Laboratorio 2 — Tablas de frecuencia
- frecuencia absoluta
- frecuencia relativa
- frecuencia acumulada
- `groupby().size()`
- `pd.cut()`
- `cumsum()`

### Laboratorio 3 — Gráficos
- barras
- `subplots()`
- títulos y etiquetas

### Laboratorio 4 — Tendencia central y percentiles
- media
- mediana
- moda
- percentiles con `quantile()`
- `describe()`
- `agg()`
- `crosstab()`

### Laboratorio 5 — Medidas de dispersión
- máximo
- mínimo
- rango
- desviación estándar
- coeficiente de variación
- `groupby()`
- `agg()`
- `isin()`

## Preguntas del trabajo

1. ¿Hay áreas del conocimiento donde las carreras sean más caras?
2. ¿Se observa relación entre edad y tipo de institución?
3. ¿Hay carreras cuyo arancel sea más alto que la mayoría?

La tercera pregunta utiliza el **percentil 75**, porque el profesor trabaja explícitamente `quantile(0.75)` en el Laboratorio 4.

## Archivo principal

`notebooks/Estadistica_Descriptiva_Biobio.ipynb`

## Material oficial del profesor

La carpeta `material_profesor/` contiene los seis laboratorios utilizados como única referencia metodológica.
