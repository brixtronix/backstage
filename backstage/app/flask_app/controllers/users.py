from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.notation import Note
from flask_app.models.project import Project
from flask_app.models.chop import Chop
from flask_app.models.release import Release
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/register',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "user_name": request.form['user_name'],
        "biography": request.form['biography'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/home')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email Not Found", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/home')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    notes = Note.get_all_notations()
    projects = Project.get_all_projects()
    chops = Chop.get_all_chops()
    releases = Release.get_all_releases()
    return render_template("home.html", current_user=User.get_by_id(data), all_notations=notes, all_projects=projects, all_chops=chops, all_releases=releases)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')