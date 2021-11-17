from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#create a Flask Instance
app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = "123321"
# Initialize database

db = SQLAlchemy(app)

# create model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False )
    email =db.Column(db.String(200), nullable=False, unique=True)
    date_added =db.Column(db.DateTime, default=datetime.utcnow)

    #Crete  A string
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Stisni")


# Create a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Stisni")

#create a route decorator


# def index():
#     return "<h1>Hello, World !</h1>"
@app.route('/')
def index():
    first_name = "John"
    return render_template("index.html", first_name=first_name)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''    
        flash("User Added Successfully")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)

#Create NAme PAge

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Uspesno prihvaceno")
    return render_template("name.html", name = name, form = form)

