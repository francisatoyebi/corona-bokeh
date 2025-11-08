"""Data processing utilities following Single Responsibility Principle."""

import pandas as pd
from bokeh.models import ColumnDataSource


class DataProcessor:
    """Processes and transforms COVID-19 data for visualization."""
    
    @staticmethod
    def filter_by_country(df: pd.DataFrame, country: str) -> pd.DataFrame:
        """
        Filter dataframe by country.
        
        Args:
            df: Source dataframe
            country: Country name to filter
            
        Returns:
            Filtered dataframe
        """
        return df[df['Country'] == country].copy()
    
    @staticmethod
    def filter_by_continents(df: pd.DataFrame, continents: list) -> pd.DataFrame:
        """
        Filter dataframe by continent list.
        
        Args:
            df: Source dataframe
            continents: List of continent names
            
        Returns:
            Filtered dataframe
        """
        df_indexed = df.set_index(['continent'])
        return df_indexed.loc[continents].reset_index()
    
    @staticmethod
    def filter_by_date(df: pd.DataFrame, date) -> pd.DataFrame:
        """
        Filter dataframe by specific date.
        
        Args:
            df: Source dataframe
            date: Date to filter
            
        Returns:
            Filtered dataframe
        """
        return df[df['Date'] == date].copy()
    
    @staticmethod
    def get_country_list(df: pd.DataFrame) -> list:
        """
        Get sorted list of unique countries.
        
        Args:
            df: Source dataframe
            
        Returns:
            Sorted list of country names
        """
        countries = list(df['Country'].value_counts().index)
        countries.sort()
        return countries
    
    @staticmethod
    def get_continent_list(df: pd.DataFrame) -> list:
        """
        Get list of unique continents.
        
        Args:
            df: Source dataframe
            
        Returns:
            List of continent names
        """
        return list(df['continent'].unique())
    
    @staticmethod
    def to_column_data_source(df: pd.DataFrame) -> ColumnDataSource:
        """
        Convert DataFrame to Bokeh ColumnDataSource.
        
        Args:
            df: Source dataframe
            
        Returns:
            ColumnDataSource for Bokeh plotting
        """
        return ColumnDataSource(df)

