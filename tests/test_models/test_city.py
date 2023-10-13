#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_instance_creation(self):
        self.assertIsInstance(self.city, City)

    def test_name_initialization(self):
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
