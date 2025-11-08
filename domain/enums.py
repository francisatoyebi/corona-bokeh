"""Enumerations for domain types."""

from enum import Enum


class PlotType(Enum):
    """Types of plots available in the application."""
    CUMULATIVE = "cumulative"
    DAILY = "daily"
    SCATTER = "scatter"


class DataType(Enum):
    """Types of COVID-19 data metrics."""
    CONFIRMED = "confirmed"
    RECOVERED = "recovered"
    DEATH = "death"

