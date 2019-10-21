class ServiceManager():
    def __init__(self):
        global ops_map
        ops_map = {
            's': 'start',
            'p': 'stop',
            'v': 'view',
            'e': 'enable',
            'd': 'disable',
            'r': 'return',
            'q': 'quit'
        }

    def ops_choice(self):
        return ops_map[raw_input('''
            Choose a operation:

            (S)tart Service
            Sto(P) Service
            (V)iew Service Status
            (E)nable Service
            (D)isable Service
            (R)eturn
            (Q)uit

            Enter choice:''').strip().lower()[0]]