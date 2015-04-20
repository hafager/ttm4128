from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "post: os og ip interfaces dette blir kult"

if __name__ == "__main__":
    app.run("78.91.20.230")

@app.route('/')
def index():
    """Just a generic index page to show."""
    return render_template('index.html')
