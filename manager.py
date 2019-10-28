import subprocess
import sys


class Manager(object):
    def __init__(self, **kwargs):
        self.ops_map = {
            'v': self.view,
            'r': 'up_return',
            'q': self.quit_menu
        }
        self.ops_map.update(kwargs)

    def exe_ops(self, menu, ops_map):
        while True:
            print menu
            choice = raw_input('Enter choice:')
            try:
                ops = ops_map.get(choice)
                if str(ops) == 'up_return':
                    break
                ops()
            except Exception as e:
                print e
                print 'Bad choice, try again.'

    # def print_menu(self, menu):
    #     print menu

    # def exe_ops(self):
    #     print_menu_flag = False
    #     while True:
    #         if print_menu_flag:
    #             self.print_menu(self.menu)
    #         choice = raw_input('Enter choice:')
    #         try:
    #             ops = self.ops_map.get(choice)
    #             if str(ops) == 'up_return':
    #                 break
    #             ops()
    #             print_menu_flag = True
    #         except Exception as e:
    #             print_menu_flag = True
    #             print e
    #             print 'Bad choice, try again.'

    def cmd_exe(self, cmd, msg='Success', err='Fail'):
        exe_code =  subprocess.call([cmd], shell=True)
        print exe_code
        if not exe_code:
            print msg
        else:
            print err
        return exe_code

    def view(self):
        pass

    def quit_menu(self):
        print "quiting"
        sys.exit()

    def cmd_history(self):
        pass

    def log_record(self):
        pass