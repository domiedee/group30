from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

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
   

def __init__(self, fname, lname, email, message):
   self.fname = fname
   self.lname = lname
   self.email = email
   self.message = message


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   if request.method == 'POST':
      
      if not request.form['fname'] or not request.form['lname'] or not request.form['email'] or not request.form['message']:
         flash('Please enter all the fields', 'error')
      else:
         user == user(request.form['fname'], request.form['lname'],
            request.form['email'], request.form['message'])
         
         db.session.add(user)
         db.session.commit()
         flash('We value your response')
         return redirect(url_for('contact'))
   return render_template('contact.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)