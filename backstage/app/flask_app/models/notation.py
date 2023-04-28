from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Note:
    db = "greenroom"
    def __init__(self,data):
        self.id = data['id']
        self.note = data['note']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster = None
        # self.user_who_liked = []

    @classmethod
    def save_notation(cls,data):
        query = "INSERT INTO notations (note,user_id,created_at,updated_at) VALUES(%(note)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_notations(cls):
        query = "SELECT * FROM notations JOIN users ON notations.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_notations = []
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
            new_notation = Note({
                "id":  row['id'],
                "note":  row['note'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            new_notation.poster = posting_user
            all_notations.append(new_notation)
        return all_notations
    
    @classmethod
    def get_one_notation(cls, data):
        query = "SELECT notations.*, users.user_name, users.biography, users.email, users.password, users.created_at, users.updated_at FROM notations JOIN users ON users.id = notations.user_id WHERE notations.id = %(id)s;"
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
            one_notation = Note({
                "id":  row['id'],
                "note":  row['note'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            one_notation.poster = posting_user
            one_notation.poster_name = poster_name
            return one_notation
        else:
            return None

    @classmethod
    def update_notation(cls,data):
        query = "UPDATE notations SET note=%(note)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_notation(cls,data):
        query  = "DELETE FROM notations WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_note(notations):
        is_valid = True
        if notations["note"] == 0:
            flash("Notation must not be blank","notations")
            is_valid = False
        return is_valid
