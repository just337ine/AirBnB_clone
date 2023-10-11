import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        # Ensure the 'all' method returns a dictionary
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        # Ensure the 'new' method adds an object to __objects
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        # Ensure the 'save' method saves objects to the file
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        self.storage.save()

        # Reload storage and check if objects are in __objects
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(obj1, new_storage.all().values())
        self.assertIn(obj2, new_storage.all().values())

    def test_reload(self):
        # Ensure the 'reload' method loads objects from the file
        obj = BaseModel()
        obj.save()
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())

if __name__ == '__main__':
    unittest.main()

