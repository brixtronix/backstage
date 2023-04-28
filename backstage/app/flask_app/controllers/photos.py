from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.pic import Photo
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/save/photo')
def new_photo():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    return render_template("media_new.html", current_user=User.get_by_id(data))

@app.route('/photo/save',methods=['POST'])
def photo_new():
    if "user_id" not in session:
        return redirect('/')
    if not Photo.validate_photo(request.form):
        return redirect('/save/photo')
    data ={
        "title": request.form['title'],
        "description": request.form['description'],
        "photo": request.form['photo'],
        "user_id": session['user_id']
    } 
    Photo.save_photo(data)
    return redirect('/home')

# view single photo
@app.route('/view/photo/<int:id>')
def photo(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    one_photo=Photo.get_one_photo(data)
    return render_template("media_view.html", current_user=User.get_by_id(data), photo=one_photo)

# edit render & method
@app.route('/edit/photo/<int:id>')
def edit_photo(id):
    data = {
        'id': id
    }
    print(data)
    return render_template('media_edit.html', photo=Photo.get_one_photo(data))

@app.route('/photo/edit/<int:id>', methods=['POST'])
def photo_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Photo.validate_photo(request.form):
        return redirect(f'/edit/photo/{id}')
    data = {
        "id": id,
        "title": request.form['title'],
        "description": request.form['description'],
        "photo": request.form['photo'],
        "user_id": session['user_id']
    }
    Photo.update_photo(data)
    return redirect('/home')

# delete
@app.route('/photo/delete/<int:id>')
def photo_destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Photo.destroy_photo(data)
    return redirect('/home')
