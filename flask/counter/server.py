from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.secret_key = "myverysecretkey" 

@app.route('/')
def index():

    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] +=1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():

    session.clear()

    return redirect('/')

@app.route('/reset_counter')
def reset_counter():
    session.clear()
    return redirect('/')

@app.route('/add_visits')
def add_visits():
    session['counter'] +=2
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)