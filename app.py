from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from datetime import datetime

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = "autowf"
app.permanent_session_lifetime = timedelta(minutes=5)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
    # return 'Build the dashboard page here.'

@app.route('/createwf')
def createwf():
    return render_template('createwf.html')
    # return "Build the create workflow page here."

@app.route('/manage')
def manage():
    # return render_template('index.html')
    return 'Build the dashboard page here.'

@app.route('/profile')
def profile():
    # return render_template('index.html')
    return 'Build the profile page here.'

@app.route("/login", methods=["POST", "GET"]) # as second parameter add methods that can be used on the page
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template('login.html')
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template('user.html')
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)