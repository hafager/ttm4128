from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from cim_client import ipInterface, os


app = Flask(__name__)
Bootstrap(app)





@app.route('/')
def index():
    """Just a generic index page to show."""
    return render_template('index.html')

#Calls the os function
operatingSystemInfo = os()

#Calls the function to get the name, ip and mask
name,ip,mask = ipInterface()

#Tells Flask what URL should trigger our function.
@app.route('/hello')
def hello():
	#Print the info (HER LEGGES DET TIL HTML)
	return ("OS: " + operatingSystemInfo + '/n' + "Name: " + name + '/n' + "Ip: " + ip + '/n' + "Mask: " + mask)

#Makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module. 
if __name__ == '__main__':
	#Tells the server the ip-address you can reach the server. (Formulere bedre?? :P )
    app.run()

