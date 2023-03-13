#!/usr/bin/python3
"""now the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB."""

    md_dic = {
        'BaseModel': BaseModel,
        'User': User,
    }
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """quits from the program"""
        return True

    def do_quit(self, line):
        """quit program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line: str):

        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.md_dic.keys():
            model = self.md_dic[line.split(" ")[0]]
            bm = model()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line: str):

        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.md_dic.keys():
            if len(line.split(" ")) > 1:
                m, i = line.split(" ")
                data = storage.all()
                key = ".".join((m, i))
                if key in data.keys():

                    print(data[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):

        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.md_dic.keys():
            if len(line.split(" ")) > 1:
                m, i = line.split(" ")
                data = storage.all()
                key = ".".join((m, i))
                if key in data.keys():
                    storage.destroy(key)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """."""

        data = storage.all()
        li = []
        if line == "":
            li = [item.__str__() for item in data.values()]
            print(li)
        elif line.split(" ")[0] in self.md_dic.keys():
            for key, value in data.items():
                if key.split(".")[0] == line.split(" ")[0]:
                    li.append(value.__str__())
            print(li)
        else:
            print("** class doesn't exist **")

    def do_update(self, line: str):
        """..."""

        spl = line.split()
        if len(spl) < 1:
            print("** class name missing **")
        elif len(spl) < 2:
            print("** instance id missing **")
        elif len(spl) < 3:
            print("** attribute name missing **")
        elif len(spl) < 4:
            print("** value missing **")

        else:
            if spl[0] in self.md_dic.keys():
                key = ".".join((spl[0], spl[1]))
                data = storage.all()
                if key in data.keys():
                    obj = data[key]
                    setattr(obj, spl[2], spl[3])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
