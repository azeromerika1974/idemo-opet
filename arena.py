from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql:///user.db"
db= SQLAlchemy(app)

class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=30), nullable=False, unique=True)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/loginn")
def logn_page():
    return render_template("login.html")



if __name__=="__main__":
    app.run(debug=True)