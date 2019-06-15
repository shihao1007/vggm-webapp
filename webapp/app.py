# import flask
from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session
from bokeh.embed import server_document

# instantiate the app
app = Flask(__name__)

# render the template
@app.route('/', methods=['GET'])
def index():
    
    with pull_session(url="http://localhost:5006/map") as session:

        # generate a script to load the customized session
        script = server_session(session_id=session.id, url='http://localhost:5006/map')

        # use the script in the rendered page
        return render_template("index.html", vggm=vggm, template="Flask")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
