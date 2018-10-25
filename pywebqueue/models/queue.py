from pywebqueue import db

class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.command