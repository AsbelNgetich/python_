from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User



# home page
@app.route("/")
def index():
    return render_template("login_page.html")


# register user route
@app.route("/register", methods = ["POST"])
def register_user():

  data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        # "password": request.form["hash"]
    }
    # userid = User.save(data)





    return redirect("/success")

#Login route
@app.route("/login", methods = ["POST"] )
def login_user():
    #check for validations
    #store sessions
    # redirect to success page
    return redirect("/success")


#success route
@app.route("/success")
def main_page():

    return render_template("main_page.html")


#Log out route
@app.route("/logout")
def logout_user():
    #clear sessions
    # redirect back to login page
    return redirect("/")







