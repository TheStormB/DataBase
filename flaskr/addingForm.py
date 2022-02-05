from wtforms import Form, IntegerField, DateField, SelectField, StringField


class AddingForm(Form):
    airport = [('Choppin Airport', 'Choppin Airport'),
               ('Istanbul Airport', 'Istanbul Airport'),
               ('Schiphol Airport', 'Schiphol Airport')]
    Flight_No = IntegerField('Flight Number')
    Arrival_Date = DateField('Date')
    Country = StringField('Country')
    airport_name = SelectField('Airport', choices=airport)
