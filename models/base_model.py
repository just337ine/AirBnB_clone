#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base model class with common attributes and methods for other classes.
    """

    # Initialization of the instance attributes
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    """
                    Convert string representation of datetime to
                    datetime object
                    """
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            # Set 'id' if it exists in kwargs, or generate a new one
            if 'id' not in kwargs:
                self.id = str(uuid4())
        else:
            # Generate an ID as a string
            self.id = str(uuid.uuid4())
            # Current datetime when an instance is create
            self.created_at = datetime.now()
            # Updated whenever an object is created or updated
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        # Creating a copy to not alter the orignal __dict__
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__

        # Format 'created _at' and 'updated_at' as ISO strings
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
