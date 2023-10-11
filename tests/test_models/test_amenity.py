#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_initialization(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_name_initial_value(self):
        self.assertEqual(self.amenity.name, "")
