from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    numofbed = IntegerField('Number of Beds', validators=[DataRequired()])
    numofbath = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])

    typeofproperty = SelectField('Type of Property', choices=[('House','House'), ('Apartment','Apartment')])

    textarea = StringField('Textarea',validators=[DataRequired()])
    photo = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png','jpeg'], 'Images only!')])
