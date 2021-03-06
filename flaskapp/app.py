# import flask
from flask import Flask, render_template
from bokeh.embed import server_document
import sys, os

# instantiate the app
app = Flask(__name__)

# render the template
@app.route('/')
def index():

    vggm = server_document(url="http://localhost:5006/map")

    return render_template("index.html", vggm=vggm)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
