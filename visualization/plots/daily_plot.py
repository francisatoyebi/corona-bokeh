"""Daily plot implementation following Single Responsibility Principle."""

import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool, TabPanel, Select
from bokeh.layouts import column, row
from .base_plot import BasePlot


class DailyPlot(BasePlot):
    """Creates daily COVID-19 progression plots."""
    
    def create_panel(self, df: pd.DataFrame) -> TabPanel:
        """
        Create daily progression panel.
        
        Args:
            df: DataFrame with daily COVID data
            
        Returns:
            TabPanel with daily plots
        """
        countries = self.processor.get_country_list(df)
        initial_country = self.settings.default_country
        
        country_df = self.processor.filter_by_country(df, initial_country)
        src = self.create_data_source(country_df)
        
        confirmed_plot = self._create_confirmed_plot(src)
        recovered_plot = self._create_recovered_plot(src)
        death_plot = self._create_death_plot(src)
        
        menu = Select(options=countries, value=initial_country, title='Distribution')
        
        def update(attr, old, new):
            country = menu.value
            new_df = self.processor.filter_by_country(df, country)
            new_src = self.create_data_source(new_df)
            src.data.update(new_src.data)
        
        menu.on_change('value', update)
        
        controls = column(menu)
        layout1 = row(controls, confirmed_plot)
        layout2 = row(recovered_plot, death_plot)
        layout = column(layout1, layout2)
        
        return TabPanel(child=layout, title='Daily Progression')
    
    def _create_confirmed_plot(self, src):
        """Create confirmed cases plot."""
        return self._create_daily_plot(
            src, 'daily_conf', 'daily_conf_f',
            'Confirmed Cases', self.settings.plot.confirmed_color
        )
    
    def _create_recovered_plot(self, src):
        """Create recovered cases plot."""
        return self._create_daily_plot(
            src, 'daily_recovered', 'daily_recovered_f',
            'Recovered Cases', self.settings.plot.recovered_color
        )
    
    def _create_death_plot(self, src):
        """Create death cases plot."""
        return self._create_daily_plot(
            src, 'daily_death', 'daily_death_f',
            'Confirmed Death', self.settings.plot.death_color
        )
    
    def _create_daily_plot(self, src, field, tooltip_field, title, color):
        """
        Create a daily plot for specific metric.
        
        Args:
            src: Data source
            field: Field name in data
            tooltip_field: Field name for tooltip (formatted)
            title: Plot title
            color: Plot color
            
        Returns:
            Styled figure
        """
        p = figure(
            width=self.settings.plot.sub_plot_width,
            height=self.settings.plot.sub_plot_height,
            title=title,
            x_axis_label='Date',
            y_axis_label='Value',
            x_axis_type='datetime'
        )
        
        hover = HoverTool(
            tooltips=[
                ('As at', '@Date{%F}'),
                ('Confirmed Cases', '@daily_conf_f'),
                ('Recovered Cases', '@daily_recovered_f'),
                ('Death Cases', '@daily_death_f')
            ],
            formatters={'@Date': 'datetime'},
            mode='vline'
        )
        
        p.line('Date', field, source=src, color=self.settings.plot.line_color)
        p.diamond(
            'Date', field, source=src,
            fill_alpha=self.settings.plot.fill_alpha,
            size=self.settings.plot.small_glyph_size,
            hover_fill_color=self.settings.plot.hover_color,
            hover_fill_alpha=self.settings.plot.hover_alpha,
            color=color
        )
        p.add_tools(hover)
        
        return self.style_manager.apply_main_style(p)

