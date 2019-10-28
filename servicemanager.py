from manager import Manager


class ServiceManager(Manager):
    def __init__(self):
        svc_ops_map = {
            's': self.start,
            'p': self.stop,
            'e': self.enable,
            'd': self.disable,
        }
        super(ServiceManager, self).__init__(**svc_ops_map)
        self.menu = '''
            Choose a operation:

            (S)tart Service
            Sto(P) Service
            (V)iew Service Status
            (E)nable Service
            (D)isable Service
            (R)eturn
            (Q)uit

            Enter choice:'''

    def start(self):
        pass

    def stop(self):
        pass

    def view(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass