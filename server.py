from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)




@app.route('/')
def index():
    """Just a generic index page to show."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()