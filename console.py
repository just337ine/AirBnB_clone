#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
