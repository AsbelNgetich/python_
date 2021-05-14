
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

# All users
@app.route("/users")
def index():
    return render_template("index.html", all_users = User.get_all())

# Create user template/route
@app.route("/users/new" )
def new_user():
    return render_template("new_user.html")

# Create user action route
@app.route("/users/create", methods=["POST"] )
def create_user():
    data={
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    userid = User.save(data)
    return redirect("/users/" + str(userid))

# Single user information route
@app.route("/users/<int:user_id>",  methods=["GET","POST"] )
def user_info(user_id): 
    data={
        "id":user_id
    } 
    return render_template("user_info.html", my_user= User.get_user(data) )


#route for editing user
@app.route("/users/<int:user_id>/edit",  methods=["GET","POST"] )
def edit_user_form(user_id ):
    data={
        "id":user_id
    }
       
    return render_template("edit_user.html", my_user= User.get_user(data))

# delete user route
@app.route("/users/<int:user_id>/delete",  methods=["GET","POST"] )
def delete_user(user_id ): 
    data={
        "id":user_id
    }
    User.delete_user(data)
    return redirect("/users")

# update user route
@app.route("/users/update", methods=["GET","POST"] )
def update_user():
    data={
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"],
        "id":request.form["id"]
    }
    User.update_user(data)
    return redirect("/users")