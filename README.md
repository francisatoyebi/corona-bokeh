# Corona Bokeh Dashboard

An interactive COVID-19 data visualization dashboard built with Bokeh.

### Project Structure

```
corona-bokeh/
├── app.py                          # Application entry point
├── config/                         # Configuration layer
│   ├── __init__.py
│   └── settings.py                 # Application settings
├── domain/                         # Domain layer (business models)
│   ├── __init__.py
│   ├── enums.py                    # Domain enumerations
│   └── models.py                   # Data models
├── data/                           # Data layer
│   ├── __init__.py
│   ├── interfaces.py               # Data loader interfaces
│   ├── loaders.py                  # CSV data loader implementation
│   └── processors.py               # Data processing utilities
├── visualization/                  # Visualization layer
│   ├── __init__.py
│   ├── interfaces.py               # Plot interfaces
│   ├── styles.py                   # Centralized styling
│   ├── plots/                      # Plot implementations
│   │   ├── __init__.py
│   │   ├── base_plot.py            # Abstract base plot
│   │   ├── cumulative_plot.py      # Cumulative progression plot
│   │   ├── daily_plot.py           # Daily progression plot
│   │   └── scatter_plot.py         # Scatter plot with animation
│   └── components/                 # Reusable UI components
│       ├── __init__.py
│       └── widgets.py              # Widget factory
├── ui/                             # UI coordination layer
│   ├── __init__.py
│   ├── tab_manager.py              # Tab management
│   └── dashboard.py                # Main dashboard coordinator
└── data/                           # Data files
    └── *.csv
```

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd corona-bokeh

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the Bokeh server:

```bash
bokeh serve --show app.py
```

The dashboard will open in your default browser with three interactive tabs:

1. **Daily Progression**: Daily COVID-19 statistics by country
2. **Cumulative Progression**: Cumulative COVID-19 statistics by country
3. **Progression**: Animated scatter plot showing cases vs recoveries by continent

## Features

- **Interactive Country Selection**: Choose any country to view its COVID-19 data
- **Multiple Visualizations**: Daily, cumulative, and comparative views
- **Animated Scatter Plot**: Watch the progression over time with play/pause controls
- **Continent Filtering**: Filter data by continent
- **Date Range Selection**: Explore data across different time periods
- **Responsive Tooltips**: Hover over data points for detailed information

## Dependencies

- Python 3.7+
- Bokeh 3.3.4
- Pandas 2.2.0
- NumPy 1.26.4
- BeautifulSoup4 4.12.3
- Other dependencies in `requirements.txt`

## Design Patterns Used

1. **Factory Pattern**: `WidgetFactory` for creating UI widgets
2. **Strategy Pattern**: Different plot implementations for different views
3. **Dependency Injection**: Settings and dependencies injected through constructors
4. **Facade Pattern**: `Dashboard` provides simplified interface to complex subsystems

## Code Quality

- All classes follow Single Responsibility Principle
- No file exceeds 200 lines
- Clear separation between layers
- Interfaces for abstraction and extensibility
- Comprehensive docstrings for all public methods

## Extending the Application

### Adding a New Plot Type

1. Create a new class extending `BasePlot` in `visualization/plots/`
2. Implement the `create_panel()` method
3. Add the plot to `TabManager.create_tabs()`

### Adding a New Data Source

1. Implement the `IDataLoader` interface
2. Add loader logic in new class
3. Inject into `Dashboard` constructor

### Modifying Styling

All styling is centralized in `config/settings.py` - modify `PlotSettings` class.
