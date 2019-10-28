from manager import Manager


class GroupManager(Manager):
    def __init__(self):
        group_ops_map = {
            'c': self.create,
            'd': self.delete,
            'm': self.modify
        }
        super(GroupManager, self).__init__(**group_ops_map)
        self.menu = '''
                Choose a operation:
    
                (C)reate Group
                (D)elete Group
                (V)iew Group
                (M)odify Group
                (R)eturn
                (Q)uit
    
                Enter choice: '''

    def create(self):
        pass

    def delete(self):
        pass

    def view(self):
        pass

    def modify(self):
        pass