import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    #return "hey"
     return flask.render_template("index.html")
app.run(
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 8080))
)
    