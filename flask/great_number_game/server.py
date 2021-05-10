from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "myrandomesecretkey"

@app.route('/')
def index():
    # compute_pick = random.randit(1,100)

    return render_template('index.html')

@app.route('/compare_numbers', methods=['POST'])
def compare_numbers():

    print("Got number Info")
    comp_number = random.randint(1,100)
    my_number = int(request.form['number'])
    print(my_number)
    print(comp_number)
    session['comp_number']=comp_number
    session['my_number'] = my_number
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)
