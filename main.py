from flask import Flask
from flask_sqlalchemy import SQLAlchemy, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa'
db = SQLAlchemy(app)

# Create model for database, limiting to data that will be needed


class BooksModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.String())
    title = db.Column(db.String())
    price = db.Column(db.Float())
    year = db.Column(db.String())


@app.route('/')
def main():
    return "Hello World!"


# @app.route('/books/')
# def book(id):
#     books = BooksModel.query.filter_by(id='id')
#     return {books}


@app.route('/books/<int:id>')
def book_info(id):
    books = BooksModel.query.filter_by(id=id)
    print(books)
    return {
        'title': BooksModel.title,
        'price': BooksModel.price,
        'method': request.method
    }


if __name__ == "__main__":
    app.run(debug=True)
