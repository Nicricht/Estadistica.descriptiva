# Auditoría final del notebook contra los laboratorios del profesor

Fecha: 26-09-2026

## Objetivo

Revisar que el notebook principal use una forma de desarrollo coherente con los laboratorios entregados por el profesor: pregunta, código visible, resultado e interpretación.

## Cambios realizados

### 1. Tablas de frecuencia

AREA CONOCIMIENTO es una variable cualitativa nominal.

Por eso la tabla conserva:
- frecuencia absoluta;
- frecuencia relativa.

Se eliminan las frecuencias acumuladas para esta variable.

Las frecuencias acumuladas se mantienen solamente cuando existe un orden, por ejemplo en variables cuantitativas agrupadas en intervalos.

### 2. Medidas de tendencia central

El desarrollo se separó por variable y se calcula de forma directa:
- media;
- mediana.

Cada resultado queda seguido por su interpretación.

### 3. Medidas de dispersión

El Laboratorio 5 trabaja:
- rango;
- desviación estándar;
- coeficiente de variación.

El notebook queda alineado con esas tres medidas. Se eliminan del bloque general la varianza y el RIC.

### 4. Clasificación Del acero al algoritmo

Se eliminó la clasificación basada en búsquedas largas con str.contains().

Ahora:
1. se crean listas explícitas de carreras;
2. se utiliza isin() para seleccionar las carreras;
3. se asigna cada lista a una familia;
4. se construyen los bloques Motores productivos y Capacidades transformadoras.

isin() aparece en el material del profesor como herramienta de filtrado.

Resultado:
- Motores productivos: **20.368 matrículas, 20,15%**.
- Capacidades transformadoras: **7.000 matrículas, 6,92%**.
- Relación aproximada: **2,9 a 1**.

### 5. Pregunta 1

Se utiliza:
- groupby();
- agg(['count', 'median']);
- sort_values();
- gráfico de barras.

La mediana es el criterio para comparar el arancel entre áreas.

### 6. Pregunta 2

Se eliminó pd.crosstab().

Ahora se utiliza:
- groupby();
- count, mean y median;
- frecuencias absolutas;
- frecuencias relativas;
- gráficos de barras.

Se comparan especialmente los grupos de 15 a 19 años y 40 años o más.

Resultados:
- 15 a 19: CRUCH 46,24%; IP 19,30%.
- 40 o más: IP 52,93%; CRUCH 10,88%.

### 7. Pregunta 3

Se reemplazó el criterio Q3 + 1,5 × RIC por un criterio basado en percentiles.

**Criterio:** oferta con arancel superior al Percentil 90.

Resultados:
- Percentil 90: **$4.106.400**.
- Ofertas sobre P90: **128 de 1.273**, aproximadamente **10,1%**.
- Universidades CRUCH: **73**.
- Universidades privadas: **55**.
- Concepción: **123**.
- Biobío: **5**.
- Salud: **38** ofertas altas.
- Tecnología: **38** ofertas altas.
- Duración mediana de ofertas altas: **10 semestres**.
- Duración mediana del resto: **5 semestres**.

## Validación técnica

Se ejecutó una copia equivalente de la versión final con el Excel real:

- Celdas de código: **51**
- Celdas ejecutadas: **51**
- Errores: **0**

## Criterio de cierre

El notebook conserva la investigación creativa “Del acero al algoritmo”, pero la forma de llegar a los resultados se acerca al estilo de los laboratorios del profesor:

**pregunta → código corto y visible → resultado → interpretación.**
