#Importing necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from scripts.line_plot import *
from scripts.scatterplot import *
from os.path import dirname, join
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from bokeh.embed import components
from bokeh.io import show, output_file
output_file('a.html')


df_line = pd.read_csv(join(dirname(__file__), 'data', 'imp_line_covid.csv'), index_col=0).dropna()
df_scatter = pd.read_csv(join(dirname(__file__), 'data', 'github_cool_covid.csv'), index_col=0).dropna()


from datetime import datetime
df_line['Date']=pd.to_datetime(df_line['Date'], format="%Y/%m/%d")
df_scatter['Date']=pd.to_datetime(df_scatter['Date'], format="%Y/%m/%d")


tab1 = daily(df_line)
tab2 = cummulative(df_line)
tab3 = scatter(df_scatter)

tab = Tabs(tabs = [tab1, tab2, tab3])

curdoc().add_root(tab)
curdoc().title = 'Corona'

show(curdoc)
