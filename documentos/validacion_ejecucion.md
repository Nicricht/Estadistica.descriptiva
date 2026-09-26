# Validación de ejecución

**Fecha:** 26-09-2026

## Resultado técnico

El notebook final fue ejecutado de principio a fin con la base real y la validación automática terminó correctamente.

- Registros originales: **106.555**
- Matrículas de pregrado: **101.093**
- Matrículas de pregrado con arancel mayor que 0: **101.067**

## Medidas descriptivas del arancel

- Media: **$3.224.895**
- Mediana: **$3.133.750**
- Moda: **$3.373.000**
- Percentil 25: **$1.988.000**
- Percentil 75: **$4.261.900**
- Rango: **$8.133.670**
- Desviación estándar: **$1.518.991**
- Coeficiente de variación: **47,1%**

## Pregunta 1

Medianas de arancel más altas por área:
- Agropecuaria: **$4.751.078**
- Derecho: **$4.250.000**
- Salud: **$4.243.207**
- Ciencias Básicas: **$4.144.870**

## Pregunta 2

Entre 15 y 19 años:
- CRUCH: **46,2%**
- Institutos Profesionales: **19,3%**

Entre 40 años o más:
- Institutos Profesionales: **52,9%**
- CRUCH: **10,9%**

## Pregunta 3

Se usa **P75 = $4.261.900** como referencia, porque el Laboratorio 4 trabaja explícitamente `quantile(0.75)`.

Entre las carreras cuya mediana supera P75 aparecen:
- Odontología: **$7.625.300**
- Medicina: **$7.490.000**
- Licenciatura en Medicina: **$6.750.000**
- Ingeniería Civil de Minas: **$6.050.705**

## Regla final

No se incorporan técnicas fuera de los laboratorios del profesor.
