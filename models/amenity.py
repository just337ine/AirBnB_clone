#!/usr/bin/python3
"""
simple Class amenity function
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing amenities like WiFi, pool, etc.
    """
    name = ""
