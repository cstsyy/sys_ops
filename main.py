#!/usr/bin/env python
#
from usermanager import UserManager

ops_obj_map = {
    'u': 'UserManager',
    'g': 'GroupManager',
    'f': 'FSManager',
    'n': 'NetworkManager',
    's': 'ServiceManager',
    'q':'Quit'
}


def ops_obj_choice():
    return ops_obj_map[raw_input('''
    Choose a operation:

    (U)ser Management
    (G)roup Management
    (F)ilesystem Management
    (N)etwork Management
    (S)ervices Management
    (Q)uit

    Enter choice: ''').strip().lower()[0]]


def ops_exec(ops_obj):
    # Turn str obj to object
    ops_obj = eval(ops_obj)()
    ops = ops_obj.ops_choice()
    ops = 'ops_obj' + '.' + ops
    eval(ops)()


if __name__ == '__main__':
    ops_obj = ops_obj_choice()
    ops_exec(ops_obj)




# choice = ops_choice()
# print choice
#
# # if choice == "UserManager":
# #     choice = UserManager()
# ops_obj = eval(choice)()
#
#
# ops = ops_obj.ops_choice()
# print ops
# ops = "ops_obj." + ops
# print ops
# eval(ops)()
