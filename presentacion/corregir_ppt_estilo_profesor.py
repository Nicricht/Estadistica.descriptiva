from __future__ import annotations

import html
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

PPT = Path("presentacion/Del_Acero_al_Algoritmo_Estilo_Profesor.pptx")

# Reemplazos por diapositiva e índice de nodo <a:t>.
# Solo cambia texto: se conserva el diseño, posiciones, tipografías y formas del PPT original.
REEMPLAZOS: dict[int, dict[int, str]] = {
    2: {
        1: "Usamos la misma base, pero cada pregunta necesita una unidad de análisis distinta.",
        10: "matrículas y estructura formativa",
        14: "matrículas con arancel mayor que $0",
        18: "precios sin repetir la misma oferta",
        19: "En simple: para comparar precios, una misma carrera no puede repetir su arancel por cada estudiante. Por eso trabajamos con 1.273 ofertas únicas.",
        20: "",
    },
    3: {
        0: "Qué herramientas usamos y para qué",
        1: "Cada herramienta del notebook corresponde a contenidos trabajados en los laboratorios del profesor.",
        5: "cuántos · porcentajes · acumulados",
        9: "valor típico o central",
        13: "posición dentro de la distribución",
        17: "rango · desviación estándar · CV",
        18: "std()",
        21: "comparar dos variables o grupos",
        23: "Idea clave: primero elegimos la herramienta, después calculamos, mostramos el resultado y finalmente lo interpretamos.",
        24: "",
    },
    4: {
        8: "En total hay más mujeres (54,3%) que hombres (45,7%); la distribución cambia según el área.",
        22: "Lectura: Tecnología (27,6%) y Salud (24,3%) concentran 51,9% de la matrícula. La base muestra el patrón, no su causa.",
        23: "",
    },
    6: {
        1: "Agrupamos carreras en 9 familias para comparar formación productiva y formación transformadora.",
        21: "Importante: esta clasificación fue creada para el trabajo. No es oficial y cada carrera aparece en una sola familia para no contarla dos veces.",
        22: "",
    },
    7: {
        1: "Comparamos cuánto pesa cada bloque dentro de la matrícula de pregrado de 2021.",
        11: "En simple: hay cerca de 2,9 matrículas productivas por cada transformadora. Es una diferencia descriptiva, no prueba un déficit profesional.",
        12: "",
    },
    8: {
        1: "Usamos 1.273 ofertas únicas y comparamos su arancel mediano por área.",
        21: "Respuesta: Sí. La mediana global es $2.030.000. Derecho, Ciencias Básicas y Agropecuaria están por encima. Usamos mediana porque los valores extremos la afectan menos.",
        22: "",
    },
    9: {
        1: "Comparamos qué tipo de institución aparece con mayor frecuencia en dos grupos de edad.",
        15: "Respuesta: la composición institucional cambia según el grupo de edad. Observamos una asociación, pero no podemos decir que la edad cause la elección.",
        16: "",
    },
    10: {
        0: "Pregunta 3 · ¿Qué aranceles están entre los más altos?",
        1: "Usamos el percentil 90 (P90): separa aproximadamente el 10% de ofertas con arancel más alto.",
        3: "P90",
        4: "$4.106.400",
        6: "SIGNIFICADO",
        7: "90%",
        9: "GRUPO SUPERIOR",
        10: "≈ 10%",
        12: "VALOR MÁXIMO",
        13: "$8.783.670",
        15: "OFERTAS SOBRE P90",
        16: "128",
        20: "10,1%",
        24: "73 / 55",
        28: "123 / 5",
        30: "Respuesta: el P90 es $4.106.400. Lo superan 128 ofertas (10,1%). De ellas, 73 son CRUCH y 55 privadas; 123 están en Concepción y 5 en Biobío.",
        31: "",
    },
    11: {
        0: "¿Cómo es el grupo de ofertas sobre P90?",
        1: "Describimos el 10% superior de aranceles. Estas variables no explican la causa del precio.",
        6: "55 privadas",
        9: "38 Salud",
        10: "38 Tecnología",
        13: "123 Concepción",
        14: "5 Biobío",
        19: "Lectura: vemos diferencias por institución, área, provincia y duración, pero ninguna de ellas puede presentarse como causa del arancel.",
        20: "",
    },
    12: {
        1: "Porcentaje y cantidad no significan lo mismo: debemos mirar ambos.",
        12: "En simple: Arauco tiene el mayor porcentaje dentro de su provincia, pero Concepción tiene muchas más matrículas transformadoras en cantidad total.",
        13: "",
    },
    13: {
        0: "Qué podemos concluir y qué no",
        1: "Los datos permiten describir diferencias y asociaciones, pero no demostrar causas.",
        13: "Qué ofertas quedan por sobre el percentil 90.",
    },
    14: {
        11: "128 de 1.273 ofertas superan el P90 de $4.106.400, equivalente a 10,1% del total.",
        12: "Respuesta central: en 2021 el bloque productivo tiene mayor peso que el transformador. Es una fotografía descriptiva de la matrícula, no una prueba de déficit ni de causalidad.",
        13: "",
    },
    15: {
        7: "Notebook final ejecutado · 0 errores",
    },
    16: {
        20: "Preguntas 1, 2 y 3",
        22: "rango, std, CV, agg, isin",
        23: "Dispersión general y comparación entre grupos",
    },
    17: {
        0: "ANEXO · Conceptos que debes saber explicar",
        1: "La clave es poder explicar qué mide cada concepto y cuándo lo usamos en el trabajo.",
        12: "Percentil 90",
        13: "quantile(0.90)",
        14: "Valor que deja aproximadamente 90% de los datos en o bajo ese punto.",
        15: "Desviación estándar",
        16: "std()",
        17: "Mide cuánto se alejan los valores respecto de su media, en la escala original.",
    },
    18: {
        11: "¿Por qué usamos P90?",
        12: "Porque permite separar de forma objetiva aproximadamente el 10% de ofertas con arancel más alto usando percentiles vistos en clase.",
    },
}

PATRON_T = re.compile(r"<a:t>(.*?)</a:t>", re.DOTALL)


def reemplazar_textos(xml: str, cambios: dict[int, str], diapositiva: int) -> str:
    coincidencias = list(PATRON_T.finditer(xml))
    for indice in cambios:
        if indice >= len(coincidencias):
            raise RuntimeError(
                f"Diapositiva {diapositiva}: índice {indice} fuera de rango; hay {len(coincidencias)} textos."
            )

    salida: list[str] = []
    ultimo = 0
    for i, m in enumerate(coincidencias):
        salida.append(xml[ultimo:m.start()])
        if i in cambios:
            valor = html.escape(cambios[i], quote=False)
            salida.append(f"<a:t>{valor}</a:t>")
        else:
            salida.append(m.group(0))
        ultimo = m.end()
    salida.append(xml[ultimo:])
    return "".join(salida)


def main() -> None:
    if not PPT.exists():
        raise FileNotFoundError(PPT)

    tmp_dir = Path(tempfile.mkdtemp(prefix="ppt_fix_"))
    salida = tmp_dir / PPT.name

    try:
        with zipfile.ZipFile(PPT, "r") as origen, zipfile.ZipFile(
            salida, "w", compression=zipfile.ZIP_DEFLATED
        ) as destino:
            for info in origen.infolist():
                datos = origen.read(info.filename)
                m = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", info.filename)
                if m:
                    n = int(m.group(1))
                    if n in REEMPLAZOS:
                        xml = datos.decode("utf-8")
                        xml = reemplazar_textos(xml, REEMPLAZOS[n], n)
                        datos = xml.encode("utf-8")
                destino.writestr(info, datos)

        # Validación rápida antes de reemplazar el archivo oficial.
        with zipfile.ZipFile(salida, "r") as z:
            textos = "\n".join(
                z.read(f"ppt/slides/slide{i}.xml").decode("utf-8") for i in range(1, 19)
            )

        prohibidos = [
            "Q3 + 1,5 × RIC",
            "Rango intercuartílico",
            "varianza",
            "var()",
            ">135<",
            "10,6%",
            "73 / 62",
            "129 / 6",
            "39 Salud",
            "39 Tecnología",
        ]
        for termino in prohibidos:
            if termino in textos:
                raise RuntimeError(f"Texto obsoleto todavía presente: {termino}")

        requeridos = [
            "percentil 90",
            "$4.106.400",
            "128",
            "10,1%",
            "73 / 55",
            "123 / 5",
            "38 Salud",
            "38 Tecnología",
            "quantile(0.90)",
        ]
        for termino in requeridos:
            if termino not in textos:
                raise RuntimeError(f"Falta texto esperado: {termino}")

        shutil.move(str(salida), str(PPT))
        print(f"PPT corregido: {PPT} ({PPT.stat().st_size} bytes)")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
