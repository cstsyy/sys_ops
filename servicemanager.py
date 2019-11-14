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

    # def result_info_print(self, svc, action):
    #     return ('MSG:Service {svc} {action} succeed.'.format(svc=svc, action=action),
    #             'Error:Service {svc} {action} failed.'.format(svc=svc, action=action))

    def start(self):
        svc = self.must_input('Service name:')
        cmd = 'systemctl start {svc}'.format(svc=svc)
        return self.cmd_exe(cmd, 'Service', svc, 'start')

    def stop(self):
        svc = self.must_input('Service name:')
        cmd = 'systemctl stop {svc}'.format(svc=svc)
        return self.cmd_exe(cmd, 'Service', svc, 'stop')

    def view(self):
        svc = self.must_input('Service name:')
        cmd = 'systemctl status {svc}'.format(svc=svc)
        return self.cmd_exe(cmd, 'Service', svc, 'view')

    def enable(self):
        svc = self.must_input('Service name:')
        cmd = 'systemctl enable {svc}'.format(svc=svc)
        return self.cmd_exe(cmd, 'Service', svc, 'enable')

    def disable(self):
        svc = self.must_input('Service name:')
        cmd = 'systemctl disable {svc}'.format(svc=svc)
        return self.cmd_exe(cmd, 'Service', svc, 'disable')

    # def create(self):
    #     """Just for init"""
    #     pass
    #
    # def delete(self):
    #     """Just for init"""
    #     pass
    #
    # def modify(self):
    #     """Just for init"""
    #     pass
