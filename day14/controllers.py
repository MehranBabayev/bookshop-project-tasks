from app import app
from flask import render_template, request , redirect, url_for
from forms import *
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from flask_login import login_user ,logout_user, current_user, login_required

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form1 = RegisterForm()
    form2 = LoginForm()
    if request.method == 'POST':
        form1 = RegisterForm(request.form)
        form2 = LoginForm(request.form)
        if form1.validate_on_submit():
            
            use = Userman(
                name = form1.name.data,
                username = form1.username.data,
                email = form1.email.data, 
                password = generate_password_hash(form1.password.data)
            )
            use.save() 
            return redirect (url_for('login'))
        if form2.validate_on_submit():
            logged_user = Userman.query.filter_by(username=form2.username.data).first()
            if logged_user and logged_user.check_password(form2.password.data):
                login_user(logged_user)
            return redirect (url_for('login'))
    return render_template ('login.html' , form1 = form1, form2 = form2)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))