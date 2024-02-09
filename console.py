#!/usr/bin/python3
"""Entry point of the command interpreter for HBNB."""

import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel
import ast


class HBNBCommand(cmd.Cmd):
    """Interactive command interpreter for HBNB."""

    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF signal."""
        return True

    def emptyline(self):
        """Do nothing on empty lines."""
        pass

    def default(self, line):
        """Default method to handle unknown commands."""
        print("Unknown command '{}'".format(line))

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        if arg:
            # Try to find a matching command and call its .__doc__ attribute
            if arg in self.get_names():
                func = getattr(self, "do_" + arg)
                print(func.__doc__)
                return
        # No specific command given; print all commands
        cmd.Cmd.do_help(self, arg)

    def do_create(self, line):
        """Creates a new instance of BaseModel."""
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = self.classes[command]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        instance = storage.all().get(instance_key)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances, optionally filtered by class name."""
        args = arg.split()
        if not args:
            instances = storage.all()
        elif args[1] not in globals():
            print("** class doesn't exist **")
            return
        else:
            instances = {
                k: v for k, v in storage.all().items() if k.startswith(args[0])
            }
        print([str(v) for v in instances.values()])

    def do_update(self, arg):
        """Update an instance with a new attribute value."""
        args = arg.split()
        if not args[1]:
            print("** class name missing **")
            return
        class_name, instance_id, attr_name = args[:5]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[instance_key]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update immutable fields **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_value = args[4]
        try:
            attr_value = ast.literal_eval(attr_value)
        except (ValueError, SyntaxError) as e:
            print("** value parsing error **")
            return
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
