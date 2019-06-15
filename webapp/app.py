# import flask
from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session
from bokeh.embed import server_document
from bokeh.server.server import Server
from tornado.ioloop import IOLoop

# instantiate the app
app = Flask(__name__)

# render the template
# @app.route('/')
# def index():
    
#     vggm = server_document(url="http://127.0.0.1:5006/map")

#     return render_template("index.html", vggm=vggm)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")

@app.route('/', methods=['GET'])
def bkapp_page():
    vggm = server_document('http://localhost:5006/map')
    return render_template("index.html", vggm=vggm, template="Flask")


def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server(io_loop=IOLoop(), allow_websocket_origin=["localhost:5000"])
    server.start()
    server.io_loop.start()

from threading import Thread
Thread(target=bk_worker).start()

if __name__ == '__main__':
    print('Opening single process Flask app with embedded Bokeh application on http://localhost:5000/')
    print()
    print('Multiple connections may block the Bokeh app in this configuration!')
    print('See "flask_gunicorn_embed.py" for one way to run multi-process')
    app.run(host="0.0.0.0")