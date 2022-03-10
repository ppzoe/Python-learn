"""
获取网管信息方法一
"""
import os
import sys

try:
    import netifaces
except ImportError:
    try:
        command_to_execute = "pip install netifaces || easy_install netifaces"
        os.system(command_to_execute)
    except OSError:
        print("Can NOT install netifaces, Aborted!")
        sys.exit(1)
    import netifaces

routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]
# routingNicMacAddr = netifaces.gateways()['default'][netifaces.AF_INET][2]
# routingIPAddr = netifaces.gateways()['default'][netifaces.AF_INET][3]
# routingIPNetmask = netifaces.gateways()['default'][netifaces.AF_INET][4]

for interface in netifaces.interfaces():
    if interface == routingNicName:
        # print netifaces.ifaddresses(interface)
        routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
        try:
            routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
            # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
            routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
        except KeyError:
            pass

display_format = '%-30s %-20s'
print(display_format % ("Routing Gateway:", routingGateway))
print(display_format % ("Routing NIC Name:", routingNicName))
print(display_format % ("Routing NIC MAC Address:", routingNicMacAddr))
print(display_format % ("Routing IP Address:", routingIPAddr))
print(display_format % ("Routing IP Netmask:", routingIPNetmask))

'''
获取网关信息方法二


import psutil
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item[1]))
    return netcard_info
if __name__ == '__main__':
    
    print (get_netcard())

'''
