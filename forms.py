# 首页登录表单

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

userIDs = ['123456']

class LoginForm(FlaskForm):
    userID = StringField(validators=[DataRequired(),Length(6)], render_kw={'placeholder': 'A string of random numbers'})
    submit = SubmitField()
    def validate_userID(self, field):
        if field.data not in userIDs:
            raise ValidationError('Invalid ID!')