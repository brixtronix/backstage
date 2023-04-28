from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.release import Release
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/save/release')
def new_release():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    return render_template("release_new.html", current_user=User.get_by_id(data))

@app.route('/release/save',methods=['POST'])
def release_new():
    if "user_id" not in session:
        return redirect('/')
    if not Release.validate_release(request.form):
        return redirect('/save/release')
    data ={
        "title": request.form['title'],
        "description": request.form['description'],
        "release_date": request.form['release_date'],
        "user_id": session['user_id']
    } 
    Release.save_release(data)
    return redirect('/home')

# view single release
@app.route('/view/release/<int:id>')
def release(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    one_release=Release.get_one_release(data)
    return render_template("release_view.html", current_user=User.get_by_id(data), release=one_release)

# edit render & method
@app.route('/edit/release/<int:id>')
def edit_release(id):
    data = {
        'id': id
    }
    print(data)
    return render_template('release_edit.html', release=Release.get_one_release(data))

@app.route('/release/edit/<int:id>', methods=['POST'])
def release_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Release.validate_release(request.form):
        return redirect(f'/edit/release/{id}')
    data = {
        "id": id,
        "title": request.form['title'],
        "description": request.form['description'],
        "release_date": request.form['release_date'],
        "user_id": session['user_id']
    }
    Release.update_release(data)
    return redirect('/home')

# delete
@app.route('/release/delete/<int:id>')
def release_destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Release.destroy_release(data)
    return redirect('/dashboard')
