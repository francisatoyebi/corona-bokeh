"""Application configuration settings."""

from dataclasses import dataclass
from os.path import dirname, join, abspath


@dataclass
class PlotSettings:
    """Settings for plot styling and dimensions."""
    
    # Main plot dimensions
    main_plot_width: int = 1000
    main_plot_height: int = 700
    
    # Sub plot dimensions
    sub_plot_width: int = 700
    sub_plot_height: int = 300
    
    # Small plot dimensions
    small_plot_width: int = 500
    small_plot_height: int = 200
    
    # Font sizes - main plots
    title_font_size: str = '20pt'
    axis_label_font_size: str = '14pt'
    tick_label_font_size: str = '12pt'
    
    # Font sizes - small plots
    small_title_font_size: str = '10pt'
    small_axis_label_font_size: str = '7pt'
    small_tick_label_font_size: str = '6pt'
    
    # Font styles
    title_font: str = 'serif'
    axis_label_style: str = 'bold'
    
    # Colors
    confirmed_color: str = 'orange'
    recovered_color: str = 'green'
    death_color: str = 'red'
    line_color: str = 'gray'
    hover_color: str = 'purple'
    
    # Glyph settings
    default_glyph_size: int = 7
    small_glyph_size: int = 5
    fill_alpha: float = 0.7
    hover_alpha: float = 1.0


@dataclass
class DataSettings:
    """Settings for data files and paths."""
    
    base_dir: str = dirname(dirname(abspath(__file__)))
    data_dir: str = 'data'
    
    # Data file names
    line_data_file: str = 'imp_line_covid.csv'
    scatter_data_file: str = 'github_cool_covid.csv'
    
    # Date format (CSV files use dashes, not slashes)
    date_format: str = "%Y-%m-%d"
    
    def get_line_data_path(self) -> str:
        """Get full path to line plot data file."""
        return join(self.base_dir, self.data_dir, self.line_data_file)
    
    def get_scatter_data_path(self) -> str:
        """Get full path to scatter plot data file."""
        return join(self.base_dir, self.data_dir, self.scatter_data_file)


@dataclass
class AppSettings:
    """Main application settings."""
    
    app_title: str = 'Corona'
    default_country: str = 'Afghanistan'
    animation_interval: int = 200  # milliseconds
    
    plot: PlotSettings = None
    data: DataSettings = None
    
    def __post_init__(self):
        """Initialize nested settings."""
        if self.plot is None:
            self.plot = PlotSettings()
        if self.data is None:
            self.data = DataSettings()

