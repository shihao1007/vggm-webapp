# import flask
from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session
from bokeh.embed import server_document

# instantiate the app
app = Flask(__name__)

# render the template
@app.route('/')
def index():
    
    print("BEFORE bokeh server_document")
    vggm = server_document(url="http://0.0.0.0:5006/map")
    print()
    print("AFTER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(vggm)
    print()
    print()
    print("******************************************")

    return render_template("index.html", vggm=vggm)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
