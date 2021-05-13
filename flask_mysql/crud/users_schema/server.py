from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
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
    my_db.query_db(query,data)
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)