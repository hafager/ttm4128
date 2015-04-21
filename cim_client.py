import pywbem


#Is the end point where we want to get the information from
CIMEndpoint = "http://ttm4128.item.ntnu.no:5988"

#Sets up the connection
conn = pywbem.WBEMConnection(CIMEndpoint)


#Here we get the information about the operating system
def os():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_OperatinSystem class
	names = conn.EnumerateInstanceNames('CIM_OperatingSystem')

	osVersion =[]
	#Returns only the information we want
	for n in names:
		os = conn.GetInstance(n)

		for key, value in os.items():
			if (key == 'Version'):
				osVersion.append(value)
	return osVersion

# #This function gets the information about the names, ip adresses and maskes from the CIM 
def interface():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_IPProtocolEndpoint class
	namess = conn.EnumerateInstanceNames('CIM_IPProtocolEndpoint')

	interface =[]
	name = []
	ip =[]
	mask = []

	for n in namess:
		os = conn.GetInstance(n)

		for key, value in os.items():
			if (key == "ElementName"):
				name.append(value)
			if (key == "IPv4Address"):
				ip.append(value)
			if (key == "SubnetMask"):
				mask.append(value)

	interface.append(name)
	interface.append(ip)
	interface.append(mask)

	return interface

print os()
print interface()


