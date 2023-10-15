#!/usr/bin/python3
"""
class user for user data
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
