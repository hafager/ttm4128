from subprocess import call
from subprocess import check_output
from time import sleep

#Method that returns 129.241.209.10s computers OS-info. 
def snmp_os():
    #Enters the command "snmpwalk -v 2c -c ttm4128 129.241.209.10 sysDescr" in terminal and returns the output.
    os = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "sysDescr"]).splitlines()
    for i in range(len(os)):
        os[i] = " ".join(os[i].split()[3:])
    return os

def snmp_interface():
    #Enters the command "snmpwalk -v 2c -c ttm4128 129.241.209.10 ifDescr" in terminal and stores it in name-variable
    name = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ifDescr"]).splitlines()
    
    #Enters the command "snmpwalk -v 2c -c ttm4128 129.241.209.10 ipAdEntAddr" in terminal and stores it in ip-variable
    ip = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ipAdEntAddr"]).splitlines()
    
    #Enters the command "snmpwalk -v 2c -c ttm4128 129.241.209.10 ipAdEntNetMask" in terminal and stores it in mask-variable
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



