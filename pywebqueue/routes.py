from flask import render_template
from pywebqueue import app, db

queue_example = [
    {"id": 0, "command": "cp somefile.txt otherfile.txt", "status": "DONE"},
    {"id": 1, "command": "rm otherfile.txt", "status": "TODO"},
    {"id": 2, "command": "rm somefile.txt", "status": "IN PROGRESS"}
]

@app.route("/")
def hello():
    return render_template('hello.html', queue=queue_example)
