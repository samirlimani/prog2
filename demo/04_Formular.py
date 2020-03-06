from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route("/hello3/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        abstand = "abstand\n"
        name_person = request.form['name']
        rueckgabe_name = "Hello " + name_person + "!"
        return rueckgabe_string + rueckgabe_name


    return render_template("das_template.html", dinger=["Eins", "Zwei", "Drei"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
