from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta, datetime
from flask import g
from flask import json
import subprocess
# from Workflows.workflows import Workflow, WorkflowManager, WorkflowOpener

app = Flask(__name__)
app.secret_key = "autowf"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workflows.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


workflow_url_junction = db.Table('workflow_url_junction',
    db.Column('workflows_id', db.Integer, db.ForeignKey('workflows.id')),                                 
    db.Column('workflow_urls_id', db.Integer, db.ForeignKey('workflow_urls.id')),                                 
)


class workflows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workflow_name = db.Column(db.String(100), nullable=False)
    # website_urls = db.relationship('workflow_urls', secondary=workflow_url_junction, backref='websites')
    # website_urls = db.Column(db.String(500), nullable=False)
    urls = db.relationship('workflow_urls', secondary=workflow_url_junction, backref=db.backref('workflows', lazy='dynamic'))
    hotkeys = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, workflow_name, hotkeys, urls):
        self.workflow_name = workflow_name #
        self.hotkeys = hotkeys
        self.urls = urls
        

    def __repr__(self):
        return f"workflows(id = {self.id}, workflow_name={self.workflow_name}, website_urls={self.website_urls}, hotkeys={self.hotkeys}, date_created={self.date_created})"

class workflow_urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # url_name = db.Column(db.String(100))
    url = db.Column(db.String(500))

    # def __repr__(self):
    #     return f'<workflow_urls:{self.url}>'
    def __init__(self, url):
        # self.url_name = url_name
        self.url = url


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    all_workflows = workflows.query.order_by(workflows.date_created).all()
    chunk_size = 4
    divided_workflows = [all_workflows[i:i + chunk_size] for i in range(0, len(all_workflows), chunk_size)]
    return render_template('dashboard.html', divided_workflows=divided_workflows)
    # return 'Build the dashboard page here.'

@app.route('/createwf', methods=['POST', 'GET']) # 
def createwf():
    if request.method == 'POST':
        workflow_name = request.form['workflow_name']
        hotkeys = request.form['hotkeys']
        # website_urls = request.form['url_input_1']

        '''
        VERSION 1
        '''
        # add_urls_to_workflow = request.form['url_input_${urlCount}']
        
        # new_urls = workflow_urls(url=add_urls_to_workflow)
        # new_workflow = workflows(workflow_name=workflow_name, website_urls=new_urls, hotkeys=hotkeys)
        # new_workflow = workflows(workflow_name=workflow_name, website_urls=website_urls, hotkeys=hotkeys)

        '''
        Version 2
        '''
        
        urls = []
        url_count = int(request.form['urlCount'])

        for i in range(1, url_count + 1):
            url_input_name = f'url_input_{i}'
            url = request.form.get(url_input_name)
            if url:
                urls.append(workflow_urls(url=url))

        new_workflow = workflows(workflow_name=workflow_name, hotkeys=hotkeys, urls=urls)

        try:
            db.session.add(new_workflow)
            db.session.commit()
            return redirect('/dashboard')
        except Exception as e:
            db.session.rollback()  # Roll back the session changes
            print(f"Error occurred: {str(e)}")
            return 'There was an issue creating your workflow.'
    else:
        # all_workflows = workflows.query.order_by(workflows.date_created).all()
        return render_template('createwf.html') # , all_workflows=all_workflows
    
 
@app.route('/delete/<int:id>')
def delete(id):
    worfkflow_to_delete = workflows.query.get_or_404(id)

    try:
        db.session.delete(worfkflow_to_delete)
        db.session.commit()
        return redirect('/dashboard')
    except:
        return 'There was a problem deleting that workflow.'

@app.route('/manage')
def manage():
    return render_template('manage.html')

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
    

# DATABASE = db


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


# workflow_to_open = workflows.get(workflows.workflow_name)
# if workflow_to_open:
#     chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#     # Open the workflow using subprocess or any other method
#     print(f"Opening workflow '{workflows.workflow_name}'...")
#     # Add your code to open the workflow (e.g., subprocess or webbrowser)
#     # For example:
#     # webbrowser.open_new_tab(workflow_to_open.website_urls[0])  # Open the first URL for demonstration
#     subprocess.Popen([chrome_path, '--new-window'] + workflow_to_open.website_urls)
#     print(f"Opened {workflows.workflow_name} workflow in Chrome successfully.")
# else:
#     print(f"Workflow '{workflows.workflow_name}' not found.")


# Determined that it is a database issue
# POSSIBLE UPDATES TO HANDLE MILTIPLE URLS
        #  Retrieve URL count
        # url_count = int(request.form.get('urlCount', 1))

        # if url_count == 1:
        #     # If only one URL is provided, store it as a string
        #     website_urls = request.form['url_input_1']
        # else:
        #     website_urls_list = [request.form[f'url_input_{i}'] for i in range(1, url_count + 1)]
        #     website_urls = json.dumps(website_urls_list)
        
   # website_urls = request.form.getlist('website_urls')  # Assuming your HTML form input is named 'url'
    # hotkeys = request.form['hotkeys']
    # new_workflow = Workflow(workflow_name=workflow_name, website_urls=website_urls, hotkeys=hotkeys)

    
    # return "Build the create workflow page here."