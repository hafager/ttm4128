import pywbem


#Is the end point where we want to get the information from
CIMEndpoint = "http://ttm4128.item.ntnu.no:5988"

#Sets up the connection
conn = pywbem.WBEMConnection(CIMEndpoint)


#Here we get the information about the operating system
def os():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_OperatinSystem class
	osConn = conn.EnumerateInstances('CIM_OperatingSystem')[0]
	#Returns only the information we want
	return (osConn["version"])


#This function gets the information about the names, ip adresses and maskes from the CIM 
def ipInterface():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_IPProtocolEndpoint class
	ipConn = conn.EnumerateInstances('CIM_IPProtocolEndpoint')[0]
	#Gets the names from the string
	name = ipConn["ElementName"]
	#Gets the ip adresses from the string
	ip = ipConn["IPv4Address"]
	#Gets the maskes from the string
	mask = ipConn["SubnetMask"]
	return name,ip,mask

