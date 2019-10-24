import subprocess


class UserManager():
    def __init__(self):
        global ops_map
        ops_map = {
            'c': 'create',
            'd': 'delete',
            'v': 'view',
            'm': 'modify',
            'r': 'return',
            'q': 'quit'
        }

    def ops_choice(self):
        return ops_map[raw_input('''
            Choose a operation:

            (C)reate User
            (D)elete User
            (V)iew User
            (M)odify User
            (R)eturn
            (Q)uit

            Enter choice: ''').strip().lower()[0]]

    def create(self):
        username = raw_input('Username:')
        uid = raw_input('Uid:')
        group = raw_input('Group:')
        groups = raw_input('Supplementary groups[group1,group2...]:')
        homedir = raw_input('HomeDir:')
        createflag = raw_input('Create homedir?[Y/N]')
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
        exe_code = subprocess.call([cmd], shell=True)
        print exe_code
        if not exe_code:
            print 'MSG:User %s create success.' %(username)
        else:
            print 'Error:User %s create fail.' %(username)

    def delete(self):
        username = raw_input('Username:')
        removeflag = raw_input('Delete homedir and mail spool?[Y/N]')
        cmd = 'userdel {optr} {username}'.format(
            optr='-r' if removeflag.lower() == 'y' else '', username=username
        )
        cmd = ' '.join(cmd.split())
        exe_code = subprocess.call([cmd], shell=True)
        print exe_code
        if not exe_code:
            print 'MSG:User %s delete success.' %(username)
        else:
            print 'Error:User %s delete fail.' %(username)

    def view(self):
        username = raw_input('Username:')
        cmd = 'id {username}'.format(username=username)
        exe_code = subprocess.call([cmd], shell=True)
        print exe_code
        if exe_code:
            print 'Error:User {} does not exests.'.format(username)


    def modify(self):
        username = raw_input('Username:')
        uid = raw_input('Uid[input the uid you want to change or press Enter to skip uid modify]:')
        group = raw_input('Gid[input the gid/group you want to change or press Enter to skip gid modify]:')
        groups = raw_input('Supplementary groups[group1,group2...]'
                           '[input the groups you want to change or press Enter to skip gtoups modify]:')
        appendflag = raw_input('Append groups?[Y/N]')
        homedir = raw_input('HomeDir[input the homedir you want to change or press Enter to skip homedir modify]:')

    def back(self):
        print "backing"
        pass

    def quit(self):
        print "quiting"
        pass

    def print_menu(self):
        print "menu menu menu"
        pass