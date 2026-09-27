import json
from pathlib import Path

NOTEBOOK = Path('notebooks/Estadistica_Descriptiva_Biobio.ipynb')

nb = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
cells = nb['cells']


def source_text(cell):
    return ''.join(cell.get('source', []))


def source_lines(text):
    lines = text.splitlines(keepends=True)
    if text and (not lines or not lines[-1].endswith('\n')):
        lines[-1] = lines[-1] + '\n'
    return lines


# 1) Control explícito de calidad de datos: nulos y duplicados completos.
quality_id = 'rubrica-calidad-datos'
if not any(c.get('id') == quality_id for c in cells):
    info_idx = next(i for i, c in enumerate(cells) if c.get('cell_type') == 'code' and 'df.info()' in source_text(c))
    insert_at = info_idx + 1
    if insert_at < len(cells) and cells[insert_at].get('cell_type') == 'markdown':
        insert_at += 1

    quality_code = {
        'cell_type': 'code',
        'execution_count': None,
        'id': quality_id,
        'metadata': {},
        'outputs': [],
        'source': source_lines("""#Controlamos duplicados completos y valores nulos\nduplicados_completos = int(df.duplicated().sum())\nnulos_por_columna = df.isna().sum()\nnulos_relevantes = nulos_por_columna[nulos_por_columna > 0]\n\nprint('Duplicados completos:', duplicados_completos)\nprint('\\nValores nulos por columna:')\nprint(nulos_relevantes)\n"""),
    }
    quality_md = {
        'cell_type': 'markdown',
        'id': 'rubrica-calidad-datos-explicacion',
        'metadata': {},
        'source': source_lines("""**Control de calidad:** comprobamos de forma explícita los duplicados completos y los valores nulos. La base tiene **0 filas completamente duplicadas**. Los valores faltantes se concentran en variables de acreditación, que no son necesarias para responder las tres preguntas del trabajo. Más adelante, para el análisis de precios, también excluimos los **26 registros con arancel igual a $0**.\n"""),
    }
    cells[insert_at:insert_at] = [quality_code, quality_md]

# 2) Frecuencias acumuladas donde tienen sentido: intervalos ordenados de edad y arancel.
for cell in cells:
    if cell.get('cell_type') != 'code':
        continue
    src = source_text(cell)
    if '#Agrupamos la edad en intervalos' in src:
        cell['source'] = source_lines("""#Agrupamos la edad en intervalos\nd['Intervalos_edad'] = pd.cut(\n    d['EDAD'],\n    bins=10,\n    include_lowest=True,\n    precision=0\n)\n\n#Calculamos las frecuencias\ncuenta_edad = d.groupby(\n    'Intervalos_edad',\n    observed=True\n).size()\n\ntabla_edad = pd.DataFrame({\n    'Frecuencia absoluta': cuenta_edad,\n    'Frecuencia relativa (%)': cuenta_edad/d.shape[0] * 100\n})\n\n#Como los intervalos están ordenados, agregamos las frecuencias acumuladas\ntabla_edad['Frecuencia acumulada'] = tabla_edad['Frecuencia absoluta'].cumsum()\ntabla_edad['Frecuencia relativa acumulada (%)'] = tabla_edad['Frecuencia relativa (%)'].cumsum()\n\nround(tabla_edad, 1)\n""")
    elif '#Agrupamos los aranceles en intervalos' in src:
        cell['source'] = source_lines("""#Agrupamos los aranceles en intervalos\nd_precio['Intervalos_arancel'] = pd.cut(\n    d_precio['VALOR ARANCEL (PESOS)'],\n    bins=9,\n    include_lowest=True,\n    precision=0\n)\n\n#Calculamos las frecuencias\ncuenta_arancel = d_precio.groupby(\n    'Intervalos_arancel',\n    observed=True\n).size()\n\ntabla_arancel = pd.DataFrame({\n    'Frecuencia absoluta': cuenta_arancel,\n    'Frecuencia relativa (%)': cuenta_arancel/d_precio.shape[0] * 100\n})\n\n#Como los intervalos están ordenados, agregamos las frecuencias acumuladas\ntabla_arancel['Frecuencia acumulada'] = tabla_arancel['Frecuencia absoluta'].cumsum()\ntabla_arancel['Frecuencia relativa acumulada (%)'] = tabla_arancel['Frecuencia relativa (%)'].cumsum()\n\nround(tabla_arancel, 1)\n""")

# 3) Ajustamos las explicaciones para que describan exactamente las tablas actuales.
for cell in cells:
    if cell.get('cell_type') != 'markdown':
        continue
    src = source_text(cell)
    if src.startswith('**Explicación:** Como la edad es una variable cuantitativa'):
        cell['source'] = source_lines("""**Explicación:** Como la edad es una variable cuantitativa con muchos valores posibles, la agrupamos en **10 intervalos** mediante pd.cut(). Luego calculamos frecuencia absoluta, frecuencia relativa y, porque los intervalos tienen un orden natural, agregamos la **frecuencia acumulada** con cumsum(). El grupo aproximado de **17 a 23 años concentra 47,9%** de las matrículas y el siguiente, de **23 a 29 años, 35,5%**. La acumulada permite ver cuánto del total se reúne al avanzar por los intervalos de edad.\n""")
    elif src.startswith('**Explicación:** Aplicamos el mismo procedimiento al arancel'):
        cell['source'] = source_lines("""**Explicación:** Aplicamos el mismo procedimiento al arancel, agrupándolo en nueve intervalos. Calculamos frecuencia absoluta, relativa y, al tratarse de intervalos ordenados, **frecuencia acumulada** mediante cumsum(). El intervalo con mayor frecuencia está aproximadamente entre **$1,55 y $2,46 millones**, con **32,3%** de los registros. También existe una concentración importante entre aproximadamente **$3,36 y $4,26 millones (20,4%)** y entre **$4,26 y $5,17 millones (17,1%)**.\n""")

NOTEBOOK.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('Notebook alineado con la rúbrica y el material del profesor.')
