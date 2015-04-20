from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def index():
    """Just a generic index page to show."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()