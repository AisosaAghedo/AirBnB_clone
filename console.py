#!/usr/bin/python3
""" Holberton AirBnB console module """
import cmd
import sys
import models
from models.base_model import BaseModel
import shlex

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """ HBNB class """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ exit the program """
        exit()

    def do_EOF(self, arg):
        """ exit the program """
        print('')
        exit()

    def emptyline(self):
        """ shouldn't execute anthing """
        pass

    def do_create(self, arg):
        """
         Creates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id
         """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        if cmd_args[0] in classes:
            new_instance = classes[cmd_args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        if cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = cmd_args[0] + "." + cmd_args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name
         and id (save the change into the JSON file
         """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = cmd_args[0] + "." + cmd_args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
         Prints all string representation of all
         instances based or not on the class name
         """
        cmd_args = shlex.split(arg)
        obj_list = []
        if len(cmd_args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif cmd_args[0] in classes:
            for key in models.storage.all():
                if cmd_args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file)"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
