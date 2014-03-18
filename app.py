
from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Landing Page"

@app.route('/submit', methods=['POST'])
def submit():
    return "Thanks for signing up!"
