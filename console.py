#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
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

    # List of available classes
    classes = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            ]

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
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(lines[0], lines[1])
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found  **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            lines = line.split()
            if lines[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(lines) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(lines[0], lines[1])
                instance = storage.all().get(key)
                if instance:
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, line):
        """
            Count the number of instances of a specific class
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            count = sum(
                    1 for key in storage.all()
                    if key.split('.')[0] == line
                    )
            print(count)

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        objects = storage.all()
        if not line:
            all_objects = [str(obj) for obj in objects.values()]
            print(all_objects)
        elif line in self.classes:
            print([str(obj) for key,
                   obj in objects.items() if key.startswith(line)])
        else:
            print("** class doesn't exist **")

    def parseline(self, line):
        """
        Input line parser
        """
        if '(' in line and ')' in line:
            line_args = line.split('.')
            cls_name = line_args[0]
            command_args = line_args[1].split('(')
            command = command_args[0]
            args = command_args[1]
            if '{' in args and '}' in args:
                start = args.find('{')
                end = args.find('}')
                dict_string = args[start:end + 1]
                new_line = args.replace(args[start:end + 1], '')
                id_arg = new_line.strip('", )')
                arg = "{} {} {}".format(cls_name, id_arg, dict_string)
                new_line = "{} {}".format(command, arg)
                return (command, arg, new_line)

            args_list = command_args[1].split()
            args_list = [arg.strip('",)') for arg in args_list]
            args = " ".join(args_list)
            if len(args) > 0:
                arg = "{} {}".format(cls_name.strip(' '), args)
            else:
                arg = cls_name
            new_line = "{} {}".format(command, arg)
            return (command, arg, new_line)
        else:
            return cmd.Cmd.parseline(self, line)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        elif len(lines) < 3:
            print("** attribute name missing **")
        elif len(lines) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(lines[0], lines[1])
            instance = storage.all().get(key)
            if instance:
                attr_name = lines[2]
                attr_value = lines[3].strip('"')
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")

    def do_clear(self, line):
        """
        Clear the terminal.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

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
            if class_name in self.classes:
                objects = storage.all(class_name)
                list_objs = [str(v) for k, v in objects.items()
                             if k.startswith(class_name)]
                print(list_objs)
            else:
                print("** class doesn't exist **")

        # Handle 'count()' method
        elif method_name == "count()":
            if class_name in self.classes:
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
