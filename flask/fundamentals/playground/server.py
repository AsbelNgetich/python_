from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():

    return render_template("play.html")

@app.route('/play/<int:x>')
def play_times(x):

    return render_template("play_times.html", x = x)



@app.route('/play/<int:x>/<color>')
def colored_boxes(x,color):

    return render_template("colored_boxes.html", x = x, color=color)


if __name__=="__main__":
    app.run(debug= True)