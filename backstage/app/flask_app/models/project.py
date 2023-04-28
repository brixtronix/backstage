from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Project:
    db = "greenroom"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster = None

    @classmethod
    def save_project(cls,data):
        query = "INSERT INTO projects (name,description,user_id,created_at,updated_at) VALUES(%(name)s,%(description)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_projects(cls):
        query = "SELECT * FROM projects JOIN users ON projects.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_projects = []
        for row in results:
            posting_user = User({
                "id":  row['id'],
                "user_name": row['user_name'],
                "biography": row['biography'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            })
            new_project = Project({
                "id":  row['id'],
                "name":  row['name'],
                "description":  row['description'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            new_project.poster = posting_user
            all_projects.append(new_project)
        return all_projects
    
    @classmethod
    def get_one_project(cls, data):
        query = "SELECT projects.*, users.user_name, users.biography, users.email, users.password, users.created_at, users.updated_at FROM projects JOIN users ON users.id = projects.user_id WHERE projects.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            row = results[0]
            poster_name = row['user_name']
            posting_user = User({
                "id":  row['id'],
                "user_name": row['user_name'],
                "biography": row['biography'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            })
            one_project = Project({
                "id":  row['id'],
                "name":  row['name'],
                "description":  row['description'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            one_project.poster = posting_user
            one_project.poster_name = poster_name
            return one_project
        else:
            return None

    @classmethod
    def update_project(cls,data):
        query = "UPDATE projects SET name=%(name)s,description=%(description)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_project(cls,data):
        query  = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_project(projects):
        is_valid = True
        if projects["name"] == 0:
            flash("Name must not be blank","projects")
            is_valid = False
        if projects["description"] == 0:
            flash("Description must not be blank","projects")
            is_valid = False
        return is_valid
