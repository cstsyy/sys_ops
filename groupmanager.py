from manager import Manager


class GroupManager(Manager):
    def __init__(self):
        # group_ops_map = {
        #     'c': self.create,
        #     'd': self.delete,
        #     'm': self.modify
        # }
        # super(GroupManager, self).__init__(**group_ops_map)
        super(GroupManager, self).__init__()
        self.menu = '''
                Choose a operation:
    
                (C)reate Group
                (D)elete Group
                (V)iew Group
                (M)odify Group
                (R)eturn
                (Q)uit
    
                Enter choice: '''

    def create(self):
        groupname = self.must_input('Group name:')
        gid = raw_input('Gid[Press Enter for default]:')
        cmd = 'groupadd {optg} {gid} {groupname}'.format(
            optg='-g' if gid else '', gid=gid, groupname=groupname
        )
        cmd = ' '.join(cmd.split())
        return self.cmd_exe(cmd, 'Group', groupname, 'create')

    def delete(self):
        groupname = self.must_input('Group name:')
        cmd = 'groupdel {groupname}'.format(groupname=groupname)
        return self.cmd_exe(cmd, 'Group', groupname, 'delete')

    def view(self):
        groupname = self.must_input('Group name:')
        cmd = 'cat /etc/group | grep ^{groupname}:'.format(groupname=groupname)
        return self.cmd_exe(cmd, 'Group', groupname, 'view')

    def modify(self):
        groupname = self.must_input('Group name[Press Enter for default]:')
        newname = raw_input('New Group name[Press Enter for default]:')
        gid = raw_input('Gid[Press Enter for default]:')
        cmd = 'groupmod {optn} {newname} {optg} {gid} {groupname}'.format(
            optn='-n' if newname else '', newname=newname,
            optg='-g' if gid else '', gid=gid, groupname=groupname
        )
        cmd = ' '.join(cmd.split())
        return self.cmd_exe(cmd, 'Group', groupname, 'modify')
