from flask import render_template
from pywebqueue import app, db

@app.route("/")
def hello():
    return render_template('hello.html')
