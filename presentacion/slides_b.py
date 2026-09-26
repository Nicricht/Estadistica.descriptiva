from ppt_deck import *
# 11
s=basic(11,4,'Pregunta obligatoria 3','¿Cuándo un arancel es sustantivamente más caro que la mayoría?','Criterio: valor atípico superior = Q3 + 1,5 × RIC sobre ofertas académicas únicas.',3); pic(s,'curve',.45,2.05,5.15);
for i,(k,v,c) in enumerate([('Q1','$1,616M',C),('Q3','$2,580M',C),('RIC','$964k',G),('LÍMITE','$4,026M',O),('OFERTAS','135',R)]): card(s,6.0+(i%3)*2.05,2.0+(i//3)*1.55,1.8,1.25,k,v,'',c,f'!!R{i}',14)
note(s,6.0,5.15,5.95,'135 / 1.273 = 10,6% · 73 CRUCH · 62 privadas · 129 Concepción · 6 Biobío.',R); pill(s,6.2,5.83,1.65,'Salud 39',C); pill(s,8.05,5.83,1.8,'Tecnología 39',C); pill(s,10.05,5.83,1.75,'10 vs 5 sem',G); footer(s)
# 12
s=basic(12,5,'Dimensión territorial','¿Cuánto talento transformador hay y dónde está?','Proporción y volumen absoluto cuentan historias distintas; no inferimos causalidad territorial.',4)
for i,(p,v,n,c) in enumerate([('ARAUCO','8,55%','232',O),('BIOBÍO','7,61%','966',G),('CONCEPCIÓN','6,77%','5.802',C)]): card(s,.85+i*4.05,2.1,3.45,1.5,p,v,n+' matrículas transformadoras',c,f'!!T{i}',23); q=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(2.2+i*4.05),Inches(4.25),Inches(.7),Inches(.7)); q.fill.solid(); q.fill.fore_color.rgb=c; q.line.color.rgb=W
note(s,.85,5.45,11.5,'Arauco tiene mayor proporción; Concepción concentra por lejos el mayor volumen.',C); footer(s)
# 13
s=basic(13,0,'Dimensión de género','La participación tecnológica también tiene una dimensión de género','Hallazgo descriptivo y pregunta futura, no consecuencia demostrada.',4); pic(s,'people',.5,2.0,3.5); bars(s,4.7,2.2,6.0,2.8,['Industria','Digital/TIC','Automatización'],[17.17,11.50,5.79],[O,C,PUP],20,'GEN'); note(s,4.7,5.25,6.0,'¿La transformación reducirá brechas o trasladará desigualdades hacia nuevas ocupaciones?',G); footer(s)
# 14
s=basic(14,1,'Huachipato 2024','Un shock industrial vuelve visible la vulnerabilidad regional','Punto de inflexión posterior a 2021. No atribuimos el cierre a falta de talento tecnológico.',4); pic(s,'industry',.45,2.0,4.5); card(s,5.55,2.05,2.55,1.45,'CIERRE','2024','Talcahuano',O,'!!HC',25); card(s,8.45,2.05,2.55,1.45,'AFECTADOS','7.168','directos e indirectos',R,'!!HW',24)
for i,t in enumerate(['reconversión','diversificación','fortalecimiento','innovación']): pill(s,5.55+(i%2)*2.9,4.05+(i//2)*.65,2.55,t,C if i%2 else G,f'!!H{i}')
source(s,'Ministerio de Economía · Plan de Fortalecimiento Industrial / avance 2026'); footer(s,'Contexto posterior a la línea base')
# 15
s=basic(15,2,'Respuesta regional 2024–2026','La región busca transformar su industria, no abandonarla','Manufactura avanzada, Industria 4.0, sistemas inteligentes, transición energética y capital humano.',4); pic(s,'steel',.45,2.0,3.1); pic(s,'chip',9.85,2.0,2.6,'!!IMG_B')
for i,(a,b,c) in enumerate([('PLAN INDUSTRIAL','32 medidas',O),('INDUSTRIA 4.0','centro tecnológico',C),('SISTEMAS 4.0','mantenimiento predictivo',G),('CAPITAL HUMANO','IA avanzada',PUP),('BIOBÍO 2050','innovación + talento',GN)]): card(s,3.5+(i%2)*2.75,2.0+(i//2)*1.25,2.45,1.0,a,b,'',c,f'!!RESP{i}',12)
source(s,'Ministerio de Economía; Corfo; GORE Biobío; Desarrolla Biobío'); footer(s)
# 16
s=basic(16,3,'ACERO + ALGORITMO','Transformar no significa reemplazar','Las capacidades digitales pueden incorporarse a los sectores productivos existentes.',4); pic(s,'steel',4.1,1.85,5.1)
for i,(a,b) in enumerate([('Manufactura','Automatización'),('Metalmecánica','Mantenimiento'),('Forestal','Sensores+datos'),('Puertos','Sistemas 4.0'),('Logística','Software'),('Industria','IA')]): x=.6+(i%3)*4.15; y=4.75+(i//3)*.75; pill(s,x,y,1.7,a,O,f'!!EA{i}'); text(s,x+1.75,y+.06,.25,.2,'+',12,W,True,PP_ALIGN.CENTER); pill(s,x+2.05,y,1.7,b,C,f'!!EB{i}')
footer(s)
# 17
s=basic(17,4,'Hipótesis futura','¿Qué riesgo merece investigarse a continuación?','Hipótesis, no conclusión: requiere empleo, vacantes, salarios, competencias, egresados y series temporales.',5); pic(s,'curve',8.0,2.0,3.7); card(s,.75,2.05,5.9,1.5,'HIPÓTESIS','Velocidades distintas','transformación industrial vs. capital humano',O,'!!HYP',21)
for i,t in enumerate(['adopción tecnológica','vacantes especializadas','talento externo','skills mismatch','inversión tecnológica','productividad potencial']): pill(s,.85+(i%2)*2.9,4.0+(i//2)*.62,2.55,t,R if i<3 else G,f'!!RSK{i}')
note(s,.85,6.0,5.45,'Riesgos plausibles ≠ efectos demostrados.',C); footer(s)
# 18
s=basic(18,5,'Línea temporal','Cuatro momentos, no una causalidad inventada','2021 es línea base; los hechos posteriores explican por qué esa fotografía puede volverse relevante.',5)
for i,(yr,lab,c) in enumerate([('2021','Fotografía + ENADEL',C),('2024','Shock Huachipato',R),('2024–26','Industria 4.0',O),('2050','Pregunta futura',GN)]): x=1+i*3.25; card(s,x-.25,2.0,2.35,1.05,yr,lab,'',c,f'!!TM{i}',13); q=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(x),Inches(3.65),Inches(.48),Inches(.48)); q.fill.solid(); q.fill.fore_color.rgb=c; q.line.color.rgb=W
for i in range(3): q=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(1.45+i*3.25),Inches(3.88),Inches(2.8),Inches(.03)); q.fill.solid(); q.fill.fore_color.rgb=GR; q.line.fill.background()
note(s,2.2,5.15,8.9,'¿Evolucionará el capital humano junto con la transformación productiva que la región proyecta?',C); footer(s)
# 19
s=basic(19,0,'Conclusiones y límites','Qué demostramos y qué NO demostramos','Separar resultados, contexto e hipótesis protege la interpretación estadística.',5); card(s,.75,2.0,3.45,1.5,'DEMOSTRAMOS','20,15% vs 6,92%','≈ 2,9 : 1 en 2021',O,'!!CA',19); card(s,4.55,2.0,3.45,1.5,'DEMOSTRAMOS','Precios + asociaciones','3 preguntas obligatorias',C,'!!CB',18); card(s,8.35,2.0,3.45,1.5,'NO DEMOSTRAMOS','Causalidad / déficit','ni evolución temporal',R,'!!CC',18)
for i,t in enumerate(['Solo 2021','Taxonomía propia','Una familia/carrera','Sin salarios','Sin vacantes carrera/carrera','Sin productividad','Sin serie temporal','Asociación ≠ causalidad']): pill(s,.8+(i%4)*3.0,4.1+(i//4)*.72,2.65,t,GR if i<4 else G,f'!!L{i}')
footer(s)
# 20
s=basic(20,1,'Fuentes y cierre','La pregunta que queda abierta','El desafío es incorporar capacidades digitales, automatización, datos e innovación a la identidad industrial del Biobío.',5); pic(s,'steel',7.8,1.8,4.3)
for i,t in enumerate(['SENCE · ENADEL 2021 Biobío','Ministerio de Economía · Plan Industrial 2024 / avance 2026','Corfo · Manufactura Avanzada e Industria 4.0, 2025','Corfo · Sistemas inteligentes / mantenimiento predictivo','GORE Biobío · Capital Humano Avanzado en IA','Desarrolla Biobío · Estrategia Biobío 2050','Excel del trabajo · elaboración propia']): text(s,.75,1.9+i*.5,6.5,.28,'• '+t,8.4,C if i==6 else W)
note(s,.95,5.72,11.0,'¿Está evolucionando el capital humano del Biobío al mismo ritmo que la transformación productiva que la región proyecta?',O); footer(s,'CIERRE · DEL ACERO AL ALGORITMO')
