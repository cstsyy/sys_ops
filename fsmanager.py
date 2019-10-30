from manager import Manager


class FSManager(Manager):
    def __init__(self):
        fs_ops_map = {
            'e':self.extend
        }
        super(FSManager, self).__init__()
        self.menu = '''
            Choose a operation:

            (C)reate PV/VG/LV/FS
            (D)elete PV/VG/LV/FS
            (V)iew PV/VG/LV/FS
            (M)odify PV/VG/LV/FS
            (R)eturn
            (Q)uit

            Enter choice:'''

    def create(self):
        fs_obj = self.must_input('What do you want to operate[PV/VG/LV/FS]:')
        if str(fs_obj) == 'PV':
            device = raw_input('Device:')
            cmd = 'pvcreate {device}'.format(device=device)
            return self.cmd_exe(cmd, fs_obj, device, 'create')
        elif str(fs_obj) == 'VG':
            vgname = raw_input('VG name:')
            pvs = raw_input('PV[PV1,PV2,PV3...]:')
            cmd = 'vgcreate {vgname} {pvs}'.format(vgname=vgname, pvs=pvs)
            return self.cmd_exe(cmd, fs_obj, vgname, 'create')
        elif str(fs_obj) == 'LV':
            lvname = raw_input('LV name:')
            size = raw_input('Size:')
            cmd = 'lvcreate -n'


    def extend(self):
        pass