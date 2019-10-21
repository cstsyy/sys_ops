class GroupManager():
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

            (C)reate Group
            (D)elete Group
            (V)iew Group
            (M)odify Group
            (R)eturn
            (Q)uit

            Enter choice: ''').strip().lower()[0]]
