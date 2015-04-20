from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "post: os og ip interfaces"

if __name__ == "__main__":
    app.run()
