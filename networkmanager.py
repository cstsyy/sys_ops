from manager import Manager


class NetworkManager(Manager):
    def __init__(self):
        # net_ops_map = {
        #     'c': self.create,
        #     'd': self.delete,
        #     'm': self.modify,
        # }
        # super(NetworkManager, self).__init__(**net_ops_map)
        super(NetworkManager, self).__init__()
        self.menu = '''
            Choose a operation:

            (C)reate Configuration file
            (D)elete Configuration file
            (V)iew Network status
            (M)odify Configuration
            (R)eturn
            (Q)uit

            Enter choice:'''

    def create(self):
        print "Unsupported now."
        pass

    def delete(self):
        print "Unsupported now."
        pass

    def modify(self):
        print "Unsupported now."
        pass

    def view(self):
        print "Unsupported now."
        pass
