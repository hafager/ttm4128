from subprocess import call
from subprocess import check_output
from time import sleep


def snmp_os():

    return check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "sysDescr"])

def snmp_ip_interface():
    name = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ifDescr"])
  
  
    ip = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ipAdEntAddr"])
    
    mask = check_output(["snmpwalk", "-v", "2c", "-c", "ttm4128", "129.241.209.10", "ipAdEntNetMask"])
    return name, ip, mask

name, ip, mask = snmp_ip_interface()
print( name)
print( ip)
print( mask)
print( snmp_os())


