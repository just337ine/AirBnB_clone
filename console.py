#!/usr/bin/python3
import cmd
import os


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
