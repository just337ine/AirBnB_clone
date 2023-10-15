#!/usr/bin/python3
"""
class review for user review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing a review by a user for a place.
    """
    place_id = ""  # it will be the Place.id
    user_id = ""   # it will be the User.id
    text = ""
