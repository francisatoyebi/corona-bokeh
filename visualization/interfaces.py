"""Interfaces for visualization layer following Interface Segregation Principle."""

from abc import ABC, abstractmethod
from bokeh.models import TabPanel
import pandas as pd


class IPlot(ABC):
    """Interface for plot creation."""
    
    @abstractmethod
    def create_panel(self, df: pd.DataFrame) -> TabPanel:
        """
        Create a Bokeh panel with the plot.
        
        Args:
            df: DataFrame containing the data to plot
            
        Returns:
            Bokeh TabPanel object
        """
        pass

