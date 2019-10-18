class UserManager():
    def __init__(self):
        global ops_map
        ops_map = {
            'c': 'create',
            'd': 'delete',
            'v': 'view',
            'm': 'modify',
            'r': 'return',
            'q': 'quit'
        }

    def ops_choice(self):
        return ops_map[raw_input('''
            Choose a operation:

            (C)reate User
            (D)elete User
            (V)iew User
            (M)odify User
            (R)eturn
            (Q)uit

            Enter choice: ''').strip().lower()[0]]

    def create(self):
        print "createing"
        pass

    def delete(self):
        print "deleteing"
        pass

    def view(self):
        print "viewing"
        pass

    def modify(self):
        print "modifing"
        pass

    def back(self):
        print "backing"
        pass

    def quit(self):
        print "quiting"
        pass
