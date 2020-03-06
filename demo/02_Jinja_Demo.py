from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route('/hello')
def hello_world():
    return render_template('index.html', name="Samir Koce", geschlecht="männlich", geburtsdatum="15.15.2097")

@app.route('/geschlecht')
def gescj():
    return render_template('index-g.html', geschlecht="männlich", )

@app.route("/test")
def test():
    return "success"

@app.route('/hello2/')
@app.route('/hello2/<name>')
def begruessung(name=False):
    if name:
         return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"


@app.route("/hello3/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

