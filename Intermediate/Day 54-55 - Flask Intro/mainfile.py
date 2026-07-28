from flask import Flask
import random

app = Flask(__name__)

random_num = random.randrange(1,10)

def high_low(func):
    def wrap(**kwargs):
        num = func(**kwargs)
        print("num",type(num))

        if num < random_num:
            return "<div style='text-align:center'><em><h2>Think bigger!</h2></em>" \
            "<img style='width:500px; height:500px;' style='align:center' src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjlxcXN2MG4zcG16NG42ejhqazc2dTBxMG51MWJlNTRmNmZxdGF0MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RuYPi0HyBnOxy/giphy.gif'></img></div>"

        elif num > random_num:
            return "<div style='text-align:center'><em><h2>Try something smaller.</h2></em>" \
            "<img style='width:500px; height:500px;' src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjlxcXN2MG4zcG16NG42ejhqazc2dTBxMG51MWJlNTRmNmZxdGF0MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8TT8VjZTZGWQw/giphy.gif'></img></div>"
   
        return "<div style='text-align:center'><em><h1>🎉 Correct!</h1></em>" \
        "<img style='width:500px; height:500px;' src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ODF5OTNmMWh6NDlkMWcwaHlheW9mbmFpOW1pcHM5aGV4aGliaW1tdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PklKBQ4bj7XXRHByqs/giphy.gif'></img></div>"
    
    return wrap

@app.route("/")
def homepage():
    return "<div style='text-align:center'><em><h2>Welcome to Guess the Number!</h2>" \
    "<br>I'm thinking of a number between 1 and 9." \
    "<br>Type a number in the URL. " \
    "<br>Example: /5</em></div>"

@app.route("/<int:num>")
@high_low
def main(num):
    return num

if __name__ == '__main__':
    app.run(debug=True)