#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_creation(self):
        """Test for checking creation of BaseModel instance"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_method(self):
        """Test to check the __str__ method of BaseModel"""
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(expected_output, str(my_model))

    def test_save_method(self):
        """Test to check save method of BaseModel"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test to check to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertTrue(type(my_model_dict["created_at"]) is str)
        self.assertTrue(type(my_model_dict["updated_at"]) is str)

    def test_create_instance_from_dict(self):
        """Test the creation of an instance from a dictionary"""
        my_model = BaseModel()
        my_model.name = "MyModel"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        # Assert the new model has the same id and attributes, but is not the same object
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertNotEqual(my_model, my_new_model)

    def test_datetime_format(self):
        """Test datetime format in dictionary"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        created_at = datetime.strptime(
            my_model_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        self.assertTrue(isinstance(created_at, datetime))
        updated_at = datetime.strptime(
            my_model_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        self.assertTrue(isinstance(updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
