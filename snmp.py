from subprocess import call
from subprocess import check_output
from time import sleep

#Method that returns 129.241.209.10s computers OS-info. 
def snmp_os():
    #Enters the command "snmpwalk -v 2c -c ttm4128 129.241.209.10 sysDescr" in terminal and returns the output.
    os = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "sysDescr"]).splitlines()
    
    #removes the unecessary overhead to the os information for all oses on the given ip-address
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
    
    #creating an array of arrays with three fields: [name, ip, mask]
    interface = []

    for n in range(len(name)):
    	#stripping the unecessary information and adding the name field to the array
        interface.append([name[n].split()[-1]])

    for i in range(len(ip)):
    	#stripping the unecessary information and adding the ip field to the array 
    	interface[i].append(ip[i].split()[-1])

    for m in range(len(mask)):
    	#stripping the unecessary information and adding the mask field to the array
        interface[m].append(mask[m].split()[-1])

    return interface



