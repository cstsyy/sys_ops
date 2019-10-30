import subprocess
import sys


class Manager(object):
    def __init__(self, **kwargs):
        self.ops_map = {
            'c': self.create,
            'd': self.delete,
            'm': self.modify,
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

    def must_input(self, prompt):
        """
        Check user's input to make sure it's not None
        :type prompt: str
        :return:input
        """
        input_str = None
        while not None:
            input_str = raw_input(prompt)
        return input_str

    def cmd_exe(self, cmd, obj, obj_name, action):
        """
        cmd = The command you want to executed
        obj, obj_name, action are used for the command execute result print
        obj = The object you operated,like user,service...
        obj_name = The specific name of object,like root(user),network(service)...
        action = The operation executed in the command,like start, stop...
        """
        # def result_info_print():
        #     return ('MSG:{obj} {obj_name} {action} succeed.'.format(obj=obj, obj_name=obj_name, action=action),
        #             'Error:{obj} {obj_name} {action} failed.'.format(obj=obj, obj_name=obj_name, action=action))
        result_info = ('MSG:{obj} {obj_name} {action} succeed.'.format(obj=obj, obj_name=obj_name, action=action),
                       'Error:{obj} {obj_name} {action} failed.'.format(obj=obj, obj_name=obj_name, action=action))
        exe_code = subprocess.call([cmd], shell=True)
        print exe_code
        if not exe_code:
            print result_info[0]
        else:
            print result_info[1]
        return exe_code

    # def create(self):
    #     pass
    #
    # def delete(self):
    #     pass
    #
    # def modify(self):
    #     pass
    #
    # def view(self):
    #     pass

    def quit_menu(self):
        print "quiting"
        sys.exit()

    def cmd_history(self):
        pass

    def log_record(self):
        pass
