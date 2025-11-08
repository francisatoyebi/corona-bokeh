"""Data layer - Data loading and processing."""

from .interfaces import IDataLoader
from .loaders import CSVDataLoader
from .processors import DataProcessor

__all__ = ['IDataLoader', 'CSVDataLoader', 'DataProcessor']

