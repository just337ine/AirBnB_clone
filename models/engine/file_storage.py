#!/usr/bin/python3
import json
import re
#from models.base_model import BaseModel
#from models.user import User
#from models.place import Place
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.review import Review


class FileStorage:
    """
    A class that handles the Serialization and Deserialization of instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary storing all objects by <class name>.id.

    Methods:
        all(): Return the dictionary __objects.
        new(obj): Add the object to the __objects dictionary.
        save(): Serialize the __objects to a JSON file.
        reload(): Deserialize the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, class_name=None):
        """
        Returns:
            dict: The dictionary of __objects,
            optionally filtered by class name.
        """
        if class_name:
            return {k: v for k, v in FileStorage.__objects.items()
                    if class_name == k.split('.')[0]}
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_obj = {
                    k: v.to_dict() for k, v in FileStorage.__objects.items()
                    }
            json.dump(dict_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to the __objects dictionary.

        Note:
            If the JSON file does not exist, the method silently
            passes and does nothing.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value["__class__"]
                    # Dynamically import the class based on its name
                    words = [word.lower() for word in
                             re.findall(r'[A-Z][^A-Z]*', cls_name)]
                    module_name = "models.{}".format('_'.join(words))
                    exec("from {} import {}".format(module_name, cls_name))
                    instance = eval(cls_name)(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass

        def classes(self):
            """
            Return a dictionary of available classes for the
            deserialization process.
            Update this dictionary as new classes are added.
            """
            classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
            }
            return classes

