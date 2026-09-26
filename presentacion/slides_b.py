from ppt_deck import *

s=basic(6,5,'Pregunta 2','Edad y tipo de institución','Usamos groupby(), agg() y crosstab().',4)
card(s,.8,2.0,3.5,1.5,'15 A 19 AÑOS','46,2% CRUCH','19,3% IP',C,'!!E1',21)
card(s,4.9,2.0,3.5,1.5,'40 AÑOS O MÁS','52,9% IP','10,9% CRUCH',O,'!!E2',21)
bars(s,1.0,4.35,7.2,1.35,['15–19 CRUCH','15–19 IP','40+ CRUCH','40+ IP'],[46.2,19.3,10.9,52.9],[C,G,G,O],60,'AGE')
note(s,8.7,4.45,3.25,'Se describen frecuencias observadas en la base.',G)
footer(s)

s=basic(7,0,'Pregunta 3','¿Hay carreras cuyo arancel sea más alto que la mayoría?','Usamos percentil 75, mediana, groupby() y agg().',4)
card(s,.8,2.0,3.2,1.5,'PERCENTIL 75','$4.261.900','quantile(0.75)',C,'!!Q3P',20)
for i,(k,v) in enumerate([('Odontología','$7.625.300'),('Medicina','$7.490.000'),('Lic. Medicina','$6.750.000'),('Ing. Civil Minas','$6.050.705')]):
    card(s,4.4+(i%2)*3.7,2.0+(i//2)*1.75,3.2,1.4,k,v,'mediana > P75',O if i<2 else G,f'!!Q3{i}',16)
note(s,1.0,5.2,10.9,'P75 deja al 75% de los datos a lo más en $4.261.900; revisamos carreras con mediana superior.',C)
footer(s)

s=basic(8,1,'Qué hicimos','Métodos utilizados en el trabajo','Cada uno aparece en los laboratorios del profesor.',5)
items=[('PANDAS','read_excel · head · tail'),('FRECUENCIAS','groupby · size · cut · cumsum'),('GRÁFICOS','bar · subplots'),('TENDENCIA','mean · median · mode'),('PERCENTILES','quantile'),('BIVARIADO','crosstab · agg'),('DISPERSIÓN','max · min · std · CV')]
for i,(a,b) in enumerate(items):
    card(s,.75+(i%3)*4.05,1.9+(i//3)*1.45,3.55,1.15,a,b,'',C if i%2==0 else G,f'!!K{i}',12)
footer(s)

s=basic(9,2,'Conclusiones','Resultados descriptivos principales','No agregamos técnicas fuera de los laboratorios.',5)
card(s,.75,2.0,3.55,1.5,'ÁREAS','Agropecuaria','mayor mediana de arancel',O,'!!C1',18)
card(s,4.9,2.0,3.55,1.5,'EDAD','Patrones distintos','según institución',C,'!!C2',18)
card(s,9.05,2.0,3.55,1.5,'P75','$4.261.900','referencia del 25% superior',G,'!!C3',18)
note(s,1.35,4.6,10.5,'El trabajo describe la base 2021 mediante frecuencias, gráficos, medidas descriptivas y percentiles.',C)
footer(s)

s=basic(10,3,'Cierre','Resumen del trabajo','Aplicación de estadística descriptiva a la base de matrículas del Biobío 2021.',5)
text(s,1.0,2.0,11.0,1.0,'Analizamos la base de matrículas del Biobío 2021 mediante herramientas de estadística descriptiva para responder preguntas sobre aranceles, edad y tipo de institución.',18,W,True,PP_ALIGN.CENTER)
note(s,2.0,4.3,9.3,'Las herramientas utilizadas corresponden a los contenidos de los laboratorios 0 al 5.',O)
footer(s,'Material de estudio: laboratorios 0 al 5 del profesor')
