from flask import Flask
from flask import render_template, url_for, request
import requests
import dotenv, os
dotenv.load_dotenv()
from smtplib import SMTP

get_blog_data = requests.get("https://api.npoint.io/25ebe1184a9fe02af7b8").json()
print(get_blog_data)

app = Flask(__name__)

@app.route("/")
def main():
    url_for('static', filename='css/style.css')
    return render_template("index.html",data=get_blog_data)

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

@app.route("/contact", methods=['POST'])
def contact_form_data():
    url_for("static", filename="css/style.css")
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    with SMTP(host="smtp.gmail.com", port=587) as conn:
        conn.starttls()
        sub = "You got a new message!"
        msg = f"Subject: {sub}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_EMAIL_PASS')
        receiver_email = os.getenv('RECEIVER_EMAIL')
        conn.login(user=sender_email,password=sender_password)
        conn.sendmail(msg=msg.encode("utf-8"),from_addr=sender_email,to_addrs=receiver_email)

        return render_template("contact.html",submitted=True)
    
    return render_template("contact.html",submitted=False)

if __name__ == '__main__':
    app.run(debug=True)