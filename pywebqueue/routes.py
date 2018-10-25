from flask import render_template
from pywebqueue import app, db

queue_example = [
    {"id": 0, "command": "cp somefile.txt otherfile.txt"},
    {"id": 1, "command": "rm otherfile.txt"},
    {"id": 2, "command": "rm somefile.txt"}
]

@app.route("/")
def hello():
    return render_template('hello.html', queue=queue_example)
