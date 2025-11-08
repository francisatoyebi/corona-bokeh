"""Main dashboard coordinator following Single Responsibility Principle."""

from bokeh.io import curdoc
from config.settings import AppSettings
from data.loaders import CSVDataLoader
from .tab_manager import TabManager


class Dashboard:
    """Coordinates the main application dashboard."""
    
    def __init__(self, settings: AppSettings):
        """
        Initialize dashboard.
        
        Args:
            settings: Application settings
        """
        self.settings = settings
        self.data_loader = CSVDataLoader(
            date_column='Date',
            date_format=settings.data.date_format
        )
        self.tab_manager = TabManager(settings)
    
    def load_data(self):
        """
        Load all required data files.
        
        Returns:
            Tuple of (line_df, scatter_df)
        """
        line_df = self.data_loader.load(self.settings.data.get_line_data_path())
        scatter_df = self.data_loader.load(self.settings.data.get_scatter_data_path())
        
        return line_df, scatter_df
    
    def create_dashboard(self):
        """
        Create and configure the complete dashboard.
        
        Returns:
            Tabs widget with all panels
        """
        line_df, scatter_df = self.load_data()
        tabs = self.tab_manager.create_tabs(line_df, scatter_df)
        
        return tabs
    
    def run(self):
        """Run the dashboard application."""
        tabs = self.create_dashboard()
        
        curdoc().add_root(tabs)
        curdoc().title = self.settings.app_title

