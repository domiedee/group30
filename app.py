from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.sqlite3"
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class user(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   fname = db.Column(db.String(100))
   lname = db.Column(db.String(50))
   email = db.Column(db.String(10))
   message = db.Column(db.String(2000))    

def __init__(self):
        return '<Entry %r>' & self.id

def __init__(self, fname, lname, email, message):
   self.fname = fname
   self.lname = lname
   self.email = email
   self.message = message

from app import db
db.create_all()

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        message= request.form['message']

        # Validate form data
        if len(fname) == 0 or len(lname) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Form data is valid; move along
            # db.session.add(user)
            db.session.commit()
            flash('We value your response')
            return redirect(url_for('contact'))

    # Render the sign-up page
    return render_template('contact.html', message=error)

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)