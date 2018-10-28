from flask import render_template
from pywebqueue import app, db

queue_example = [
    {"id": 0, "command": "cp somefile.txt otherfile.txt", "status": "DONE", "progress": 100},
    {"id": 1, "command": "rm otherfile.txt", "status": "TODO", "progress": 0},
    {"id": 2, "command": "rm somefile.txt", "status": "IN PROGRESS", "progress": 99}
]

@app.route("/")
def hello():
    return render_template('hello.html', queue=queue_example)
