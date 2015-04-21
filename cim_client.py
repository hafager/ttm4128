import pywbem


#Is the end point where we want to get the information from
CIMEndpoint = "http://ttm4128.item.ntnu.no:5988"

#Sets up the connection
conn = pywbem.WBEMConnection(CIMEndpoint)


# This method return a list of operation systems stripped down to the only information we want to display
def cim_os():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_OperatinSystem class
	names = conn.EnumerateInstanceNames('CIM_OperatingSystem')

	osVersion =[]
	#Returns only the information we want
	for n in names:
		os = conn.GetInstance(n)

		for key, value in os.items():
			if (key == 'Version'):
				# Formats the string correctly
				pretty_name = value[value.find("PRETTY_NAME"):]
				pretty_name = pretty_name[pretty_name.find('"')+1:]
				pretty_name = pretty_name[:pretty_name.find('"')]
				osVersion.append(pretty_name)
	return osVersion

# #This function gets the information about the names, ip adresses and masks from the CIM 
# It returns a list with all interfaces
def cim_interface():
	#EnumerateInstances returns a list of CIMNamedInstance objects which contain the instance name and instance of for each and every instance of the CIM_IPProtocolEndpoint class
	namess = conn.EnumerateInstanceNames('CIM_IPProtocolEndpoint')

	interface =[]

	for n in namess:
		os = conn.GetInstance(n)
		interfacex = ["","",""]
		for key, value in os.items():
			if (key == "ElementName"):
				interfacex[0]=value
			if (key == "IPv4Address"):
				interfacex[1]=value
			if (key == "SubnetMask"):
				interfacex[2]=value
		interface.append(interfacex)

	return interface