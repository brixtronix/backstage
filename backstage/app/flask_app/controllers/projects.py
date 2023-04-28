from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/save/project')
def new_project():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    return render_template("project_new.html", current_user=User.get_by_id(data))

@app.route('/project/save',methods=['POST'])
def project_new():
    if "user_id" not in session:
        return redirect('/')
    if not Project.validate_project(request.form):
        return redirect('/save/project')
    data ={
        "name": request.form['name'],
        "description": request.form['description'],
        "user_id": session['user_id']
    } 
    Project.save_project(data)
    return redirect('/home')

# view single project
@app.route('/view/project/<int:id>')
def project(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    one_project=Project.get_one_project(data)
    return render_template("one_project.html", current_user=User.get_by_id(data), project=one_project)

# edit render & method
@app.route('/edit/project/<int:id>')
def edit_project(id):
    data = {
        'id': id
    }
    print(data)
    return render_template('project_edit.html', project=Project.get_one_project(data))

@app.route('/project/edit/<int:id>', methods=['POST'])
def project_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Project.validate_project(request.form):
        return redirect(f'/edit/project/{id}')
    data = {
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    Project.update_project(data)
    return redirect('/home')

# delete
@app.route('/project/delete/<int:id>')
def project_destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Project.destroy_project(data)
    return redirect('/home')
