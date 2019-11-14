from manager import Manager


class UserManager(Manager):
    def __init__(self):
        # user_ops_map = {
        #     'c': self.create,
        #     'd': self.delete,
        #     'm': self.modify
        # }
        # super(UserManager, self).__init__(**user_ops_map)
        super(UserManager, self).__init__()
        # self.ops_map = {
        #     'c': self.create,
        #     'd': self.delete,
        #     'v': self.view,
        #     'm': self.modify,
        #     'r': 'up_return',
        #     'q': self.quit_menu
        # }
        self.menu = '''Choose a operation:

            (C)reate User
            (D)elete User
            (V)iew User
            (M)odify User
            (R)eturn
            (Q)uit'''

    # def print_menu(self):
    #     print '''Choose a operation:
    #
    #         (C)reate User
    #         (D)elete User
    #         (V)iew User
    #         (M)odify User
    #         (R)eturn
    #         (Q)uit'''

    # def exe_ops(self):
    #     print_menu_flag = False
    #     while True:
    #         if print_menu_flag:
    #             self.print_menu()
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

    # def ops_choice(self):
    #     return self.ops_map[raw_input('''
    #         Choose a operation:https://hao.rising.cn/?actionid=4150002&b=57

    #
    #         (C)reate User
    #         (D)elete User
    #         (V)iew User
    #         (M)odify User
    #         (R)eturn
    #         (Q)uit
    #
    #         Enter choice: ''').strip().lower()[0]]

    def create(self):
        username = self.must_input('Username:')
        uid = raw_input('Uid[Press Enter for default]:')
        group = raw_input('Group[Press Enter for default]:')
        groups = raw_input('Supplementary groups[group1,group2...][Press Enter for default]:')
        homedir = raw_input('HomeDir[Press Enter for default]:')
        createflag = raw_input('Create homedir?[Y/N][Press Enter for default]')
        cmd = 'useradd {optu} {uid} {optg} {group} {optG} {groups} {optd} {homedir} {createflag} {username}'.format(
            optu='-u' if uid else '', uid=uid,
            optg='-g' if group else '', group=group,
            optG='-G' if groups else '', groups=groups,
            optd='-d' if homedir else '', homedir=homedir,
            createflag='-m' if createflag.lower() == 'y' else '',
            username=username
        )
        cmd = ' '.join(cmd.split())
        # print cmd
        return self.cmd_exe(cmd, 'User', username, 'create')
        # print exe_code
        # if not exe_code:
        #     print 'MSG:User %s create success.' % username
        # else:
        #     print 'Error:User %s create fail.' % username

    def delete(self):
        username = self.must_input('Username:')
        removeflag = raw_input('Delete homedir and mail spool?[Y/N]')
        cmd = 'userdel {optr} {username}'.format(
            optr='-r' if removeflag.lower() == 'y' else '', username=username
        )
        cmd = ' '.join(cmd.split())
        return self.cmd_exe(cmd, 'User', username, 'delete')
        # exe_code = self.cmd_exe(cmd)
        # print exe_code
        # if not exe_code:
        #     print 'MSG:User %s delete success.' % username
        # else:
        #     print 'MSG:User %s delete success.' % username

    def view(self):
        username = self.must_input('Username:')
        cmd = 'id {username}'.format(username=username)
        return self.cmd_exe(cmd, 'User', username, 'view')
        # exe_code = self.cmd_exe(cmd)
        # print exe_code
        # if exe_code:
        #     print 'Error:User {} does not exests.'.formatusername

    def modify(self):
        username = self.must_input('Username:')
        uid = raw_input('Uid[input the uid you want to change or press Enter to skip uid modify]:')
        group = raw_input('Gid[input the gid/group you want to change or press Enter to skip gid modify]:')
        groups = raw_input('Supplementary groups[group1,group2...]'
                           '[input the groups you want to change or press Enter to skip gtoups modify]:')
        if groups:
            appendflag = raw_input('Append groups?[Y/N]')
        homedir = raw_input('HomeDir[input the homedir you want to change or press Enter to skip homedir modify]:')
        cmd = 'usermod {optu} {uid} {optg} {gid} {appendflag} {optG} {groups} {optd} {homedir} {username}'.format(
            optu='-u' if uid else '', uid=uid,
            optg='-g' if group else '', gid=group,
            appendflag='-a' if groups and str(appendflag.lower()) == 'y' else '',
            optG='-G' if groups else '', groups=groups,
            optd='-d' if homedir else '', homedir=homedir,
            username=username
        )
        cmd = ' '.join(cmd.split())
        return self.cmd_exe(cmd, 'User', username, 'modify')
        # print cmd
        # exe_code = self.cmd_exe(cmd)
        # print exe_code
        # if not exe_code:
        #     print 'MSG:User %s modify success.' % username
        # else:
        #     print 'Error:User %s modify fail.' % username

    # def up_return(self):
    #     pass

    # def quit_menu(self):
    #     print "quiting"
    #     sys.exit()

