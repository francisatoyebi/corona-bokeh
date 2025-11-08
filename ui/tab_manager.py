"""Tab management following Single Responsibility Principle."""

import pandas as pd
from bokeh.models import TabPanel, Tabs
from config.settings import AppSettings
from visualization.plots import DailyPlot, CumulativePlot, ScatterPlot


class TabManager:
    """Manages creation and coordination of dashboard tabs."""
    
    def __init__(self, settings: AppSettings):
        """
        Initialize tab manager.
        
        Args:
            settings: Application settings
        """
        self.settings = settings
        self.daily_plot = DailyPlot(settings)
        self.cumulative_plot = CumulativePlot(settings)
        self.scatter_plot = ScatterPlot(settings)
    
    def create_tabs(self, line_df: pd.DataFrame, scatter_df: pd.DataFrame) -> Tabs:
        """
        Create all application tabs.
        
        Args:
            line_df: DataFrame for line plots (daily and cumulative)
            scatter_df: DataFrame for scatter plot
            
        Returns:
            Tabs widget containing all panels
        """
        daily_tab = self._create_daily_tab(line_df)
        cumulative_tab = self._create_cumulative_tab(line_df)
        scatter_tab = self._create_scatter_tab(scatter_df)
        
        return Tabs(tabs=[daily_tab, cumulative_tab, scatter_tab])
    
    def _create_daily_tab(self, df: pd.DataFrame) -> TabPanel:
        """
        Create daily progression tab.
        
        Args:
            df: DataFrame with daily data
            
        Returns:
            TabPanel for daily progression
        """
        return self.daily_plot.create_panel(df)
    
    def _create_cumulative_tab(self, df: pd.DataFrame) -> TabPanel:
        """
        Create cumulative progression tab.
        
        Args:
            df: DataFrame with cumulative data
            
        Returns:
            TabPanel for cumulative progression
        """
        return self.cumulative_plot.create_panel(df)
    
    def _create_scatter_tab(self, df: pd.DataFrame) -> TabPanel:
        """
        Create scatter progression tab.
        
        Args:
            df: DataFrame with scatter data
            
        Returns:
            TabPanel for scatter progression
        """
        return self.scatter_plot.create_panel(df)

