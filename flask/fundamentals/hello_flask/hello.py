from flask import Flask
app = Flask(__name__)

#localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_word():
    return 'Hello World!'

#localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def coding_dojo():
    return 'Dojo!'

#localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<name>')
def say_flask(name):
    if (name.isnumeric()):
         return "Please reenter a correct name" 
    else:
         return f'Hi {name}!'
       


# localhost:5000/repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<number>/<greetings>')
def multiply_hello(number,greetings):
    if(number.isnumeric() and greetings.isnumeric() == False):
        return int(number) * (greetings + " ")
    else:
        return "Error occured. Please type the correct format" 

@app.errorhandler(404)
def handle_404(e):
    return 'Sorry! No response. Try again'





if __name__=="__main__":
    app.run(debug=True)