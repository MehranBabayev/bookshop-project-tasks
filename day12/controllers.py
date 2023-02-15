from flask import render_template 

from app import app
from models import Book




@app.route("/")
def render():
    book = Book.query.all()
    return render_template('index.html', Books = book)


@app.route("/Book/<int:id>")
def book_detail(id):
    book = Book.query.filter_by(id=id).first()
    Books = Book.query.all()
    return render_template('book.html', book = book, Books = Books)
