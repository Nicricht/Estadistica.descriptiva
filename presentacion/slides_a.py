from ppt_deck import *

s=prs.slides.add_slide(prs.slide_layouts[6]); bg(s,0)
card(s,.75,.85,5.8,2.0,'ESTADÍSTICA DESCRIPTIVA','EDUCACIÓN SUPERIOR','Biobío 2021',C,'!!COVER',27)
text(s,.9,4.0,11.3,.7,'Aplicación de los contenidos de los laboratorios 0 al 5 del profesor.',18,W,True,name='!!QUESTION')
note(s,.9,5.15,9.4,'Metodología: Pandas, frecuencias, gráficos, tendencia central, percentiles y dispersión.',O)
flow(s,1); footer(s)

s=basic(2,1,'Base de datos','Carga y filtro de la información','Laboratorio 0: Pandas, exploración y filtros.',0)
for i,(k,v,sub,c) in enumerate([('ORIGINAL','106.555','registros',C),('PREGRADO','101.093','matrículas',O),('ARANCEL > 0','101.067','matrículas',G)]):
    card(s,1.0+i*3.7,2.0,3.1,1.5,k,v,sub,c,f'!!D{i}',22)
for i,t in enumerate(['read_excel()','head()','tail()','shape','info()','value_counts()','isin()']):
    pill(s,1.0+(i%4)*2.85,4.4+(i//4)*.6,2.45,t,C if i<4 else G,f'!!F{i}')
footer(s)

s=basic(3,2,'Tablas de frecuencia','¿Cómo se distribuyen las matrículas?','Laboratorio 2: frecuencia absoluta, relativa y acumulada.',1)
bars(s,.7,2.0,5.0,2.6,['Tecnol.','Salud','Adm.','Educ.'],[27.6,24.3,13.4,11.4],[C,O,G,GN],30,'AREA')
card(s,6.2,2.0,2.5,1.4,'FEMENINO','54,3%','54.881 matrículas',C,'!!GEN1',20)
card(s,9.1,2.0,2.5,1.4,'MASCULINO','45,7%','46.212 matrículas',O,'!!GEN2',20)
note(s,6.2,4.05,5.4,'Herramientas: groupby().size(), pd.cut(), cumsum().',G)
footer(s)

s=basic(4,3,'Medidas descriptivas','Tendencia central, percentiles y dispersión','Laboratorios 4 y 5.',3)
for i,(k,v,sub,c) in enumerate([('MEDIA ARANCEL','$3.224.895','mean()',C),('MEDIANA','$3.133.750','median()',O),('MODA','$3.373.000','mode()',G),('P25','$1.988.000','quantile(.25)',GN),('P75','$4.261.900','quantile(.75)',C),('CV','47,1%','std / mean × 100',O)]):
    card(s,.75+(i%3)*4.0,2.0+(i//3)*1.8,3.45,1.45,k,v,sub,c,f'!!M{i}',16)
note(s,2.3,5.65,8.7,'Lab 5: máximo, mínimo, rango, desviación estándar y coeficiente de variación.',G)
footer(s)

s=basic(5,4,'Pregunta 1','¿Hay áreas donde las carreras sean más caras?','Usamos groupby(), agg(), media y mediana.',4)
bars(s,.75,2.0,7.0,2.8,['Agro','Derecho','Salud','Cs. Bás.','Tecnol.'],[4.751,4.250,4.243,4.145,2.314],[O,G,C,GN,GR],5.2,'P1')
card(s,8.35,2.05,3.45,1.35,'MAYOR MEDIANA','$4.751.078','Agropecuaria',O,'!!P1A',18)
card(s,8.35,3.75,3.45,1.35,'SIGUIENTES','Derecho · Salud','≈ $4,25M',C,'!!P1B',16)
note(s,8.35,5.45,3.45,'Comparación descriptiva por mediana.',G)
footer(s)
