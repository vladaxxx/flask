from flask import Flask, render_template


#create a Flask Instance
app = Flask(__name__)

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


