from pathlib import Path
import json

# Agrega una clasificación explícita de variables al notebook y a la presentación.
# El criterio sigue los laboratorios del profesor. En particular, el Laboratorio 1
# clasifica la edad como cuantitativa continua.

# -----------------------------------------------------------------------------
# Notebook
# -----------------------------------------------------------------------------
nb_path = Path('notebooks/Estadistica_Descriptiva_Biobio.ipynb')
nb = json.loads(nb_path.read_text(encoding='utf-8'))

variables_text = """# 1. Población, base de análisis y variables

**Población de interés:** matrículas de educación superior de la Región del Biobío durante 2021.

**Base disponible:** 106.555 registros.

**Subbase principal:** 101.093 matrículas de pregrado.

**Unidad de análisis:** para describir la matrícula se trabaja con registros de matrícula; para comparar precios entre carreras y áreas se utilizan ofertas académicas únicas. No se extrajo una muestra aleatoria adicional, sino que se trabajó con la base entregada y con subbases construidas según el objetivo de cada análisis.

## 1.1 Clasificación de las variables principales

Para organizar el análisis se clasificaron las variables principales según su naturaleza estadística. Las variables cualitativas representan categorías, mientras que las cuantitativas expresan magnitudes numéricas. A su vez, se distinguen los subtipos nominal, ordinal, discreta y continua.

| Variable | Tipo general | Subtipo | Justificación breve |
|---|---|---|---|
| GÉNERO | Cualitativa | Nominal | Presenta categorías sin un orden natural. |
| RANGO EDAD | Cualitativa | Ordinal | Sus categorías siguen un orden de menor a mayor edad. |
| TIPO DE INSTITUCIÓN | Cualitativa | Nominal | Distingue categorías de institución sin jerarquía numérica. |
| NOMBRE CARRERA | Cualitativa | Nominal | Identifica carreras como categorías sin un orden natural. |
| ÁREA DEL CONOCIMIENTO | Cualitativa | Nominal | Agrupa campos de estudio sin establecer jerarquía entre ellos. |
| PROVINCIA SEDE | Cualitativa | Nominal | Identifica territorios sin un orden estadístico. |
| EDAD | Cuantitativa | Continua | Conceptualmente mide edad sobre una escala continua, aunque en la base se registra en años enteros. |
| AÑO INGRESO | Cuantitativa | Discreta | Se registra mediante años enteros, por ejemplo 2019, 2020 o 2021. |
| DURACIÓN TOTAL CARRERA (SEMESTRES) | Cuantitativa | Continua | Se trabaja como una medida de duración y la base la expresa en semestres. |
| VALOR ARANCEL (PESOS) | Cuantitativa | Continua | Representa una magnitud monetaria sobre la que se calculan medidas descriptivas. |

**Criterio utilizado:** nominal corresponde a categorías sin orden; ordinal a categorías ordenadas; discreta a valores numéricos separados; y continua a mediciones realizadas sobre una escala numérica.
"""

changed = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') != 'markdown':
        continue
    txt = ''.join(cell.get('source', []))
    if txt.startswith('# 1. Población, muestra y variables'):
        if txt != variables_text:
            cell['source'] = variables_text.splitlines(keepends=True)
            changed = True
        break

if changed:
    nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# -----------------------------------------------------------------------------
# PowerPoint: agregar anexo 18 sin alterar la secuencia principal.
# -----------------------------------------------------------------------------
ppt_source = Path('presentacion/generar_presentacion_profesor.py')
s = ppt_source.read_text(encoding='utf-8')

slide_variables = """

s=base('ANEXO · Clasificación de variables',18,'Clasificamos las variables principales según el criterio trabajado en el Laboratorio 1.')
shape(s,.72,1.62,5.82,4.72,L,EDGE); shape(s,6.78,1.62,5.82,4.72,L,EDGE)
text(s,1.02,1.9,4.9,.38,'VARIABLES CUALITATIVAS',13.5,NAV,True)
text(s,7.08,1.9,4.9,.38,'VARIABLES CUANTITATIVAS',13.5,NAV,True)
for i,(v,t,c) in enumerate([
 ('GÉNERO','Nominal',TEAL),('RANGO EDAD','Ordinal',ORG),('TIPO DE INSTITUCIÓN','Nominal',TEAL),
 ('NOMBRE CARRERA','Nominal',TEAL),('ÁREA DEL CONOCIMIENTO','Nominal',TEAL),('PROVINCIA SEDE','Nominal',TEAL)
]):
 y=2.42+i*.58; badge(s,1.02,y,1.15,t,c); text(s,2.35,y-.02,3.72,.34,v,9.4,TXT,True)
for i,(v,t,c) in enumerate([
 ('EDAD','Continua',GRN),('AÑO INGRESO','Discreta',BLUE),('DURACIÓN TOTAL (SEMESTRES)','Continua',GRN),('VALOR ARANCEL (PESOS)','Continua',GRN)
]):
 y=2.42+i*.78; badge(s,7.08,y,1.25,t,c); text(s,8.55,y-.02,3.55,.34,v,9.4,TXT,True)
note(s,7.08,5.55,5.15,.62,'CLAVE','Nominal: sin orden · Ordinal: con orden · Discreta: valores contables · Continua: medida en una escala.',ORG)
note(s,.72,6.47,11.88,.48,'CRITERIO DEL CURSO','Seguimos el criterio de los laboratorios del profesor: por ejemplo, Edad se clasifica como cuantitativa continua.',TEAL)
"""

if 'ANEXO · Clasificación de variables' not in s:
    marker = "prs.save(OUT); print('Generado',OUT,len(prs.slides))"
    if marker not in s:
        raise RuntimeError('No se encontró el punto de inserción de la diapositiva de variables.')
    s = s.replace(marker, slide_variables + '\n' + marker)
    ppt_source.write_text(s, encoding='utf-8')

print('Clasificación de variables agregada al notebook y al generador del PowerPoint.')
