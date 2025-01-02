from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_new_datetime(date_str, time_str, hours_to_add):
    given_datetime_str = date_str + ' ' + time_str
    given_datetime = datetime.strptime(given_datetime_str, '%d-%m-%Y %H:%M:%S')
    new_datetime = given_datetime + timedelta(hours=hours_to_add)
    return new_datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_str = request.form['date']
        time_str = request.form['time']
        hours_to_add = int(request.form['hours'])
        new_datetime = calculate_new_datetime(date_str, time_str, hours_to_add)
        return render_template('index.html', new_datetime=new_datetime)
    return render_template('index.html', new_datetime=None)

if __name__ == '__main__':
    app.run(debug=True)
