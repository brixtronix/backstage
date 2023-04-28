from flask_app.__innit__ import app

from flask_app.controllers.users import User
from flask_app.controllers.notations import Note
from flask_app.controllers.projects import Project
from flask_app.controllers.chops import Chop
from flask_app.controllers.releases import Release


if __name__=="__main__":
    app.run(debug=True)