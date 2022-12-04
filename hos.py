from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('abc.html') #will look for templates in ./templates

app.run(host='0.0.0.0')