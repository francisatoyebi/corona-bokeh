"""Widget creation factory following Factory Pattern."""

from bokeh.models import Select, CheckboxGroup, DateSlider, Button
import pandas as pd


class WidgetFactory:
    """Factory for creating Bokeh widgets with consistent configuration."""
    
    @staticmethod
    def create_country_selector(countries: list, default: str, title: str = 'Distribution') -> Select:
        """
        Create a country selection dropdown.
        
        Args:
            countries: List of country names
            default: Default selected country
            title: Widget title
            
        Returns:
            Select widget
        """
        return Select(options=countries, value=default, title=title)
    
    @staticmethod
    def create_continent_checkbox(continents: list, active_indices: list = None) -> CheckboxGroup:
        """
        Create a continent checkbox group.
        
        Args:
            continents: List of continent names
            active_indices: List of initially active indices
            
        Returns:
            CheckboxGroup widget
        """
        if active_indices is None:
            active_indices = [0, 1] if len(continents) >= 2 else [0]
        
        return CheckboxGroup(labels=continents, active=active_indices)
    
    @staticmethod
    def create_date_slider(min_date, max_date, initial_date=None, title: str = "Date: ") -> DateSlider:
        """
        Create a date slider widget.
        
        Args:
            min_date: Minimum date
            max_date: Maximum date
            initial_date: Initial selected date (defaults to max_date)
            title: Widget title
            
        Returns:
            DateSlider widget
        """
        if initial_date is None:
            initial_date = max_date
        
        return DateSlider(
            title=title,
            start=min_date,
            end=max_date,
            value=initial_date,
            step=1
        )
    
    @staticmethod
    def create_play_button(width: int = 60) -> Button:
        """
        Create a play/pause button for animations.
        
        Args:
            width: Button width in pixels
            
        Returns:
            Button widget
        """
        return Button(label='► Play', width=width)

