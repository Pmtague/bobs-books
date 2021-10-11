import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

load_dotenv()

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BooksModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String())
    title = db.Column(db.String())
    price = db.Column(db.Float())
    year = db.Column(db.String())

    def __init__(self, author, title, price, year):
        self.author = author
        self.title = title
        self.price = price
        self.year = year

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'title': self.title,
            'price': self.price
        }


@app.route('/')
def main():
    return "Hello World!"


@app.route('/books/')
def books():
    try:
        books = BooksModel.query.all()
        return jsonify([book.serialize() for book in books])
    except:
        return(str(Exception))


@app.route('/books/<id>/')
def book_info(id):
    print(request)
    try:
        book = BooksModel.query.get(id)
        return jsonify(book.serialize())
    except:
        return(str(Exception))


if __name__ == "__main__":
    app.run(debug=True)
