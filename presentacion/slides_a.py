from ppt_deck import *
# 1
s=prs.slides.add_slide(prs.slide_layouts[6]); bg(s,0); card(s,.65,.72,5.35,2.2,'ESTADÍSTICA DESCRIPTIVA','DEL ACERO\nAL ALGORITMO','Educación Superior del Biobío',O,'!!COVER',28); pic(s,'steel',6.05,1.2,6.3); text(s,.9,5.15,11.3,.78,'¿Desde qué base de capital humano parte el Biobío para transformar su histórica vocación industrial hacia una economía de manufactura avanzada e Industria 4.0?',15,W,True,name='!!QUESTION'); flow(s,1); footer(s)
# 2
s=basic(2,1,'Biobío industrial','¿Por qué importa estudiar esta base formativa?','Industria, manufactura, forestal, puertos, logística, pesca, construcción y energía.',0); pic(s,'industry',.5,1.9,5.4); pic(s,'chip',9.05,2.0,3.2,'!!IMG_B');
for i,t in enumerate(['Industria','Forestal','Puertos','Logística','Pesca','Energía']): pill(s,5.55+(i%2)*2.25,2.0+(i//2)*.55,1.95,t,O if i<4 else C,f'!!SEC{i}')
note(s,5.55,4.0,4.15,'La pregunta no es INDUSTRIA vs. TECNOLOGÍA.',O); note(s,5.55,4.7,4.15,'La pregunta es INDUSTRIA + TECNOLOGÍA.',C); footer(s)
# 3
s=basic(3,2,'Dataset y metodología','De 106.555 registros a tres unidades de análisis','Personas, precios y ofertas requieren bases distintas para no distorsionar resultados.',0); pic(s,'data',.45,1.85,3.0)
for i,(k,v,sub,c) in enumerate([('ORIGINAL','106.555','28 columnas',C),('PREGRADO','101.093','personas / ADN',C),('PRECIO','101.067','arancel > $0',O),('OFERTAS','1.273','precios únicos',G)]): card(s,3.75+i*2.2,2.05,1.9,1.35,k,v,sub,c,f'!!K{i}',16)
note(s,3.75,4.0,8.5,'Oferta única = institución + carrera + comuna + modalidad + jornada + duración + matrícula + arancel.',G); pill(s,4.0,4.8,2.0,'0 duplicados',GN); pill(s,6.2,4.8,2.5,'26 aranceles $0',O); pill(s,8.9,4.8,2.6,'nulos en acreditación',GR); footer(s)
# 4
s=basic(4,3,'Radiografía estadística','¿Qué nos dicen los datos antes del problema regional?','Frecuencias, tendencia central, percentiles y dispersión resumen la estructura general.',1); bars(s,.75,2.0,4.0,2.5,['Tecnol.','Salud','Adm.','Educ.'],[27.6,24.3,13.4,11.4],[C,C,O,G]);
for i,(k,v,sub,c) in enumerate([('GÉNERO','54,3% F','45,7% M',C),('DURACIÓN','10 sem','moda',GN),('CV ARANCEL','47,1%','dispersión relativa',G),('MEDIA','$3,22M','arancel',C),('MEDIANA','$3,13M','arancel',O),('CUARTILES','Q1 / Q3','percentiles',G)]): card(s,5.2+(i%3)*2.25,2.0+(i//3)*1.55,1.95,1.25,k,v,sub,c,f'!!S{i}',13)
note(s,5.2,5.25,6.45,'El notebook aplica fi, hi, acumuladas, moda, percentiles, rango, desviación y CV.',C); footer(s)
# 5
s=basic(5,4,'ADN profesional','De cientos de carreras a nueve familias estratégicas','Taxonomía analítica propia: una carrera se asigna a una sola familia para evitar doble conteo.',2); pic(s,'industry',.45,1.9,3.2); pic(s,'chip',9.6,1.85,2.8,'!!IMG_B');
for i,t in enumerate(['Industria','Construcción','Logística','Forestal','Pesca','Agro','Digital/TIC','Automatización','Energía+bio']): pill(s,3.35+(i%3)*2.05,2.0+(i//3)*.65,1.8,t,O if i<6 else C,f'!!F{i}')
note(s,3.35,4.25,5.85,'MOTORES PRODUCTIVOS  →  “ACERO”',O); note(s,3.35,5.0,5.85,'CAPACIDADES TRANSFORMADORAS  →  “ALGORITMO”',C); footer(s)
# 6
s=basic(6,5,'Hallazgo central','En 2021, el componente productivo era casi tres veces el transformador','Resultado descriptivo. No demuestra déficit, atraso educativo ni escasez laboral.',2); pic(s,'industry',.45,2.0,3.1); pic(s,'chip',9.7,2.0,2.75,'!!IMG_B'); card(s,3.75,2.05,2.35,1.55,'MOTORES','20.368','20,15%',O,'!!MOT',24); card(s,6.45,2.05,2.35,1.55,'TRANSFORMADORAS','7.000','6,92%',C,'!!TRA',24); note(s,4.3,4.15,4.0,'≈ 2,9 matrículas productivas por cada transformadora.',G); note(s,3.4,5.05,5.8,'Línea base 2021: “más peso” ≠ “déficit”.',C); footer(s)
# 7
s=basic(7,0,'Interpretación contextual','¿Por qué podría existir esa diferencia?','Planteamos explicaciones plausibles, no causas demostradas por el Excel.',2); pic(s,'steel',8.7,2.05,3.55)
for i,(k,v) in enumerate([('HERENCIA INDUSTRIAL','Trayectoria'),('OFERTA FORMATIVA','Visible'),('TRANSFORMACIÓN','Más reciente'),('CAUSALIDAD','No demostrada')]): card(s,.8+(i%2)*3.4,2.0+(i//2)*1.7,3.0,1.3,k,v,'interpretación contextual',O if i<2 else C,f'!!I{i}',14)
note(s,.8,5.4,6.4,'Contexto regional ≠ prueba causal.',R); footer(s)
# 8
s=basic(8,1,'Señal laboral 2021','En el mismo período, la manufactura reportaba dificultades de contratación','ENADEL aporta contexto laboral, pero NO prueba relación causal con nuestro 6,92%.',4); pic(s,'industry',.45,2.0,3.6); pic(s,'people',9.75,2.15,2.5,'!!IMG_B'); card(s,4.2,2.05,2.1,1.45,'EMPRESAS','69%','dificultades para llenar vacantes',O,'!!E1',23); card(s,6.55,2.05,2.1,1.45,'POSTULANTES','30%','falta de postulantes',C,'!!E2',23); card(s,4.2,3.85,2.1,1.45,'COMPETENCIAS','30%','técnicas insuficientes',C,'!!E3',23); note(s,6.55,3.85,2.95,'69% NO es causado por el 6,92%.',R); source(s,'SENCE · Observatorio Laboral Biobío · ENADEL 2021'); footer(s,'Contexto laboral · no causal')
# 9
s=basic(9,2,'Pregunta obligatoria 1','¿Hay áreas donde las carreras sean más caras?','Unidad: 1.273 ofertas únicas. Criterio: mediana, menos sensible a valores extremos.',3); bars(s,.65,2.05,6.4,2.8,['Derecho','Cs. Bás.','Agro','Tecnol.','Salud','Global'],[3.586,3.290,2.982,2.122,2.080,2.030],[O,G,GN,C,C,GR],4.0,'Q1'); pic(s,'price',8.4,2.1,3.6); card(s,.75,5.2,2.15,1.0,'CRITERIO','Mediana','por área',C,'!!QC',13); card(s,3.1,5.2,2.15,1.0,'COMPLEMENTO','P25 · P75','+ cantidad',G,'!!QQ',12); card(s,5.45,5.2,2.15,1.0,'MAYOR','Derecho','$3.586.000',O,'!!QD',13); footer(s)
# 10
s=basic(10,3,'Pregunta obligatoria 2','La composición institucional cambia entre grupos de edad','Tabla de contingencia y porcentajes: asociación observada, no “la edad causa la elección”.',3); pic(s,'people',.45,1.95,3.0); pic(s,'campus',9.6,2.15,2.75,'!!IMG_B'); card(s,3.85,2.0,2.2,1.35,'15–19','46,24% CRUCH','19,30% IP',C,'!!AGE1',20); card(s,6.35,2.0,2.2,1.35,'40+','52,93% IP','10,88% CRUCH',O,'!!AGE2',20); bars(s,3.9,4.25,4.6,1.35,['15–19 CRUCH','15–19 IP','40+ CRUCH','40+ IP'],[46.24,19.30,10.88,52.93],[C,G,G,O],60,'AGE'); note(s,8.8,4.45,3.1,'Se observan diferencias ≠ influencia causal.',C); footer(s)
