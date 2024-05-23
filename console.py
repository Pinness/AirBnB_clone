import cmd 

class MyConsole (cmd.Cmd):
    def cmdloop(self):
        self.prompt = 'Piness >>>  '
        return cmd.Cmd.cmdloop(self)


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
        """ Enters a new line"""

        pass #do nothing when an empty line is entered


    #handle wrong commands
    def default(self, arg):
        print(f"Unknown Command: {arg}")


if __name__ == '__main__':
    MyConsole().cmdloop()

