#!/usr/bin/env ptyon
#
import sys
from usermanager import UserManager
from groupmanager import GroupManager
from fsmanager import FSManager
from networkmanager import NetworkManager
from servicemanager import ServiceManager


class SysManager():
    def __init__(self):
        self.method_map = {
            '1':UserManager,
            '2':GroupManager,
            '3':FSManager,
            '4':NetworkManager,
            '5':ServiceManager,
            '6':self.quit_menu
        }

    def print_menu(self):
        print '''Choose a operation:

            1.User Management
            2.Group Management
            3.Filesystem Management
            4.Network Management
            5.Services Management
            6.Quit '''

    def get_obj(self):
        while True:
            choice = str(raw_input('Enter choice:'))
            try:
                obj = self.method_map.get(choice)()
                obj.print_menu()
            except Exception:
                print 'Bad choice, try again.'

    def quit_menu(self):
        sys.exit()

if __name__ == '__main__':
    sys_obj = SysManager()
    sys_obj.print_menu()
    sys_obj.get_obj()