#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel"}

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
