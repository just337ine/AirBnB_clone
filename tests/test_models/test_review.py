#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        """Sets up the testing environment, creating a new Review instance."""
        self.review = Review()

    def tearDown(self):
        """Tears down the testing environment."""
        del self.review

    def test_instance_creation(self):
        """Tests if the instance is created correctly."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Tests if Review class inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute_initialization(self):
        """Tests if the attributes are initialized correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
