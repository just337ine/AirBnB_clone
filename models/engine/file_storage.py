#!/usr/bin/python3
import json
import importlib


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
    class_to_module_map = {
        'BaseModel': 'base_model',
        'User': 'user' 
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: The dictionary __objects.
        """
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
                    if cls_name == "BaseModel":
                        # Dynamically import the class based on its name
                        module_name = class_to_module_map.get(cls_name, cls_name.lower())
                        module = importlib.import_module("models." + module_name)
                        cls = getattr(module, cls_name)
                        
                    instance = eval(cls_name)(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
