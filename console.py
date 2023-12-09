#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter
"""
import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A class that defines the command interpreter

    Attributes:
        prompt (str)
    """

    prompt = "(hbnb)"
    __classes = {"BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"}
    __commands = {"quit", "EOF", "help",
                  "create", "show", "destroy",
                  "all", "update"}

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

    def do_create(self, type_model):
        """A method that creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            dict = {'BaseModel': BaseModel, 'User': User,
                    'State': State, 'City': City,
                    'Amenity': Amenity, 'Place': Place,
                    'Review': Review}
            my_model = dict[type_model]()
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """A method that prints all string
        representation of all instances
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
