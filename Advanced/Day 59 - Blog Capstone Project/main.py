from flask import Flask
from flask import render_template, url_for
import requests

get_blog_data = requests.get("https://api.npoint.io/25ebe1184a9fe02af7b8").json()
print(get_blog_data)

app = Flask(__name__)

@app.route("/home")
def home():
    url_for('static', filename='css/style.css')
    return render_template("index.html",data=get_blog_data)

@app.route("/about")
def about():
    url_for("static", filename="css/style.css")
    return render_template("about.html")

@app.route("/post/<post_num>")
def post(post_num):
    url_for("static", filename="css/style.css")
    return render_template("post.html",data=get_blog_data[int(post_num)])

@app.route("/contact")
def contact():
    url_for("static", filename="css/style.css")
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)