from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, InputRequired
from market.models import User
from flask_wtf.file import FileField, FileAllowed

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    firstName = StringField(label='First Name:', validators=[Length(min=1, max=30), DataRequired()])
    lastName = StringField(label='Last Name:', validators=[Length(min=1, max=30), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')

class createListing(FlaskForm):
    location = StringField('City', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    bed = IntegerField('Bed', validators=[DataRequired()])
    bath = IntegerField('Bath', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    picture = FileField(default='userimage.png', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add listing')


class deleteUser(FlaskForm):
    submit = SubmitField(label="Delete User")

    
class changePasssword(FlaskForm):
    new_password = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label ='Submit')

class searchListing(FlaskForm):
    query = StringField('Search for property...', validators=[DataRequired()])
    submit = SubmitField('Search')