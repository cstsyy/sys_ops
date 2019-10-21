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

            (C)reate FS
            (D)elete FS
            (V)iew FS
            (M)odify FS
            (R)eturn
            (Q)uit

            Enter choice:''').strip().lower()[0]]