
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

def generate_app(app) :
    app.debug=True
    return app




