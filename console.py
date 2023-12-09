#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A class that defines the command interpreter

    Attributes:
        prompt (str)
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the command interpreter.
        """

        return True

    def do_EOF(self, arg):
        """EOF to exit the program.
        """

        return True

    def help(self):
        """A method that provides a help to the user while,
        inquirying about any command.
        """
        print("A clarifying of a command")

    def emptyline(self):
        """it should do nothing when recieving an empty line
        """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
