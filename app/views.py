"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from flask_wtf import FlaskForm
from flask.helpers import send_from_directory
from flask_sqlalchemy import SQLAlchemy

###
# Routing for your application.
###

db = SQLAlchemy(app)
class User(db.Model):
    # Uncomment the line below if you want to set your own table name
    __tablename__ = "property"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    number_of_bedrooms = db.Column(db.Integer())
    number_of_bathrooms = db.Column(db.Integer())
    location = db.Column(db.String(120))
    price = db.Column(db.Float(120))
    type1 = db.Column(db.String(120))
    description = db.Column(db.String(120))
    photo = db.Column(db.String(120))


    def __init__(self,title, number_of_bedrooms,number_of_bathrooms,location,price,type1,description,photo):
        self.title = title
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.type1 = type1
        self.description = description
        self.photo = photo
        
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

app.config['uploads'] = "uploads"

@app.route('/property', methods=['POST', 'GET'])
def property():
    form = PropertyForm()
    if request.method == "POST":
        info = form.title.data
        info1 = form.numofbed.data 
        info2 = form.numofbath.data 
        info3 = form.location.data
        info4 = form.price.data
        info5 = form.typeofproperty.data 
        info6 = form.textarea.data
        info7 = form.photo.data
        info8 = info7.filename
      
        data = User(info, info1,info2,info3,info4,info5,info6,info8)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('properties'))
        flash('The property was sucessfully added!', 'success')
    return render_template('property.html', form=form)



@app.route('/properties', methods=["GET","POST"])
def properties():
    properties_list=[]
    
    properties= db.session.query(User).all()
    return render_template('properties.html', property=properties)

@app.route('/property/<propertyid>')
def propertyid():
    user = User.query.filter_by(id=propertyid).first()
    return render_template('propertyid.html', propertyid=user)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
