from flask import Flask
from cim_client import ipInterface, os
import socket

app = Flask(__name__)
myIpAdress = socket.gethostbyname(socket.gethostname())

#Calls the os function
operatingSystemInfo = os()

#Calls the function to get the name, ip and mask
name,ip,mask = ipInterface()

#Tells Flask what URL should trigger our function.
@app.route('/')
def hello():
	#Print the info (HER LEGGES DET TIL HTML)
	return ("OS: " + operatingSystemInfo + '/n' + "Name: " + name + '/n' + "Ip: " + ip + '/n' + "Mask: " + mask)

#Makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module. 
if __name__ == '__main__':
	#Tells the server the ip-address you can reach the server. (Formulere bedre?? :P )
    app.run(myIpAdress)
