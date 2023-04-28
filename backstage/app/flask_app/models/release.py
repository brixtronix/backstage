from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Release:
    db = "greenroom"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster = None

    @classmethod
    def save_release(cls,data):
        query = "INSERT INTO releases (title,description,release_date,user_id,created_at,updated_at) VALUES(%(title)s,%(description)s,%(release_date)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_releases(cls):
        query = "SELECT * FROM releases JOIN users ON releases.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_releases = []
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
            new_release = Release({
                "id":  row['id'],
                "title":  row['title'],
                "description":  row['description'],
                "release_date": row['release_date'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            new_release.poster = posting_user
            all_releases.append(new_release)
        return all_releases
    
    @classmethod
    def get_one_release(cls, data):
        query = "SELECT releases.*, users.user_name, users.biography, users.email, users.password, users.created_at, users.updated_at FROM releases JOIN users ON users.id = releases.user_id WHERE releases.id = %(id)s;"
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
            one_release = Release({
                "id":  row['id'],
                "title":  row['title'],
                "description":  row['description'],
                "release_date": row['release_date'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            one_release.poster = posting_user
            one_release.poster_name = poster_name
            return one_release
        else:
            return None

    @classmethod
    def update_release(cls,data):
        query = "UPDATE releases SET title=%(title)s,description=%(description)s,release_date=%(release_date)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_release(cls,data):
        query  = "DELETE FROM releases WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_release(releases):
        is_valid = True
        if releases["title"] == 0:
            flash("Title must not be blank","releases")
            is_valid = False
        if releases["description"] == 0:
            flash("Description must not be blank","releases")
            is_valid = False
        if releases["release_date"] == 0:
            flash("Please select a release date.","releases")
            is_valid = False
        return is_valid
