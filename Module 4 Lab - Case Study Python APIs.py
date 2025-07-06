from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.model):
 id = db.Column(db.Integer, primarykey=True)
 book_name = db.Column(db.String(80), unique=True)
 author = db.Column(db.String(80), unique=False )
 publisher = db.Column(db.String(80,) unique=False)

 def __repr__(self):
     return f"{self.book_name} - {self.author} - {self.publisher}"


@app.route('/books')
def getbooks():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'book_name': book.name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/books/'<id>')
def get_book(id):
    book = Book.query.get(id)
    return {"name": book.name, "author": book.author, "publisher": book.publisher }

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['name'], author=request.jason['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return "Added successfully"

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return "Deleted successfully"
