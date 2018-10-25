from pywebqueue import app, db

@app.route("/")
def hello():
    return "Hello World!"
