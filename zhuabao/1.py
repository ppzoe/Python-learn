import netifaces as ni
import winreg as wr
from pprint import pprint

def get_driver_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Cleass\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(wr.QueryInfoKey(reg_key)[0]):
        subkey_name = wr.EnumKey(reg_key, i)
        try:
            reg_subkey = wr.OpenKey(reg_key, subkey_name)
            guid = wr.QueryValueEx(reg_subkey, 'NetCfgInstanceId')[0]
            try:
                idx = iface_guids.index(guid)
                iface_names[idx] = wr.QueryValueEx(reg_subkey, 'DriverDesc')[0]
            except ValueError:
                pass
        except PermissionError:
            pass
    return iface_names

x = ni.interfaces()
pprint(get_driver_name_from_guid(x))
