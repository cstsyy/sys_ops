from manager import Manager


class FSManager(Manager):
    def __init__(self):
        fs_ops_map = {
            'e': self.extend
        }
        super(FSManager, self).__init__(**fs_ops_map)
        self.menu = '''
            Choose a operation:

            (C)reate PV/VG/LV/FS
            (D)elete PV/VG/LV/FS
            (E)xtend VG/LV/FS
            (V)iew PV/VG/LV/FS
            (M)odify VG/LV/FS
            (R)eturn
            (Q)uit

            Enter choice:'''

    def create(self):
        while True:
            fs_obj = self.must_input('What object do you want to operate[PV/VG/LV/FS]:')
            if str(fs_obj) == 'PV':
                device = self.must_input('Device:')
                cmd = 'pvcreate {device}'.format(device=device)
                return self.cmd_exe(cmd, fs_obj, device, 'create')
            elif str(fs_obj) == 'VG':
                vgname = self.must_input('VG name:')
                pvs = self.must_input('PV[PV1,PV2,PV3...]:')
                cmd = 'vgcreate {vgname} {pvs}'.format(vgname=vgname, pvs=pvs)
                return self.cmd_exe(cmd, fs_obj, vgname, 'create')
            elif str(fs_obj) == 'LV':
                lvname = self.must_input('LV name:')
                size = self.must_input('Size:')
                vgname = self.must_input("VG:")
                cmd = 'lvcreate -n {lvname} -L {size} {vgname}'.format(
                    lvname=lvname,
                    size=size,
                    vgname=vgname
                )
                return self.cmd_exe(cmd, fs_obj, lvname, 'create')
            elif str(fs_obj) == 'FS':
                lvname = self.must_input('LV name')
                vgname = self.must_input('VG:')
                fstype = self.must_input('FS type[ext2/3/4]:')
                cmd = 'mkfs.{fstype} /dev/{vgname}/{lvname}'.format(fstype=fstype, vgname=vgname, lvname=lvname)
                return self.cmd_exe(cmd, fs_obj, lvname, 'create')
            else:
                print "Bad choice,try again."

    def delete(self):
        while True:
            fs_obj = self.must_input('What object do you want to operate[PV/VG/LV/FS]:')
            if str(fs_obj) == 'PV':
                device = self.must_input('Device:')
                cmd = 'pvremove {device}'.format(device=device)
                return self.cmd_exe(cmd, fs_obj, device, 'delete')
            elif str(fs_obj) == 'VG':
                vgname = self.must_input('VG name:')
                cmd = 'vgremove {vgname}'.format(vgname=vgname)
                return self.cmd_exe(cmd, fs_obj, vgname, 'delete')
            elif str(fs_obj) == 'LV':
                lvname = self.must_input('LV name:')
                vgname = self.must_input("VG:")
                cmd = 'lvremove {vgname}/{lvname}'.format(lvname=lvname, vgname=vgname)
                return self.cmd_exe(cmd, fs_obj, lvname, 'delete')
            else:
                print "Bad choice,try again."

    def extend(self):
        print "Unsupported now."
        pass

    def view(self):
        while True:
            fs_obj = self.must_input('What object do you want to operate[PV/VG/LV/FS]:')
            if str(fs_obj) == 'PV':
                device = self.must_input('Device:')
                cmd = 'pvs {device}'.format(device=device)
                return self.cmd_exe(cmd, fs_obj, device, 'view')
            elif str(fs_obj) == 'VG':
                vgname = self.must_input('VG name:')
                cmd = 'vgs {vgname}'.format(vgname=vgname)
                return self.cmd_exe(cmd, fs_obj, vgname, 'view')
            elif str(fs_obj) == 'LV':
                lvname = self.must_input('LV name:')
                vgname = self.must_input("VG:")
                cmd = 'lvs {vgname}/{lvname}'.format(lvname=lvname, vgname=vgname)
                return self.cmd_exe(cmd, fs_obj, lvname, 'view')
            else:
                print "Bad choice,try again."

    def modify(self):
        print "Unsupported now."
        pass
