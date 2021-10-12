from flask_app.config.mysqlconnection import connectToMySQL



class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        my_conn_obj = connectToMySQL('users_schema') 
        users_from_db = my_conn_obj.query_db(query)
        users = []
        for u in users_from_db:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name,last_name,email) VALUES (%(fn)s,%(ln)s,%(email)s);"
        my_db = connectToMySQL("users_schema")
        userid = my_db.query_db(query,data)
        return userid

    @classmethod
    def update_user(cls,data):
            
        query = "UPDATE users SET first_name = %(fn)s ,last_name = %(ln)s ,email= %(email)s WHERE id = %(id)s;"
        my_db = connectToMySQL("users_schema")
        userid = my_db.query_db(query,data)
        return

    @classmethod
    def delete_user(cls,data):
        query= " DELETE FROM users WHERE id= %(id)s;"
        my_db = connectToMySQL("users_schema")
        my_db.query_db(query,data)
        return
    
    @classmethod
    def get_user(cls,data):
        query= "SELECT * FROM users WHERE id= %(id)s;"
        my_db = connectToMySQL("users_schema")
        user_info = my_db.query_db(query,data)
        return user_info
