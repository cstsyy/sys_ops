from manager import Manager


class NetworkManager(Manager):
    def __init__(self):
        self.ops_map = {
            'c': 'create',
            'd': 'delete',
            'v': 'view',
            'm': 'modify',
            'r': 'up_return',
            'q': self.quit_menu
        }
        self.menu = '''
            Choose a operation:

            (C)reate Configuration file
            (D)elete Configuration file
            (V)iew Network status
            (M)odify Configuration
            (R)eturn
            (Q)uit

            Enter choice:'''