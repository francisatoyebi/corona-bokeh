"""Scatter plot implementation following Single Responsibility Principle."""

import pandas as pd
from datetime import timedelta
from bokeh.plotting import figure
from bokeh.models import HoverTool, TabPanel, Button, CheckboxGroup, DateSlider
from bokeh.layouts import column, row
from bokeh.io import curdoc
from .base_plot import BasePlot


class ScatterPlot(BasePlot):
    """Creates scatter plot with animation for COVID-19 progression."""
    
    def __init__(self, settings):
        """Initialize scatter plot."""
        super().__init__(settings)
        self.callback_id = None
    
    def create_panel(self, df: pd.DataFrame) -> TabPanel:
        """
        Create scatter plot panel with animation controls.
        
        Args:
            df: DataFrame with scatter plot data
            
        Returns:
            TabPanel with scatter plot and controls
        """
        continents = self.processor.get_continent_list(df)
        initial_continents = continents[:2] if len(continents) >= 2 else continents
        
        filtered_df = self.processor.filter_by_continents(df, initial_continents)
        max_date = df['Date'].max()
        date_filtered_df = self.processor.filter_by_date(filtered_df, max_date)
        
        src = self.create_data_source(date_filtered_df)
        
        plot = self._create_scatter_plot(src)
        
        continent_selection = CheckboxGroup(
            labels=continents,
            active=[i for i, c in enumerate(continents) if c in initial_continents]
        )
        
        day_slider = DateSlider(
            title="Date: ",
            start=df['Date'].min(),
            end=df['Date'].max(),
            value=df['Date'].max(),
            step=1
        )
        
        button = Button(label='► Play', width=60)
        
        def update(attr, old, new):
            selected_continents = [
                continent_selection.labels[i] 
                for i in continent_selection.active
            ]
            
            temp_df = self.processor.filter_by_continents(df, selected_continents)
            date = pd.to_datetime(day_slider.value_as_date)
            filtered_df = self.processor.filter_by_date(temp_df, date)
            
            new_src = self.create_data_source(filtered_df)
            src.data.update(new_src.data)
        
        def animate_update():
            day = day_slider.value_as_date + timedelta(days=1)
            
            # Convert to Timestamp for comparison with pandas datetime
            if pd.Timestamp(day) > df['Date'].max():
                day = df['Date'].min().date()
            day_slider.value = day
        
        def animate():
            if button.label == '► Play':
                button.label = '❚❚ Pause'
                self.callback_id = curdoc().add_periodic_callback(
                    animate_update, 
                    self.settings.animation_interval
                )
            else:
                button.label = '► Play'
                if self.callback_id is not None:
                    curdoc().remove_periodic_callback(self.callback_id)
        
        continent_selection.on_change('active', update)
        day_slider.on_change('value', update)
        button.on_click(animate)
        
        controls = row(continent_selection, day_slider, button)
        layout = column(controls, plot)
        
        return TabPanel(child=layout, title='Progression')
    
    def _create_scatter_plot(self, src):
        """
        Create scatter plot figure.
        
        Args:
            src: Data source
            
        Returns:
            Styled figure
        """
        p = figure(
            width=self.settings.plot.main_plot_width,
            height=600,
            title='Confirmed Cases vs Recovered Cases (Size of glyph = Confirmed Death)',
            x_axis_label='Confirmed Cases',
            y_axis_label='Recovered Cases'
        )
        
        p.circle(
            'confirmed_cases', 'recovered_cases',
            source=src,
            fill_alpha=self.settings.plot.fill_alpha,
            size='death1',
            hover_fill_color=self.settings.plot.hover_color,
            hover_fill_alpha=0.7,
            color='color',
            legend_field='continent'
        )
        
        hover = HoverTool(
            tooltips=[
                ('As at', '@Date{%F}'),
                ('Country', '@Country'),
                ('Confirmed', '@confirm'),
                ('Recovered', '@recovered'),
                ('Death', '@death')
            ],
            formatters={'@Date': 'datetime'}
        )
        
        p.add_tools(hover)
        p.legend.location = "center_right"
        p.legend.click_policy = 'hide'
        
        return self.style_manager.apply_main_style(p)

