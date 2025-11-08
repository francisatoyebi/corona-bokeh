"""Base plot class following Open/Closed Principle."""

from abc import abstractmethod
import pandas as pd
from bokeh.models import ColumnDataSource
from visualization.interfaces import IPlot
from visualization.styles import PlotStyleManager
from config.settings import AppSettings
from data.processors import DataProcessor


class BasePlot(IPlot):
    """Abstract base class for all plot types."""
    
    def __init__(self, settings: AppSettings):
        """
        Initialize base plot.
        
        Args:
            settings: Application settings
        """
        self.settings = settings
        self.style_manager = PlotStyleManager(settings.plot)
        self.processor = DataProcessor()
    
    @abstractmethod
    def create_panel(self, df: pd.DataFrame):
        """Create panel - must be implemented by subclasses."""
        pass
    
    def create_data_source(self, df: pd.DataFrame) -> ColumnDataSource:
        """
        Convert DataFrame to ColumnDataSource.
        
        Args:
            df: Source DataFrame
            
        Returns:
            ColumnDataSource for plotting
        """
        return self.processor.to_column_data_source(df)

