import pywbem

CIMEndpoint = "http://ttm4128.item.ntnu.no:5988"

conn = pywbem.WBEMConnection(CIMEndpoint)


def os():

	osConn = conn.EnumerateInstances('CIM_OperatingSystem')[0]
	return (osConn["version"])

operatingSystemInfo = os()

def ipInterface():
	osConn = conn.EnumerateInstances('CIM_IPProtocolEndpoint')[0]
	name = osConn["ElementName"]
	ip = osConn["IPv4Address"]
	mask = osConn["SubnetMask"]
	print (osConn.items())
	return name,ip,mask

name,ip,mask = ipInterface()



