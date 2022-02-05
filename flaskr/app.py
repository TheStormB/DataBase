import os

import data as data
import form as form
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
# from flask_marshmallow import Marshmallow
from addingForm import AddingForm

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Berke.teksas1",
        database="airportdatabase"
    )
except:
    print("--------------It can't connect--------------")


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Berke.teksas1@localhost/airportdatabase'
app.config['SQLALCHEMY_TRACK_URI'] = False

db = SQLAlchemy(app)


# ma = Marshmallow(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Check In':
            return checkIn()
        elif request.form['submit_button'] == 'Flight Logs':
            return flighLogs()
    elif request.method == 'GET':
        return render_template("index.html", form=form)


@app.route('/checkIn')
def checkIn():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM airportdatabase.tickets")
    data = mycursor.fetchall()
    return render_template("checkIn.html", data=data)


@app.route('/FlightLogs')
def flighLogs():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM airportdatabase.departuredetails")
    data = mycursor.fetchall()
    # if request.method == 'POST':
    #     # if request.form['']
    return render_template("flightLogs.html", data=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddingForm(request.form)
    # if request.method == 'POST' and form.validate():
        # arrival = form(form.Flight_No.data,
        #                   form.Arrival_Date.data, form.Country.data,
        #                   form.airport_name.data)

    # mydb.add(arrival)
    return render_template('add.html', form=form)




if __name__ == "__main__":
    app.run(debug=True)
