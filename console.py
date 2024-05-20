#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from re import search


class HBNBCommand(cmd.Cmd):
    """
    Class that defines the command interpreter
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        """Exit the program with Ctrl+D"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.list_classes:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[id_object]
                storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        element_list = []
        args_list = shlex.split(arg)
        if not args_list:
            for value in storage.all().values():
                element_list.append(str(value))
            print(element_list)
        elif args_list[0] in HBNBCommand.list_classes:
            for value in storage.all().values():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            elif (len(args_list) == 3 and args_list[2].startswith("{") and
                  args_list[2].endswith("}")):
                # Handle dictionary input
                try:
                    attributes = eval(args_list[2])
                    if isinstance(attributes, dict):
                        instance = storage.all()[id_object]
                        for key, value in attributes.items():
                            setattr(instance, key, value)
                        instance.save()
                    else:
                        print("** attribute name missing **")
                except Exception:
                    print("** invalid dictionary **")
            elif len(args_list) < 3:
                print("** attribute name missing **")
            elif len(args_list) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[id_object]
                attr_name = args_list[2]
                attr_value = args_list[3]
                try:
                    if hasattr(instance, attr_name):
                        attr_type = type(getattr(instance, attr_name))
                        if attr_type == int:
                            attr_value = int(attr_value)
                        elif attr_type == float:
                            attr_value = float(attr_value)
                    else:
                        if attr_value.isdigit():
                            attr_value = int(attr_value)
                        else:
                            try:
                                attr_value = float(attr_value)
                            except ValueError:
                                pass
                except ValueError:
                    pass
                setattr(instance, attr_name, attr_value)
                instance.save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        for key in storage.all().keys():
            if key.split(".")[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """
            Method called on an input line when the command prefix
            is not recognized
        """
        args_list = arg.split(".", 1)
        if args_list[0] in HBNBCommand.list_classes:
            method = args_list[1].split("(")[0]
            if method == "all":
                return self.do_all(args_list[0])
            elif method == "count":
                return self.do_count(args_list[0])
            elif method == "show":
                id_show = args_list[1].split('"')[1]
                args_show = "{} {}".format(args_list[0], id_show)
                return self.do_show(args_show)
            elif method == "destroy":
                id_destroy = args_list[1].split('"')[1]
                args_destroy = "{} {}".format(args_list[0], id_destroy)
                return self.do_destroy(args_destroy)
            elif method == "update":
                part1 = args_list[1].replace(")", "")
                check_dict = part1.split(", ")
                if check_dict[1][0] == "{":
                    class_id = check_dict[0].replace('"', "")
                    attributes = eval(part1.split(", ", 1)[1])
                    for attr_name, attr_value in attributes.items():
                        args_update = "{} {} {} {}".format(
                            args_list[0], class_id, attr_name, attr_value)
                        self.do_update(args_update)
                else:
                    args_update = "{} {}".format(args_list[0],
                                                 part1.replace('"', ""))
                    return self.do_update(args_update)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
