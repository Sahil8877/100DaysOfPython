import main
from flask import Flask,render_template

# instance of flask application
app = Flask(__name__)
count_of_hazardous_object = len(main.hazardous_astro)
date = main.START_DATE
time = main.TIME
data = {
    'Name': main.closes_astro_list['name'],
    'Date' : main.closes_astro_list['date'],
    'Time' : main.closes_astro_list['time'],
    'Miss Distance' : float(main.closes_astro_list['miss_dist']),
    'Distance From Moon' : float(main.closes_astro_list['dist_from_moon']),
    'Velocity' : main.closes_astro_list['velocity'],
}

@app.route("/")
def hello_world():
    return render_template('name.html',data=data,count=count_of_hazardous_object,date = date,time = time)

if __name__ == '__main__':  
   app.run()


