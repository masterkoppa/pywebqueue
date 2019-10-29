from flask import render_template
from pywebqueue import app, db

queue_example = [
    {
        "id": 0, 
        "command": "cp somefile.txt otherfile.txt", 
        "status": "DONE", 
        "progress": 100,
        "output": "test\ntest\ntest\n"
    },
    {
        "id": 1, 
        "command": "rm otherfile.txt", 
        "status": "TODO", 
        "progress": 0,
        "output": "testing\ntesting\ntesting\n"
    },
    {
        "id": 2, 
        "command": "rm somefile.txt", 
        "status": "IN PROGRESS", 
        "progress": 99,
        "output": "boo"
    }
]

@app.route("/")
def index():
    return render_template('index.html', queue=queue_example)
