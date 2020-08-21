# Importing necessary library and module

import pandas as pd
import numpy as np

from bokeh.io import curdoc

from bokeh.plotting import figure

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, Panel, Button, Legend
from bokeh.models.widgets import CheckboxGroup, Slider, RangeSlider, Tabs, DateSlider

from bokeh.layouts import column, row, WidgetBox
from bokeh.palettes import Category20_16

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application

from bokeh.models import LabelSet, Label
from datetime import datetime, timedelta

def scatter(df):
    #global df1
    
    def make_dataset(df):
        return ColumnDataSource(df)
    
    def style(p):
        # Title 
        p.title.align = 'center'
        p.title.text_font_size = '20pt'
        p.title.text_font = 'serif'

        # Axis titles
        p.xaxis.axis_label_text_font_size = '14pt'
        p.xaxis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label_text_font_size = '14pt'
        p.yaxis.axis_label_text_font_style = 'bold'

        # Tick labels
        p.xaxis.major_label_text_font_size = '12pt'
        p.yaxis.major_label_text_font_size = '12pt'

        return p

    def make_plot(src):
        # Blank plot with correct labels
        p = figure(plot_width = 1000, plot_height = 600, title = 'Confirmed Cases vs Recovered Cases (Size of glyph = Confirmed Death)',
                  x_axis_label = 'Confirmed Cases', y_axis_label = 'Recovered Cases')
        
        
        
        p.circle('confirmed_cases', 'recovered_cases', source=src, fill_alpha=0.7, size='death1',
            hover_fill_color = 'purple', hover_fill_alpha = 0.7, color='color', legend_field = 'continent')

        hover = HoverTool(tooltips=[('As at', '@Date{%F}'),
                                    ('Country', '@Country'),
                                    ('Confirmed Cases', '@confirm'),
                                    ('Recovered/Death', '@recovered'),
                                    ('Death Cases', '@death')],
                         formatters={'@Date': 'datetime'})

        p.add_tools(hover)
        
        p.legend.location = "center_right"
        
        p.legend.click_policy = 'hide'

        # Styling
        p = style(p)

        return p
    
    # Callback function
    def update(attr, old, new):
       
        continent_to_plot = [continent_selection.labels[i] for i in 
                             continent_selection.active]
        
        df1 = df.set_index(['continent'])
        df1 = df1.loc[continent_to_plot]
        
        a = day_slider.value_as_date
        date = pd.to_datetime(a)

        d = df1[df1['Date'] == date]
        new_src = make_dataset(d)


        src.data.update(new_src.data)
    
    def animate_update():
        day = day_slider.value_as_date + timedelta(days=1)
        
        if day>df['Date'].max():
            day = df['Date'].min()
        day_slider.value = day

    def animate():
        global callback_id
        if button.label == '► Play':
            button.label = '❚❚ Pause'
            callback_id = curdoc().add_periodic_callback(animate_update, 200)
        else:
            button.label = '► Play'
            curdoc().remove_periodic_callback(callback_id)
            
    callback_id = None
    
    button = Button(label='► Play', width=60)
    button.on_click(animate)

        
    value = list(df['continent'].unique())
    continent_selection = CheckboxGroup(labels=value, active = [0, 1])
    continent_selection.on_change('active', update)
    
    day_slider = DateSlider(title="Date: ", start=df['Date'].min(), end=df['Date'].max(),
                                   value=df['Date'].max(), step=1)
    
    day_slider.on_change('value', update)
    
    controls = row(continent_selection, day_slider, button)
    
    initial = [continent_selection.labels[i] for i in continent_selection.active]
    df1 = df.set_index(['continent'])
    df1 = df1.loc[initial]
    
    dat = df1['Date'].max()
    d = df1[df1['Date'] == dat]
    src = make_dataset(d)
    
    p = make_plot(src)
    
    layout = column([controls, p])
    
    tab = Panel(child = layout, title = 'Progression')
    
    return tab