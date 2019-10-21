class FSManager():
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

            (C)reate Configuration file
            (D)elete Configuration file
            (V)iew Network status
            (M)odify Configuration
            (R)eturn
            (Q)uit

            Enter choice:''').strip().lower()[0]]