#!/usr/bin/python3

"""
models/__init__.py
------------------
This module initializes the `storage` instance for your application.
Upon initialization, it sets up a new instance of the FileStorage class,
which provides methods for serialization and deserialization of objects.
The storage instance then reloads any previously
serialized objects if available.
"""

# Importing the FileStorage class from the engine module.
# FileStorage handles the serialization and deserialization of instances.
from models.engine.file_storage import FileStorage

"""
 Create an instance of the FileStorage class.
 This instance will be the primary object for serialization
 and deserialization tasks in the application.
"""
storage = FileStorage()

# Call the `reload` method on the `storage` instance.
# This method deserializes the JSON file back to the Python objects.
# If the file doesn't exist or there's an error, it does nothing.
storage.reload()
