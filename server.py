#flask sever python file
from flask import Flask
#import marketDataRetrieval as mdr
import request
from flask import render_template


# create an app instance
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
