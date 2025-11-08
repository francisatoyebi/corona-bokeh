"""Interfaces for data layer following Dependency Inversion Principle."""

from abc import ABC, abstractmethod
import pandas as pd


class IDataLoader(ABC):
    """Interface for data loading operations."""
    
    @abstractmethod
    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load data from specified file path.
        
        Args:
            file_path: Path to the data file
            
        Returns:
            DataFrame containing the loaded data
        """
        pass
    
    @abstractmethod
    def validate(self, df: pd.DataFrame) -> bool:
        """
        Validate loaded data structure.
        
        Args:
            df: DataFrame to validate
            
        Returns:
            True if valid, False otherwise
        """
        pass

