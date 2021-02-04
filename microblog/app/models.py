from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(64), unique=True)
    email = db.Column(db.VARCHAR(120), unique=True)
    password_hash = db.Column(db.VARCHAR(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)









