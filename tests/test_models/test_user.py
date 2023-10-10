#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_instance(self):
        """Test creation of a User instance"""
        user = User()
        self.assertIsInstance(user, User)
