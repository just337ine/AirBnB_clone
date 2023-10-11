#!/usr/bin/python3
import cmd
import os
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
    """hbnb class definition"""
    prompt = ' (hbnb) '

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) by exiting."""
        print()  # to print a newline
        return True

    def do_quit(self, arg):
        """Exit the command loop."""
        return True

    def do_shell(self, line):
        """Run a shell command"""
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_create(self, args):
        """Creates a new instance of BaseModel or User"""
        if not args:
            print("** class name missing **")
        elif args == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif args == "User":    # Handle User instances
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        elif args == "Place":
            new_instance = Place()
            new_instance.save()
            print(new_instance.id)
        elif args == "State":
            new_instance = State()
            new_instance.save()
            print(new_instance.id)
        elif args == "City":
            new_instance = City()
            new_instance.save()
            print(new_instance.id)
        elif args == "Amenity":
            new_instance = Amenity()
            new_instance.save()
            print(new_instance.id)
        elif args == "Review":
            new_instance = Review()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        if not args:
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

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        if not args:
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

    def do_all(self, args):
        """Prints all string representation of all instances"""
        if args and args not in ["BaseModel", "User", "Place", "State",
                                 "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            all_objects = [str(obj) for obj in storage.all().values()]
            print(all_objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args_list = args.split()
        if not args:
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

    def do_clear(self, args):
        """Clear the terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def default(self, line):
        """Method to handle <class name>.<method name>() format."""
        line_parts = line.split('.')
        if len(line_parts) != 2:
            print("** class doesn't exist **")
            return
        class_name = line_parts[0]
        method_name = line_parts[1]
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
    
    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for 'EOF' command."""
        print("Quit the command loop by typing EOF or Ctrl+D.")

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
