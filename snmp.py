from subprocess import call
from subprocess import check_output
from time import sleep


def snmp_os():

    os = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "sysDescr"]).splitlines()
    for i in range(len(os)):
        os[i] = " ".join(os[i].split()[3:])
    return os

def snmp_interface():
    
    name = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ifDescr"]).splitlines()

    ip = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ipAdEntAddr"]).splitlines()
    
    mask = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ipAdEntNetMask"]).splitlines()
    
    interface = []

    for n in range(len(name)):
    	interface.append([name[n].split()[-1]])

    for i in range(len(ip)):
    	address = ip[i].split()
    	interface[i].append(address[-1])

    for m in range(len(mask)):
    	interface[m].append(mask[m].split()[-1])

    return interface



