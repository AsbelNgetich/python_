from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt(app)


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
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }

    isvalid = User.validate_user(data)

    if isvalid:
        User.register_user(data)
        session['user_first_name'] = request.form["first_name"]
        return redirect("/success") 

    return redirect("/")

#Login route
@app.route("/login", methods = ["POST"] )
def login_user():

    data= {
        "email": request.form["email"],
        "password": request.form["password"]
       
    }
    #check for validations
    isvalid = User.validate_login(data)

    if isvalid:
        new_data = {    
        "email": request.form["email"]
         }
        user = User.get_user(new_data)
        if user == None:
            flash("Your email is invalid!")
            return redirect('/')
        
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash('Your Password is incorrect!')
            return redirect('/')
        
        session['user_id'] = user.id
        session['user_first_name'] = user.first_name
        session['user_email']= user.email
        return redirect("/success")  
    else:
        return redirect('/')

  
    


#success route
@app.route("/success")
def main_page():

    if not session.get("user_first_name") is None:
        return render_template("main_page.html")
    else:
        return redirect('/')


#Log out route
@app.route("/logout")
def logout_user():
    #clear sessions
    session.clear()
    # redirect back to login page
    return redirect("/")







