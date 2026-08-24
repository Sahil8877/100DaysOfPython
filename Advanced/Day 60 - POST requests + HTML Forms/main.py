from flask import Flask
from flask import render_template
from flask import request
from smtplib import SMTP


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def get_data():
    name = request.form['name']
    passw = request.form['passw']

    return render_template("login.html",name=name,passw=passw)

if __name__ == '__main__':
    app.run(debug=True)
