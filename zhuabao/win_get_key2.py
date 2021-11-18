import winreg
'''网卡id翻译'''
nic_key='SYSTEM\ControlSet001\Control\Class\{07D20C5F-D2BF-47E6-B112-AAAEF4AFB290}'
key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,nic_key)
index=0
nic_information=dict()
while True:
    try:
        sub_key = winreg.EnumKey(key,index)
        sub_key = winreg.OpenKey(key,sub_key)
        nic_name,_ = winreg.QueryValueEx(sub_key,'DriverDesc')
        nic_id,_ = winreg.QueryValueEx(sub_key,'DriverDesc')
        nic_information[nic_id] = nic_name
        index = index+1
    except:
        break
for key , value in nic_information.items():
    print(key,value,sep=':')

print(nic_name,nic_id)