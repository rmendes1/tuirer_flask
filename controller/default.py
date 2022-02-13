from app import app, db, lm
from flask import render_template, flash, redirect, url_for
from model.forms import LoginForm
from model.tables import User
from flask_login import login_user, logout_user

from model.tables import User
from model.forms import LoginForm

@lm.user_loader #loads the user and returns his actual data
def load_user(id):
    return User.query.filter_by(id=id).first() #session token

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first() #check if user already exists

        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in.')
            return redirect(url_for("index"))


        else:
            flash('Login is invalid.')

    return render_template('login.html', form = form)




@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


#Working with CRUD
# This is a testing function to be improved in the future
@app.route("/teste/<info>")
@app.route("/teste", defaults = {"info": None})

def teste(info):
    i = User("paulie321", "thepassword1", "Paulie", "pauliesopranos@hotmail.com") #fictional user
    db.session.add(i)
    db.session.commit()

    return "User added"



    #@app.route("/test/<info>")
    #@app.route("/test", defaults = {"info": None})

    #def test(info):
        #i = User("paulie321", "thepassword1", "Paulie", "pauliesopranos@hotmail.com")
        #db.session.add(i)
        #db.session.commit()

        #r = User.query.filter_by(username="thepunisher").all()
        #print(r)
        #return r

        #return "Ok"
