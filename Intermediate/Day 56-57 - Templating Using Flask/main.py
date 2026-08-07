from flask import Flask, render_template
import post

post_data = post.Post()
app = Flask(__name__)

@app.route('/post/<n>')
def post_read(n):
    return render_template('post.html',data= post_data.get_post_data(),num=int(n))

@app.route('/')
def home():
    return render_template("index.html",data = post_data.get_post_data())

if __name__ == "__main__":
    app.run(debug=True)
