#!/usr/bin/python3
import cmd
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """hbnb class definition """
    prompt = '(hbnb) '

    #  _________Commands:
    def do_quit(self, line):
        """
        Exit the command loop
        """
        print()
        return True

    def do_EOF(self, line):
        """
        Handle EOF (ctrl+D) by exiting
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel or User
        """
        if not line:
            print("** class name missing **")
        elif line == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif line == "User":    # Handle User instances
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        elif line == "Place":
            new_instance = Place()
            new_instance.save()
            print(new_instance.id)
        elif line == "State":
            new_instance = State()
            new_instance.save()
            print(new_instance.id)
        elif line == "City":
            new_instance = City()
            new_instance.save()
            print(new_instance.id)
        elif line == "Amenity":
            new_instance = Amenity()
            new_instance.save()
            print(new_instance.id)
        elif line == "Review":
            new_instance = Review()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
            Prints the string representation of an instance
        """
        args_list = line.split()
        if not line:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State",
                                  "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id
        """
        args_list = line.split()
        if not line:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State",
                                  "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_count(self, line):
        """
            Count the number of instances of a specific class
        """
        lines = line.split()
        if not lines:
            print("** class name missing **")
        elif lines[0] not in ["BaseModel", "User", "Place", "State",
                              "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            class_name = lines[0]
            count = sum(
                    1 for key in storage.all()
                    if key.split('.')[0] == class_name
                    )
            print(count)

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        if line and line not in ["BaseModel", "User", "Place", "State",
                                 "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            all_objects = [str(obj) for obj in storage.all().values()]
            print(all_objects)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        args_list = line.split()
        if not line:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State",
                                  "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                attr_name = args_list[2]
                attr_value = args_list[3]
                # remove quotes from attr_value
                if attr_value[0] == '"' and attr_value[-1] == '"':
                    attr_value = attr_value[1:-1]
                    setattr(storage.all()[key], attr_name, attr_value)
                    storage.all()[key].save()

#    def do_clear(self, line):
#        """
#        Clear the terminal.
#        """
#        os.system('cls' if os.name == 'nt' else 'clear')

    def default(self, line):
        """
            Method to handle <class name>.<method name>() format.
        """
        line_parts = line.split('.')
        if len(line_parts) != 2:
            print("** class doesn't exist **")
            return
        class_name = line_parts[0]
        method_and_args = line_parts[1].split('(')
        method_name = method_and_args[0]
        # Handle 'all' method
        if method_name == "all()":
            if class_name in ["BaseModel", "User", "Place", "State",
                              "City", "Amenity", "Review"]:
                objects = storage.all(class_name)
                list_objs = [str(v) for k, v in objects.items()
                             if k.startswith(class_name)]
                print(list_objs)
            else:
                print("** class doesn't exist **")
        # Handle 'count()' method
        elif method_name == "count()":
            if class_name in ["BaseModel", "User", "Place", "State",
                              "City", "Amenity", "Review"]:
                objects = storage.all(class_name)
                print(len(objects))
            else:
                print("** class doesn't exist **")
        # Handle 'show' method
        elif method_name == "show":
            if len(method_and_args) != 2:
                print("** instance id missing **")
                return
            instance_id = method_and_args[1].split(')')[0].replace('"', '')
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])
        elif method_name == "destroy":
            if len(method_and_args) != 2:
                print("** instance id missing **")
                return
            instance_id = method_and_args[1].split(')')[0].replace('"', '')
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        # Handle 'update' method
        elif method_name == "update":
            args_split = method_and_args[1].split('), ')
            if len(args_split) != 2:
                print("** invalid format **")
                return
            instance_id = args_split[0].split(')')[0].replace('"', '')
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            dict_str = args_split[1].replace("'", '"')
            try:
                update_dict = json.loads(dict_str)
                if not isinstance(update_dict, dict):
                    raise Exception()
            except Exception:
                print("** unable to process dictionary **")
                return
            for attr, value in update_dict.items():
                setattr(storage.all()[key], attr, value)
                storage.all()[key].save()
        else:
            print("** method doesn't exist **")

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass

    # __________Helps:
    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        print("Quit the command loop by typing EOF or Ctrl+D.")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
