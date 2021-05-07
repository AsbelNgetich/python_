from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:x>')
def flexible_row(x):
    x = int(x/2)
    
    return render_template("flexible_rows.html",x=x)


if __name__=="__main__":
    app.run(debug=True)


