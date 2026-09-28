from pathlib import Path
import json

NB = Path('notebooks/Estadistica_Descriptiva_Biobio.ipynb')
nb = json.loads(NB.read_text(encoding='utf-8'))

nuevo_inicio = """# DEL ACERO AL ALGORITMO
## Estadística Descriptiva aplicada a la Educación Superior del Biobío

**Base de datos:** Matrículas de Educación Superior de la Región del Biobío, 2021.

### Pregunta central
**¿Desde qué base de capital humano parte el Biobío para transformar su histórica vocación industrial hacia una economía de manufactura avanzada e Industria 4.0?**

### ¿Qué significa el título “Del acero al algoritmo”?

El título funciona como una **metáfora del problema que queremos estudiar**.

- **“Acero”** representa la base productiva e industrial del Biobío y, dentro de este trabajo, se relaciona con los **motores productivos**: industria y manufactura, construcción e infraestructura, logística y puertos, forestal y madera, pesca y acuicultura, y agroalimentación.
- **“Algoritmo”** representa las **capacidades transformadoras** asociadas a una economía más tecnológica: Digital y TIC, automatización y robótica, y energía, sustentabilidad y biotecnología.

La idea **no es afirmar que el Biobío esté abandonando su industria ni demostrar que ya exista una transición causada por la tecnología**. Con esta base solo observamos una fotografía de la matrícula de educación superior de 2021. Por eso, el título plantea una pregunta de análisis: **qué peso tienen la formación vinculada a la base productiva y las capacidades tecnológicas que podrían complementarla**.

En simple, el proyecto busca responder: **¿con qué formación de capital humano contaba el Biobío en 2021 para combinar su identidad productiva con nuevas capacidades tecnológicas?**

El desarrollo se organiza desde la preparación de la base hasta la interpretación de los resultados, manteniendo como foco las variables y preguntas definidas para el análisis.
"""

if not nb.get('cells') or nb['cells'][0].get('cell_type') != 'markdown':
    raise RuntimeError('La primera celda del notebook no es Markdown.')

nb['cells'][0]['source'] = nuevo_inicio.splitlines(keepends=True)
NB.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('Título explicado en la primera celda del notebook.')
