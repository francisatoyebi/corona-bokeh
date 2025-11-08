"""Domain models for COVID-19 data."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CovidDataModel:
    """Represents COVID-19 data for a specific country and date."""
    
    country: str
    date: datetime
    confirmed_cases: int
    recovered_cases: int
    death_cases: int
    daily_confirmed: Optional[int] = None
    daily_recovered: Optional[int] = None
    daily_death: Optional[int] = None
    continent: Optional[str] = None
    
    def __post_init__(self):
        """Validate data integrity."""
        if self.confirmed_cases < 0:
            raise ValueError("Confirmed cases cannot be negative")
        if self.recovered_cases < 0:
            raise ValueError("Recovered cases cannot be negative")
        if self.death_cases < 0:
            raise ValueError("Death cases cannot be negative")

