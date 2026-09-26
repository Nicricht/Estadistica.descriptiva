# Auditoría final del notebook contra los laboratorios del profesor y la pauta

Fecha: 26-09-2026

## Resultado general

El notebook principal fue revisado tomando como referencia los laboratorios del profesor y los requisitos del trabajo práctico.

## Correcciones realizadas

### 1. Estructura
Se mantiene el patrón:
**pregunta → código → resultado → interpretación**.

### 2. Clasificación de EDAD
Se ajustó a **cuantitativa continua** para mantener el mismo criterio utilizado por el profesor en sus laboratorios.

### 3. Calidad de datos
Se agregó una revisión simple de:
- filas y columnas;
- valores nulos;
- filas duplicadas;
- aranceles registrados en $0.

Resultados:
- Base original: 106.555 filas.
- Duplicados completos: 0.
- Valores nulos: 3.715 en PERIODO DE ACREDITACION y 3.715 en AÑOS DE ACREDITACION.
- Aranceles $0 en la base original: 490.

### 4. Separación correcta de bases
Se corrigió un problema metodológico importante.

Ahora:
- **d** = pregrado completo: 101.093 matrículas.
- **d_precio** = pregrado con arancel > $0: 101.067 matrículas.
- Solo se excluyen 26 registros de pregrado cuando el cálculo realmente estudia precios.

Edad, institución y ADN profesional usan las 101.093 matrículas.

### 5. Frecuencias acumuladas
Se corrigió la tabla de AREA CONOCIMIENTO. La frecuencia acumulada ahora se calcula después de ordenar las categorías.

### 6. Intervalos de edad
Se cambió a **10 intervalos**, siguiendo el patrón del laboratorio de gráficos del profesor.

### 7. Pregunta 1
La tabla incluye cantidad de ofertas, mediana, Q1, Q3 y RIC.

### 8. Pregunta 2
Se utilizan las 101.093 matrículas de pregrado.

Resultados extremos:
- 15 a 19 años: CRUCH 46,24%; IP 19,30%.
- 40 años o más: IP 52,93%; CRUCH 10,88%.

### 9. Pregunta 3
Además del criterio RIC, se agregaron:
- tipo de institución;
- área del conocimiento;
- provincia;
- duración de la carrera.

Hallazgos:
- límite superior: $4.026.000;
- 135 de 1.273 ofertas sobre el límite;
- 73 CRUCH y 62 privadas;
- 129 en Concepción y 6 en Biobío;
- Salud y Tecnología: 39 ofertas altas cada una;
- duración mediana: 10 semestres en ofertas altas vs 5 semestres en el resto.

También se agregó un gráfico de las carreras con mayor arancel mediano.

## Validación técnica

Se ejecutó una copia auditada del notebook de principio a fin con el Excel real.

- Celdas de código: **41**
- Celdas ejecutadas: **41**
- Errores: **0**

## Tema creativo

Se mantiene una sola idea:

# Del acero al algoritmo

- Motores productivos: 20.368 matrículas, **20,15%**.
- Capacidades transformadoras: 7.000 matrículas, **6,92%**.
- Relación aproximada: **2,9 a 1**.

La conclusión sigue siendo descriptiva. No se afirma déficit de profesionales ni causalidad.

## Estado

El notebook ya está estructural y metodológicamente preparado para pasar a la presentación y la defensa oral.
