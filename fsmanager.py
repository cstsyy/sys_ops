from manager import Manager


class FSManager(Manager):
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

            (C)reate FS
            (D)elete FS
            (V)iew FS
            (M)odify FS
            (R)eturn
            (Q)uit

            Enter choice:'''