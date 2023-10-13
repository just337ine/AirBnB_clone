#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """
        Set up method for the test class.
        """
        self.place = Place()

    def test_instance_creation(self):
        """
        Test if the instance is of type Place.
        """
        self.assertIsInstance(self.place, Place)

    # Testing string attributes
    def test_city_id_initialization(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id_initialization(self):
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name_initialization(self):
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description_initialization(self):
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

    # Testing integer attributes
    def test_number_rooms_initialization(self):
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_initialization(self):
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_initialization(self):
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_initialization(self):
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

    # Testing float attributes
    def test_latitude_initialization(self):
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_initialization(self):
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)

    # Testing list attributes
    def test_amenity_ids_initialization(self):
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
