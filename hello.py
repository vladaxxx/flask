from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "123321"

# Create a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Stisni")

#create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello, World !</h1>"

def index():
    first_name = "John"
    return render_template("index.html", first_name=first_name)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


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

