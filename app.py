"""
COVID-19 Dashboard Application Entry Point

A Bokeh dashboard for visualizing COVID-19 data with interactive plots.
Refactored to follow SOLID principles.

Usage:
    bokeh serve --show app.py
"""

from config.settings import AppSettings
from ui.dashboard import Dashboard


# Initialize and run the dashboard
# This code runs at module level for Bokeh server
settings = AppSettings()
dashboard = Dashboard(settings)
dashboard.run()
