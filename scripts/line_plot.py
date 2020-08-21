from bokeh.models import ColumnDataSource, Select 

import pandas as pd
import numpy as np

from bokeh.plotting import figure

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, Panel
from bokeh.models.widgets import CheckboxGroup, Slider, RangeSlider, Tabs, DateSlider, DateRangeSlider

from bokeh.layouts import column, row, WidgetBox

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application

def cummulative(df):
    
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
    def style_z(p):
        # Title 
        p.title.align = 'center'
        p.title.text_font_size = '10pt'
        p.title.text_font = 'serif'

        # Axis titles
        p.xaxis.axis_label_text_font_size = '7pt'
        p.xaxis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label_text_font_size = '7pt'
        p.yaxis.axis_label_text_font_style = 'bold'

        # Tick labels
        p.xaxis.major_label_text_font_size = '6pt'
        p.yaxis.major_label_text_font_size = '6pt'

        return p
    
    def make_plot_g(src):
        # Blank plot with correct labels
        p = figure(plot_width = 1000, plot_height = 700, title = 'Overview',
                  x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
        hover = HoverTool(tooltips=[('As at', '@Date{%F}'), ('Confirmed Cases', '@confirm'),
                                    ('Recovered Cases', '@recovered'),
                                    ('Death Cases', '@death')],
                         formatters={'@Date': 'datetime'})
        
        p.line('Date', 'recovered_cases', source=src, color='gray')
        p.circle('Date', 'recovered_cases', source=src, fill_alpha=0.7, size=7,
            hover_fill_color = 'purple', hover_fill_alpha = 1, 
                 color='green')
        p.add_tools(hover)
        
        
        p.line('Date', 'death_cases', source=src, color='gray')
        p.circle('Date', 'death_cases', source=src, fill_alpha=0.7, size=7,
            hover_fill_color = 'purple', hover_fill_alpha = 1, 
                 color='red')
        
        p.line('Date', 'confirmed_cases', source=src, color='gray')
        p.circle('Date', 'confirmed_cases', source=src, fill_alpha=0.7, size=7,
            hover_fill_color = 'purple', hover_fill_alpha = 1, 
                 color='orange')
        p.add_tools(hover)

        # Styling
        p = style(p)

        return p
    
    
    
    def make_plot1(src):
        # Blank plot with correct labels
            pp = figure(plot_width = 500, plot_height = 200, title = 'Confirmed Cases',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Confirmed Cases', '@confirm')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            pp.line('Date', 'confirmed_cases', source=src, color='gray')
            pp.diamond('Date', 'confirmed_cases', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='orange')
            pp.add_tools(hover)       

            # Styling
            pp = style_z(pp)

            return pp
        
    def make_plot2(src):
        # Blank plot with correct labels
            p1 = figure(plot_width = 500, plot_height = 200, title = 'Recovered Cases',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Recovered Cases', '@recovered')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            p1.line('Date', 'recovered_cases', source=src, color='gray')
            p1.diamond('Date', 'recovered_cases', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='green')
            p1.add_tools(hover)       

            # Styling
            p1 = style_z(p1)

            return p1
        
    def make_plot3(src):
        # Blank plot with correct labels
            p2= figure(plot_width = 500, plot_height = 200, title = 'Confirmed Death',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Death Cases', '@death')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            p2.line('Date', 'death_cases', source=src, color='gray')
            p2.diamond('Date', 'death_cases', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='red')
            p2.add_tools(hover)       

            # Styling
            p2 = style_z(p2)

            return p2
    
    # Update function takes three default parameters
    def update(attr, old, new):
        country = menu.value

        df1 = df[df['Country'] == country]
        new_src = make_dataset(df1)

        # Update the source used the quad glpyhs
        src.data.update(new_src.data)
        
        return country
    
    option = list(df['Country'].value_counts().index)
    option.sort() 
    
    menu = Select(options=option, value = 'Afghanistan', title='Distribution')
    
    menu.on_change('value', update) 
    
    controls = column(menu)
    
    country = menu.value
     
    df1 = df[df['Country'] == country]
    src = make_dataset(df1)
    
    
    p = make_plot_g(src)
    p1 = make_plot1(src)
    p2 = make_plot2(src)
    p3 = make_plot3(src)
    
    layout = column([controls, p1,p2, p3])
    layout = row(layout,p)
    tab = Panel(child = layout, title = 'Cummulative Progression')

    
    return tab

def daily(df):
    
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

    def make_plot1(src):
        # Blank plot with correct labels
            pp = figure(plot_width = 700, plot_height = 300, title = 'Confirmed Cases',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Confirmed Cases', '@daily_conf_f'),
                                       ('Recovered Cases', '@daily_recovered_f'),
                                       ('Death Cases', '@daily_death_f')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            pp.line('Date', 'daily_conf', source=src, color='gray')
            pp.diamond('Date', 'daily_conf', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='orange')
            pp.add_tools(hover)

            # Styling
            pp = style(pp)

            return pp
        
    def make_plot2(src):
        # Blank plot with correct labels
            p1 = figure(plot_width = 700, plot_height = 300, title = 'Recovered Cases',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Confirmed Cases', '@daily_conf_f'),
                                        ('Recovered Cases', '@daily_recovered_f'),
                                       ('Death Cases', '@daily_death_f')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            p1.line('Date', 'daily_recovered', source=src, color='gray')
            p1.diamond('Date', 'daily_recovered', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='green')
            p1.add_tools(hover)       

            # Styling
            p1 = style(p1)

            return p1
        
    def make_plot3(src):
        # Blank plot with correct labels
            p2= figure(plot_width = 700, plot_height = 300, title = 'Confirmed Death',
                      x_axis_label = 'Date', y_axis_label = 'Value', x_axis_type='datetime')
            
            hover = HoverTool(tooltips=[('As at', '@Date{%F}'),('Confirmed Cases', '@daily_conf_f'),
                                        ('Recovered Cases', '@daily_recovered_f'),
                                        ('Death Cases', '@daily_death_f')],
                              formatters={'@Date': 'datetime'}, mode = 'vline')

            p2.line('Date', 'daily_death', source=src, color='gray')
            p2.diamond('Date', 'daily_death', source=src, fill_alpha=0.7, size=5,
                hover_fill_color = 'purple', hover_fill_alpha = 1, 
                     color='red')
            p2.add_tools(hover)       

            # Styling
            p2 = style(p2)

            return p2
    
    # Update function takes three default parameters
    def update(attr, old, new):
        country = menu.value
        
        df1 = df[df['Country'] == country]
        new_src = make_dataset(df1)

        src.data.update(new_src.data)
        
        return country
    
    option = list(df['Country'].value_counts().index)
    option.sort() 
    
    menu = Select(options=option, value = 'Afghanistan', title='Distribution')
    
    menu.on_change('value', update) 
    
    controls = column(menu)
    
    country = menu.value
     
    df1 = df[df['Country'] == country]
    src = make_dataset(df1)
    
    p1 = make_plot1(src)
    p2 = make_plot2(src)
    p3 = make_plot3(src)
    
    layout1 = row([controls, p1])
    layout2 = row([p2, p3], sizing_mode="scale_both")
    layout = column(layout1, layout2)
    
    tab = Panel(child = layout, title = 'Daily Progression')

    
    return tab