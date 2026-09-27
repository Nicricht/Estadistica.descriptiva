# Criterio metodológico

## Tema definitivo

**DEL ACERO AL ALGORITMO**

Pregunta central:

**¿Desde qué base de capital humano parte el Biobío para transformar su histórica vocación industrial hacia una economía de manufactura avanzada e Industria 4.0?**

El análisis es descriptivo. La base 2021 funciona como una fotografía o línea base; no permite demostrar causalidad ni evolución temporal por sí sola.

## Tres bases de trabajo

### 1. Matrículas de pregrado

Se utilizan cuando la pregunta describe personas, carreras o estructura formativa:
- edad;
- género;
- tipo de institución;
- área del conocimiento;
- clasificación “Del acero al algoritmo”.

Base: **101.093 matrículas de pregrado**.

Los 26 registros con arancel $0 se mantienen aquí porque el precio no es necesario para estos análisis.

### 2. Matrículas con precio válido

Se utilizan para describir aranceles asociados a matrículas.

Base: **101.067 matrículas**, después de excluir únicamente los 26 registros de pregrado con arancel registrado en $0.

No se interpreta $0 como gratuidad porque la base no entrega esa explicación.

### 3. Ofertas académicas únicas

Se utilizan cuando la pregunta compara cuánto cuesta una carrera u oferta.

Una oferta se identifica mediante:
- institución;
- carrera;
- comuna de sede;
- modalidad;
- jornada;
- duración total;
- valor de matrícula;
- valor de arancel.

Con este criterio se obtienen **1.273 ofertas académicas únicas**.

La razón es simple: si una carrera tiene 500 estudiantes, no corresponde contar su precio 500 veces al responder cuánto cuesta una oferta académica.

## Hallazgo “Del acero al algoritmo”

Sobre 101.093 matrículas de pregrado:

- Motores productivos: **20.368 (20,15%)**.
- Capacidades transformadoras: **7.000 (6,92%)**.
- Otros campos: **73.725 (72,93%)**.
- Relación aproximada: **2,9 : 1**.

Interpretación permitida:

> En la fotografía educativa de 2021, el componente formativo asociado a motores productivos tenía un peso cercano a tres veces el componente clasificado como capacidades transformadoras.

No demuestra déficit de profesionales ni atraso de la educación.

## Pregunta obligatoria 1 — Áreas y arancel

Unidad: **oferta académica única**.

Criterio: **mediana del arancel por área**, porque es menos sensible a valores extremos.

- Mediana global: **$2.030.000**.
- Derecho: **$3.586.000**.
- Ciencias Básicas: **$3.290.000**.
- Agropecuaria: **$2.981.500**.

Se calculan también percentiles y cantidad de ofertas por área.

## Pregunta obligatoria 2 — Edad e institución

Unidad: **matrícula de pregrado**.

Se estudia asociación, no causalidad.

- 15–19 años: CRUCH **46,24%**, IP **19,30%**.
- 40 años o más: IP **52,93%**, CRUCH **10,88%**.

## Pregunta obligatoria 3 — Arancel sustantivamente alto

Unidad: **oferta académica única**.

Criterio final del proyecto: **percentil 90 (P90)**, calculado con `quantile(0.90)`.

Se eligió P90 para transformar la expresión “sustantivamente alto” en un umbral reproducible usando una herramienta trabajada en el Laboratorio 4. Un borrador interno anterior propuso IQR/Tukey; esa propuesta queda descartada y no se presenta como requisito confirmado de la pauta.

- P90 ≈ **$4.106.400**.
- Ofertas sobre P90: **128 de 1.273 (10,1%)**.
- CRUCH: **73**.
- Privadas: **55**.
- Concepción: **123**.
- Biobío: **5**.
- Salud: **38**.
- Tecnología: **38**.
- Duración mediana del grupo alto: **10 semestres**.
- Duración mediana del resto: **5 semestres**.

## Regla de interpretación

Se pueden afirmar diferencias, concentraciones y asociaciones observadas.

No se debe afirmar causalidad cuando la base no la identifica.
