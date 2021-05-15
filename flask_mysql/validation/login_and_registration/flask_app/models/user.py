from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt 
import re

bcrypt = Bcrypt(app)

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # register user class method
    @classmethod
    def register_user(cls,data):

        hashed_pw = bcrypt.generate_password_hash(data['password'])
        data['hashed_pw']= hashed_pw

        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(hashed_pw)s);"
        my_db = connectToMySQL("login_and_registration")
        userid = my_db.query_db(query,data)
        return userid

    # get user class method
    @classmethod
    def get_user(cls, data):

        query= "SELECT * FROM users WHERE email= %(email)s;"
        my_db = connectToMySQL("login_and_registration")
        user_info = my_db.query_db(query,data)

        if len(user_info) <= 0:
            return None
        else:
          return User(user_info[0]) 


    @staticmethod
    def validate_user(data):
        is_valid = True 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        ALPHABET_REGEX = re.compile(r'^[a-zA-Z]+$')
        if len(data['first_name']) < 2 or len(data['first_name']) > 60 :
            flash("First Name must be at least 2 to 60 characters.")
            is_valid = False
        if len(data['last_name']) < 2 or len(data['last_name']) > 60:
            flash("Last Name must be at least 2 to 60 characters.")
            is_valid = False
        if data['password'] == "":
            flash("Password fields cannot be blank!")
            is_valid = False
        if len(data['password']) < 8 or len(data['password']) > 60:
            flash("Password must be at least 8 to 60 characters.")
            is_valid = False
        if data['password'] != data['confirm_password'] :
            flash("Password and Confirm password fields doesn't match.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        if not ALPHABET_REGEX.match(data['first_name']):
            flash("First Name can only be alphabetical!")
            is_valid = False
        if not ALPHABET_REGEX.match(data['last_name']):
            flash("Last Name can only be alphabetical!")
            is_valid = False
    
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email address!")
            is_valid = False
        if data['password'] == "":
            flash("Password fields cannot be blank! ")
            is_valid = False

        return is_valid

