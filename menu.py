#!/usr/bin/env ptyon
#
# import sys
from manager import Manager
from usermanager import UserManager
from groupmanager import GroupManager
from fsmanager import FSManager
from networkmanager import NetworkManager
from servicemanager import ServiceManager


class SysManager(Manager):
    def __init__(self):
        self.ops_obj_map = {
            '1':UserManager,
            '2':GroupManager,
            '3':FSManager,
            '4':NetworkManager,
            '5':ServiceManager,
            '6':self.quit_menu
        }
        self.menu = '''Choose a operation:

            1.User Management
            2.Group Management
            3.Filesystem Management
            4.Network Management
            5.Services Management
            6.Quit '''

    # def print_menu(self):
    #     print '''Choose a operation:
    #
    #         1.User Management
    #         2.Group Management
    #         3.Filesystem Management
    #         4.Network Management
    #         5.Services Management
    #         6.Quit '''

    def get_obj(self):
        while True:
            print self.menu
            choice = str(raw_input('Enter choice:'))
            ops_obj = self.ops_obj_map.get(choice)()
            return ops_obj
            # try:
            #     ops_obj = self.ops_obj_map.get(choice)()
            #     return ops_obj
            # except Exception as e:
            #     print e
            #     print 'Bad choice, try again.'

    # def quit_menu(self):
    #     sys.exit()


if __name__ == '__main__':
    mgr_obj = SysManager()
    while True:
        ops_obj = mgr_obj.get_obj()
        ops_obj.exe_ops(ops_obj.menu, ops_obj.ops_map)
