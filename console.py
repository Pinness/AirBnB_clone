#!/usr/bin/python3

import cmd 
from models.base_model4 import BaseModel
from models.engine.file_storage  import FileStorage
from models import storage


class MyConsole (cmd.Cmd):
    classes = ["BaseModel"]




    def __init__(self):
        super().__init__()
        self.prompt = 'Piness >>> '
        #self.storage = storage


    def cmdloop(self):
        return super().cmdloop()


    #prompt = 'Piness >>>  '   #display prompt
    #def do_quit(self, arg):

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        """ Exits the program"""
        print()
        return True # exit program wshen user trigger EOF


    def do_help(self, arg):
        if arg == 'quit':
            print('Quit command to exit the program')

        elif arg == '':
            print('''Welcome to MyConsole!\n\nDocumented commands (type help <topic>):
            ========================================')
                    'Available commands:\n    help - Provide assistance\n    quit - Exit the program\n    EOF - Exit the program''')

         
        else:
             cmd.Cmd.do_help(self, arg)


    def emptyline(self):
        """ Enters a new line """

        pass #do nothing when an empty line is entered


    #handle wrong commands
    def default(self, arg):
        print(f"Unknown Command: {arg}")

   

    def do_create(self, arg):
        """ Creates a new instance and prints the ID"""
        class_name = arg.strip()

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in globals():
            print("** class doesn't exist **")
            return


        new_instance = globals()[class_name]()

        storage.new(new_instance)
        storage.save()


        #print the id of the created instance
        print(new_instance.id)

    def do_show(self, arg):
        #retrieve classname and id from arg
        arg = arg.split(" ")
        print(arg)
        print(len(arg))
        if len(arg) < 2:
            print("class name or instance id missing")
            return


        class_name = arg[0]
        instance_id = arg[1]

        #check if class name is given
        if not class_name:
            print("** class name missing **")
            return

        #chevck if classname exist
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        #check if id is given
        if not instance_id:
            print("** instance id missing **")
            return

        #check if the instance exist in the storage
        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return


        # Retrieve the instance from storage and print
        instance_dict = storage.all()[instance_key]
        print(instance_dict)




if __name__ == '__main__':
    MyConsole().cmdloop()
