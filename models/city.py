#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city within a state
    """
    state_id = ""   # it will be the State.id
    name = ""
