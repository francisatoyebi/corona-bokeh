"""Cumulative plot implementation following Single Responsibility Principle."""

import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool, TabPanel, Select
from bokeh.layouts import column, row
from .base_plot import BasePlot


class CumulativePlot(BasePlot):
    """Creates cumulative COVID-19 progression plots."""
    
    def create_panel(self, df: pd.DataFrame) -> TabPanel:
        """
        Create cumulative progression panel.
        
        Args:
            df: DataFrame with cumulative COVID data
            
        Returns:
            TabPanel with cumulative plots
        """
        countries = self.processor.get_country_list(df)
        initial_country = self.settings.default_country
        
        country_df = self.processor.filter_by_country(df, initial_country)
        src = self.create_data_source(country_df)
        
        overview_plot = self._create_overview_plot(src)
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
        left_layout = column(controls, confirmed_plot, recovered_plot, death_plot)
        layout = row(left_layout, overview_plot)
        
        return TabPanel(child=layout, title='Cummulative Progression')
    
    def _create_overview_plot(self, src):
        """Create main overview plot."""
        p = figure(
            width=self.settings.plot.main_plot_width,
            height=self.settings.plot.main_plot_height,
            title='Overview',
            x_axis_label='Date',
            y_axis_label='Value',
            x_axis_type='datetime'
        )
        
        hover = HoverTool(
            tooltips=[
                ('As at', '@Date{%F}'),
                ('Confirmed Cases', '@confirm'),
                ('Recovered Cases', '@recovered'),
                ('Death Cases', '@death')
            ],
            formatters={'@Date': 'datetime'}
        )
        
        self._add_line_with_circles(
            p, src, 'recovered_cases', 
            self.settings.plot.recovered_color
        )
        self._add_line_with_circles(
            p, src, 'death_cases', 
            self.settings.plot.death_color
        )
        self._add_line_with_circles(
            p, src, 'confirmed_cases', 
            self.settings.plot.confirmed_color
        )
        
        p.add_tools(hover)
        return self.style_manager.apply_main_style(p)
    
    def _create_confirmed_plot(self, src):
        """Create confirmed cases small plot."""
        return self._create_small_plot(
            src, 'confirmed_cases', '@confirm',
            'Confirmed Cases', self.settings.plot.confirmed_color
        )
    
    def _create_recovered_plot(self, src):
        """Create recovered cases small plot."""
        return self._create_small_plot(
            src, 'recovered_cases', '@recovered',
            'Recovered Cases', self.settings.plot.recovered_color
        )
    
    def _create_death_plot(self, src):
        """Create death cases small plot."""
        return self._create_small_plot(
            src, 'death_cases', '@death',
            'Confirmed Death', self.settings.plot.death_color
        )
    
    def _create_small_plot(self, src, field, tooltip_field, title, color):
        """
        Create a small plot for specific metric.
        
        Args:
            src: Data source
            field: Field name in data
            tooltip_field: Field name for tooltip
            title: Plot title
            color: Plot color
            
        Returns:
            Styled figure
        """
        p = figure(
            width=self.settings.plot.small_plot_width,
            height=self.settings.plot.small_plot_height,
            title=title,
            x_axis_label='Date',
            y_axis_label='Value',
            x_axis_type='datetime'
        )
        
        hover = HoverTool(
            tooltips=[('As at', '@Date{%F}'), (title, tooltip_field)],
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
        
        return self.style_manager.apply_small_style(p)
    
    def _add_line_with_circles(self, plot, src, field, color):
        """
        Add line and circle glyphs to plot.
        
        Args:
            plot: Figure to add glyphs to
            src: Data source
            field: Field name
            color: Glyph color
        """
        plot.line('Date', field, source=src, color=self.settings.plot.line_color)
        plot.circle(
            'Date', field, source=src,
            fill_alpha=self.settings.plot.fill_alpha,
            size=self.settings.plot.default_glyph_size,
            hover_fill_color=self.settings.plot.hover_color,
            hover_fill_alpha=self.settings.plot.hover_alpha,
            color=color
        )

