"""Centralized styling management following DRY principle."""

from bokeh.plotting import figure
from config.settings import PlotSettings


class PlotStyleManager:
    """Manages plot styling to avoid code duplication."""
    
    def __init__(self, settings: PlotSettings):
        """
        Initialize style manager.
        
        Args:
            settings: Plot settings configuration
        """
        self.settings = settings
    
    def apply_main_style(self, plot: figure) -> figure:
        """
        Apply main plot styling.
        
        Args:
            plot: Bokeh figure to style
            
        Returns:
            Styled figure
        """
        plot.title.align = 'center'
        plot.title.text_font_size = self.settings.title_font_size
        plot.title.text_font = self.settings.title_font
        
        plot.xaxis.axis_label_text_font_size = self.settings.axis_label_font_size
        plot.xaxis.axis_label_text_font_style = self.settings.axis_label_style
        plot.yaxis.axis_label_text_font_size = self.settings.axis_label_font_size
        plot.yaxis.axis_label_text_font_style = self.settings.axis_label_style
        
        plot.xaxis.major_label_text_font_size = self.settings.tick_label_font_size
        plot.yaxis.major_label_text_font_size = self.settings.tick_label_font_size
        
        return plot
    
    def apply_small_style(self, plot: figure) -> figure:
        """
        Apply small plot styling.
        
        Args:
            plot: Bokeh figure to style
            
        Returns:
            Styled figure
        """
        plot.title.align = 'center'
        plot.title.text_font_size = self.settings.small_title_font_size
        plot.title.text_font = self.settings.title_font
        
        plot.xaxis.axis_label_text_font_size = self.settings.small_axis_label_font_size
        plot.xaxis.axis_label_text_font_style = self.settings.axis_label_style
        plot.yaxis.axis_label_text_font_size = self.settings.small_axis_label_font_size
        plot.yaxis.axis_label_text_font_style = self.settings.axis_label_style
        
        plot.xaxis.major_label_text_font_size = self.settings.small_tick_label_font_size
        plot.yaxis.major_label_text_font_size = self.settings.small_tick_label_font_size
        
        return plot

