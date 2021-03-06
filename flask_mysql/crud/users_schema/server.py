from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT * FROM users;")
    return render_template("index.html", all_users = users)

@app.route("/users/new" )
def new_user():

    return render_template("new_user.html")

@app.route("/users/create", methods=["POST"] )
def create_user():

    query = "INSERT INTO users(first_name,last_name,email) VALUES (%(fn)s,%(ln)s,%(email)s);"
    data={
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }

    my_db = connectToMySQL("users_schema")
    userid = my_db.query_db(query,data)


    return redirect("/users/" + str(userid))

@app.route("/users/<int:user_id>",  methods=["GET","POST"] )
def user_info(user_id):
 
    query= "SELECT * FROM users WHERE id= %(id)s;"
    data={
        "id":user_id
    }

    mysql = connectToMySQL("users_schema")
    user = mysql.query_db(query,data)
   
    return render_template("user_info.html", my_user=user )

@app.route("/users/<int:user_id>/edit",  methods=["GET","POST"] )
def edit_user_form(user_id ):

    print("inside user edit function")
    print(user_id)
    query= "SELECT * FROM users WHERE id= %(id)s;"
    data={
        "id":user_id
    }

    mysql = connectToMySQL("users_schema")
    user = mysql.query_db(query,data)
    
   
    return render_template("edit_user.html", my_user=user)

@app.route("/users/<int:user_id>/delete",  methods=["GET","POST"] )
def delete_user(user_id ):

    print("inside delete function")
    print(user_id)

    query= " DELETE FROM users WHERE id= %(id)s;"
    data={
        "id":user_id
    }

    mysql = connectToMySQL("users_schema")
    mysql.query_db(query,data)
    
   
    return redirect("/users")

@app.route("/users/update", methods=["GET","POST"] )
def update_user():
#
    query = "UPDATE users SET first_name = %(fn)s ,last_name = %(ln)s ,email= %(email)s WHERE id = %(id)s;"
    data={
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"],
        "id":request.form["id"]

    }
    print("Inside update form")
    print(data)
    my_db = connectToMySQL("users_schema")
    my_db.query_db(query,data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)