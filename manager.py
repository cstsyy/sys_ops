import subprocess
import sys

class Manager():
    def exe_ops(self):
        while True:
            print self.menu
            choice = raw_input('Enter choice:')
            try:
                ops = self.ops_map.get(choice)
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

    def cmd_exe(self, cmd):
        return subprocess.call([cmd], shell=True)

    def quit_menu(self):
        print "quiting"
        sys.exit()

    def cmd_history(self):
        pass

    def log_record(self):
        pass