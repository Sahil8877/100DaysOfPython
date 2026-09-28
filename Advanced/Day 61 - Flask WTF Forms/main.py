from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import sys
import markupsafe
sys.modules['flask'].Markup = markupsafe.Markup

from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success", methods=["POST","GET"])
def success():
    return render_template("success.html")

@app.route("/denied", methods=["POST","GET"])
def denied():
    return render_template("denied.html")

app.secret_key = "secret"
class MyForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label="Submit")


@app.route("/login", methods=['POST','GET'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            print("success")
            return redirect(url_for('success'))
        else:
            print("denied")
            return redirect(url_for("denied"))
    return render_template("login.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
