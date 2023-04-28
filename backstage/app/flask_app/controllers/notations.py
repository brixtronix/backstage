from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.notation import Note
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/save/notation')
def new_notation():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    return render_template("notation_new.html", current_user=User.get_by_id(data))

@app.route('/notation/save',methods=['POST'])
def notation_new():
    if "user_id" not in session:
        return redirect('/')
    if not Note.validate_note(request.form):
        return redirect('/save/notation')
    data ={
        "note": request.form['note'],
        "user_id": session['user_id']
    } 
    Note.save_notation(data)
    return redirect('/home')

@app.route('/view/notation/<int:id>')
def notation(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    one_notation=Note.get_one_notation(data)
    return render_template("notation_view.html", current_user=User.get_by_id(data), one_note=one_notation)

@app.route('/edit/notation/<int:id>')
def edit_notation(id):
    data = {
        'id': id
    }
    print(data)
    return render_template('notation_edit.html', one_note=Note.get_one_notation(data))

@app.route('/notation/edit/<int:id>', methods=['POST'])
def notation_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Note.validate_note(request.form):
        return redirect(f'/edit/notation/{id}')
    data = {
        "id": id,
        "note": request.form['note'],
        "user_id": session['user_id']
    }
    Note.update_notation(data)
    return redirect('/home')

@app.route('/notation/delete/<int:id>')
def notation_destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Note.destroy_notation(data)
    return redirect('/home')
