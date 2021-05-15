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
def save(cls,data):
    query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
    my_db = connectToMySQL("login_and_registration")
    userid = my_db.query_db(query,data)
    return userid