import cmd

class MyConsole(cmd.Cmd):
    def do_quit(self, arg):
        return True #exit when the user type quit


    def do_EOF(self, arg):
        return True # exit program wshen user trigger EOF

    def do_help(self, arg):
        print('Welcome to MyConsole')
        print('Available commands:\n    quit - Exit the program\n    EOF - Exit the program')

    def help_quit(self):
        print('Quit command to exit the program')

    def prompt(self):
        return 'Piness >>>  ' #cusom prompt

    def do_emptyline(self):
        pass #do nothing when an empty line is entered


if __name__ == '__main__':
        MyConsole().cmdloop()
