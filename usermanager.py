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
        print "deleteing"
        pass

    def view(self):
        print "viewing"
        pass

    def modify(self):
        print "modifing"
        pass

    def back(self):
        print "backing"
        pass

    def quit(self):
        print "quiting"
        pass
