from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Photo:
    db = "greenroom"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.photo = data['photo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user_id']
        self.poster = None

    @classmethod
    def save_photo(cls,data):
        query = "INSERT INTO pics (title,description,photo,user_id,created_at,updated_at) VALUES(%(title)s,%(description)s,%(photo)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_photos(cls):
        query = "SELECT * FROM pics JOIN users ON pics.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_photos = []
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
            new_photo = Photo({
                "id":  row['id'],
                "title":  row['title'],
                "description":  row['description'],
                "photo": row['photo'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            new_photo.poster = posting_user
            all_photos.append(new_photo)
        return all_photos
    
    @classmethod
    def get_one_photo(cls, data):
        query = "SELECT pics.*, users.user_name, users.biography, users.photo, users.email, users.password users.created_at, users.updated_at FROM pics JOIN users ON users.id = pics.user_id WHERE pics.id = %(id)s;"
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
            one_photo = Photo({
                "id":  row['id'],
                "title":  row['title'],
                "description":  row['description'],
                "photo": row['photo'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "user_id": row["user_id"]
            })
            one_photo.poster = posting_user
            one_photo.poster_name = poster_name
            return one_photo
        else:
            return None

    @classmethod
    def update_photo(cls,data):
        query = "UPDATE pics SET title=%(title)s,description=%(description)s,photo=%(photo)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy_photo(cls,data):
        query  = "DELETE FROM pics WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_photo(pics):
        is_valid = True
        if pics["title"] == 0:
            flash("Title must not be blank","pics")
            is_valid = False
        if pics["description"] == 0:
            flash("Description must not be blank","pics")
            is_valid = False
        if pics["photo"] == 0:
            flash("Photo link must not be empty","pics")
            is_valid = False
        return is_valid
