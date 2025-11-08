"""Concrete implementations of data loaders."""

import pandas as pd
from .interfaces import IDataLoader


class CSVDataLoader(IDataLoader):
    """Loads COVID-19 data from CSV files."""
    
    def __init__(self, date_column: str = 'Date', date_format: str = "%Y/%m/%d"):
        """
        Initialize CSV data loader.
        
        Args:
            date_column: Name of the date column
            date_format: Format string for date parsing
        """
        self.date_column = date_column
        self.date_format = date_format
    
    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load CSV data and parse dates.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            DataFrame with parsed dates
        """
        df = pd.read_csv(file_path, index_col=0).dropna()
        
        if self.date_column in df.columns:
            df[self.date_column] = pd.to_datetime(
                df[self.date_column], 
                format=self.date_format
            )
        
        return df
    
    def validate(self, df: pd.DataFrame) -> bool:
        """
        Validate DataFrame structure.
        
        Args:
            df: DataFrame to validate
            
        Returns:
            True if valid
        """
        if df is None or df.empty:
            return False
        
        required_columns = [self.date_column]
        return all(col in df.columns for col in required_columns)

