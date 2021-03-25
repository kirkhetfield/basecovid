pip install plotly==4.14.3
!pip install plotly==4.14.3

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots


basecovid = pd.read_csv('base.csv',sep=';')


basecovid['Infectados/Milhao'] = (basecovid['Infectados']/ basecovid['Populacao']) * 1000000

basecovid['Mortes/Milhao'] = (basecovid['Mortes']/ basecovid['Populacao']) * 1000000

basecovid['Letalidade(Em %)'] = (basecovid['Mortes']/ basecovid['Infectados']) * 100



basecovid.describe().apply(lambda s: s.apply('{0:.5f}'.format))


top10_milhao = pd.DataFrame(basecovid).sort_values(by=['Mortes/Milhao'],ascending = False).nlargest(25, 'Mortes/Milhao')
top10_letalidade = pd.DataFrame(basecovid).sort_values(by=['Letalidade(Em %)'],ascending = False).nlargest(25, 'Letalidade(Em %)')



fig3 = px.bar(top10_milhao, x = top10_milhao.Pais, y = 'Mortes/Milhao', height = 600, color = 'Mortes/Milhao',
             title = 'Top 25 Mortes / Milhão', hover_data=["Mortes/Milhao","Infectados","Mortes","Recuperados"], color_continuous_scale = px.colors.sequential.Viridis)
fig3.show()



top10_confirmed = basecovid.groupby('Pais')['Infectados'].sum().nlargest(10).sort_values(ascending = False)
fig1 = px.scatter(top10_confirmed, x = top10_confirmed.index, y = 'Infectados', size = 'Infectados', size_max = 120,
                color = top10_confirmed.index, title = '10 países com mais casos')
fig1.show()



fig3 = px.bar(top10_letalidade, x = top10_letalidade.Pais, y = 'Letalidade(Em %)', height = 600, color = 'Letalidade(Em %)',
             title = 'Top 25  Maiores letalidades', hover_data=["Mortes/Milhao","Infectados","Mortes","Recuperados"], color_continuous_scale = px.colors.sequential.Viridis)
fig3.show()