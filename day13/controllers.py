from flask import render_template , request
from models import *
from app import app
from forms import ContactForm
    





@app.route("/Book/<int:id>" , methods = ['GET', 'POST'])
def book_detail(id):
    book = Book.query.filter_by(id=id).first()
    Books = Book.query.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate_on_submit():
            contact = Contact(
                Your_Name = form.Your_Name.data,
                Email_Address = form.Email_Address.data,
                Message = form.Message.data,
                
            )
            contact.save()
        comments=Contact.query.all()
    return render_template('book.html', book = book, Books = Books, form=form,comments=comments)