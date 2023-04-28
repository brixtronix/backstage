from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Chop:
    db = "greenroom"
    def __init__(self,data):
        self.id = data['id']
        self.skill = data['skill']
        self.studied_for = data['studied_for']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster = None

    @classmethod
    def save_chop(cls,data):
        query = "INSERT INTO chops (skill,studied_for,user_id,created_at,updated_at) VALUES(%(skill)s,%(studied_for)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_chops(cls):
        query = "SELECT * FROM chops JOIN users ON chops.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_chops = []
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
            new_chop = Chop({
                "id":  row['id'],
                "skill":  row['skill'],
                "studied_for":  row['studied_for'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            new_chop.poster = posting_user
            all_chops.append(new_chop)
        return all_chops
    
    @classmethod
    def get_one_chop(cls, data):
        query = "SELECT chops.*, users.user_name, users.biography, users.email, users.password, users.created_at, users.updated_at FROM chops JOIN users ON users.id = chops.user_id WHERE chops.id = %(id)s;"
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
            one_chop = Chop({
                "id":  row['id'],
                "skill":  row['skill'],
                "studied_for":  row['studied_for'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            one_chop.poster = posting_user
            one_chop.poster_name = poster_name
            return one_chop
        else:
            return None

    @classmethod
    def update_chop(cls,data):
        query = "UPDATE chops SET skill=%(skill)s,studied_for=%(studied_for)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_chop(cls,data):
        query  = "DELETE FROM chops WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_chop(chops):
        is_valid = True
        if chops["skill"] == 0:
            flash("Skill must not be blank","chops")
            is_valid = False
        if chops["studied_for"] == 0:
            flash("Please enter how long you have been studying this skill","chops")
            is_valid = False
        return is_valid
