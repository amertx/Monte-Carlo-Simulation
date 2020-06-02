#flask sever python file
from flask import Flask

# create an app instance
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! this is very cool a continuous change"
if __name__ == "__main__":
    app.run(debug=True)
