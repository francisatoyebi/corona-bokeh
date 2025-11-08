"""Domain layer - Business models and entities."""

from .models import CovidDataModel
from .enums import PlotType, DataType

__all__ = ['CovidDataModel', 'PlotType', 'DataType']

