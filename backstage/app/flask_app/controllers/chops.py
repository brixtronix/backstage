from flask import render_template, redirect, session, request, flash
from flask_app.__innit__ import app
from flask_app.models.user import User
from flask_app.models.chop import Chop
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/save/chops')
def new_chop():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    return render_template("chops_new.html", current_user=User.get_by_id(data))

@app.route('/chops/save',methods=['POST'])
def chops_new():
    if "user_id" not in session:
        return redirect('/')
    if not Chop.validate_chop(request.form):
        return redirect('/save/chops')
    data ={
        "skill": request.form['skill'],
        "studied_for": request.form['studied_for'],
        "user_id": session['user_id']
    } 
    Chop.save_chop(data)
    return redirect('/home')

# view single chop
@app.route('/view/chops/<int:id>')
def chop(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id": id
    }
    one_chop=Chop.get_one_chop(data)
    return render_template("chops_view.html", current_user=User.get_by_id(data), chop=one_chop)






# edit render & method
@app.route('/edit/chops/<int:id>')
def edit_chop(id):
    data = {
        'id': id
    }
    print(data)
    return render_template('chops_edit.html', chop=Chop.get_one_chop(data))

@app.route('/chops/edit/<int:id>', methods=['POST'])
def chops_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Chop.validate_chop(request.form):
        return redirect(f'/edit/chops/{id}')
    data = {
        "id": id,
        "skill": request.form['skill'],
        "studied_for": request.form['studied_for'],
        "user_id": session['user_id']
    }
    Chop.update_chop(data)
    return redirect('/home')






# delete
@app.route('/chops/delete/<int:id>')
def chop_destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Chop.destroy_chop(data)
    return redirect('/dashboard')
