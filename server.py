
from flask import Flask, render_template
from cim_client import cim_interface, cim_os
from snmp import snmp_interface, snmp_os
import socket


myIpAdress = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)

#Calls the os function
cim_os = cim_os()
snmp_os = snmp_os()

#Calls the function to get the name, ip and mask
cim_interfaces = cim_interface()
snmp_interfaces = snmp_interface()

@app.route('/')
def index():
    """Just a generic index page to show."""
    return render_template('index.html', cim_interfaces=cim_interfaces, snmp_interfaces=snmp_interfaces, cim_os=cim_os, snmp_os=snmp_os)


#Makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module. 
if __name__ == '__main__':
	#Tells the server the ip-address you can reach the server. (Formulere bedre?? :P )

    app.run(myIpAdress)