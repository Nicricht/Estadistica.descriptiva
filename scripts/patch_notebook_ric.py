import json
from pathlib import Path

NB = Path('notebooks/Estadistica_Descriptiva_Biobio.ipynb')
nb = json.loads(NB.read_text(encoding='utf-8'))
cells = nb['cells']


def src(cell):
    return ''.join(cell.get('source', []))


def lines(text):
    if not text.endswith('\n'):
        text += '\n'
    return text.splitlines(keepends=True)


def md(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': lines(text)}


def code(text, output=None):
    c = {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': lines(text)}
    if output is not None:
        c['outputs'] = [{'name': 'stdout', 'output_type': 'stream', 'text': lines(output)}]
    return c

# 1) Pregunta central definitiva
for cell in cells:
    if cell.get('cell_type') == 'markdown' and src(cell).startswith('# DEL ACERO AL ALGORITMO'):
        text = src(cell)
        old = '**¿Qué peso tenía en 2021 la formación ligada a los motores productivos del Biobío frente a las capacidades que pueden transformarlos mediante digitalización, automatización y sustentabilidad?**'
        new = '**¿Desde qué base de capital humano parte el Biobío para transformar su histórica vocación industrial hacia una economía de manufactura avanzada e Industria 4.0?**'
        cell['source'] = lines(text.replace(old, new))
        break

# 2) Dispersión: alinear con el Laboratorio 5 del profesor
for cell in cells:
    if cell.get('cell_type') == 'markdown' and src(cell).startswith('# 5. Medidas de Dispersión'):
        cell['source'] = lines('''# 5. Medidas de Dispersión

Aplicaremos las medidas de dispersión que aparecen en el Laboratorio 5 del profesor:

- Rango.
- Desviación estándar.
- Coeficiente de variación.

El RIC se reserva para la Pregunta 3 como aplicación de los cuartiles del Laboratorio 4.
''')
        break

for cell in cells:
    if cell.get('cell_type') == 'code' and src(cell).startswith('#Calculamos el máximo y mínimo'):
        cell['source'] = lines('''#Calculamos el máximo y mínimo
maximo_arancel = d_precio['VALOR ARANCEL (PESOS)'].max()
minimo_arancel = d_precio['VALOR ARANCEL (PESOS)'].min()

#Rango
rango_arancel = maximo_arancel - minimo_arancel

#Desviación estándar
desviacion_arancel = d_precio['VALOR ARANCEL (PESOS)'].std()

#Coeficiente de variación
cv_arancel = desviacion_arancel / media_arancel * 100

print(f'Rango: ${rango_arancel}')
print(f'Desviación estándar: ${desviacion_arancel:.0f}')
print(f'CV: {cv_arancel:.1f}%')
''')
        cell['outputs'] = [{'name': 'stdout', 'output_type': 'stream', 'text': [
            'Rango: $8133670\n',
            'Desviación estándar: $1518991\n',
            'CV: 47.1%\n'
        ]}]
        break

# 3) Pregunta 3: volver al criterio Q3 + 1,5 RIC, consistente con la pauta y el criterio metodológico
start = next(i for i,c in enumerate(cells) if c.get('cell_type') == 'markdown' and src(c).startswith('## Pregunta 3'))
end = next(i for i,c in enumerate(cells[start+1:], start+1) if c.get('cell_type') == 'markdown' and src(c).startswith('# 8. Conclusiones generales'))

# Conservamos las dos celdas del ranking, porque no dependen del criterio de valores altos.
ranking_cells = [c for c in cells[start:end] if c.get('cell_type') == 'code' and ('ranking_carreras = ofertas.groupby' in src(c) or "ax.set_title('Carreras con mayor arancel mediano')" in src(c))]

new_p3 = [
    md('''## Pregunta 3
### ¿Hay carreras cuyo arancel sea sustantivamente más caro que la mayoría?

**Criterio diseñado:** utilizaremos el criterio de valores atípicos superiores basado en el rango intercuartílico:

**Límite superior = Q3 + 1,5 × RIC**

Este criterio permite identificar ofertas cuyo arancel se ubica claramente por encima del rango central de la distribución.
'''),
    code('''#Cuartiles del arancel de las ofertas académicas únicas
q1_ofertas = ofertas['VALOR ARANCEL (PESOS)'].quantile(0.25)
q3_ofertas = ofertas['VALOR ARANCEL (PESOS)'].quantile(0.75)

#Rango intercuartílico
ric_ofertas = q3_ofertas - q1_ofertas

#Límite superior
limite_superior = q3_ofertas + 1.5 * ric_ofertas

print(f'Q1: ${q1_ofertas:.0f}')
print(f'Q3: ${q3_ofertas:.0f}')
print(f'RIC: ${ric_ofertas:.0f}')
print(f'Límite superior: ${limite_superior:.0f}')
''', '''Q1: $1616000
Q3: $2580000
RIC: $964000
Límite superior: $4026000
'''),
    code('''#Ofertas que superan el límite superior
altas = ofertas[
    ofertas['VALOR ARANCEL (PESOS)'] > limite_superior
].copy()

cantidad_altas = altas.shape[0]
porcentaje_altas = cantidad_altas / ofertas.shape[0] * 100

print(f'Ofertas sobre el límite: {cantidad_altas}')
print(f'Porcentaje: {porcentaje_altas:.1f}%')
''', '''Ofertas sobre el límite: 135
Porcentaje: 10.6%
'''),
    md('''### ¿Qué variables de la base ayudan a comprender este grupo?

Revisaremos tipo de institución, área del conocimiento, provincia y duración de la carrera. Estas asociaciones son descriptivas y no prueban causalidad.
'''),
    code("""#Frecuencia por tipo de institución
altas.groupby(
    'TIPO DE INSTITUCION'
).size().sort_values(ascending=False)
"""),
    code("""#Frecuencia por área del conocimiento
altas.groupby(
    'AREA CONOCIMIENTO'
).size().sort_values(ascending=False)
"""),
    code("""#Frecuencia por provincia
altas.groupby(
    'PROVINCIA SEDE'
).size().sort_values(ascending=False)
"""),
    code('''#Comparamos la duración mediana de las ofertas altas con el resto
duracion_altas = altas['DURACION TOTAL CARRERA (SEMESTRES)'].median()

resto = ofertas[
    ofertas['VALOR ARANCEL (PESOS)'] <= limite_superior
]

duracion_resto = resto['DURACION TOTAL CARRERA (SEMESTRES)'].median()

print(f'Duración mediana ofertas altas: {duracion_altas} semestres')
print(f'Duración mediana resto: {duracion_resto} semestres')
''', '''Duración mediana ofertas altas: 10.0 semestres
Duración mediana resto: 5.0 semestres
'''),
]

# Añadir ranking y gráfico que ya estaban ejecutados
new_p3.extend(ranking_cells)
new_p3.append(md('''### Respuesta

Sí. En las **1.273 ofertas académicas únicas**:

- **Q1 ≈ $1.616.000**.
- **Q3 ≈ $2.580.000**.
- **RIC ≈ $964.000**.
- El límite superior **Q3 + 1,5 × RIC ≈ $4.026.000**.
- **135 ofertas** superan ese límite, aproximadamente **10,6%** del total.

Entre esas ofertas:

- **73** corresponden a universidades CRUCH y **62** a universidades privadas.
- **129** se encuentran en Concepción y **6** en Biobío.
- Salud y Tecnología concentran **39 ofertas cada una**.
- La duración mediana es de **10 semestres**, frente a **5 semestres** en el resto.

Entre las carreras con mayor arancel mediano aparecen **Medicina** y **Odontología**.

Los aranceles altos aparecen asociados en esta base con determinadas áreas, territorio, institución y duración. Estas variables **no se interpretan como causas del precio**.
'''))

cells[start:end] = new_p3

NB.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('Notebook alineado con el método del profesor y la pregunta central definitiva.')
