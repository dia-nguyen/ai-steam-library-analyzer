from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length

class SteamIdForm(FlaskForm):
    """Form for sending steam id"""
    steam_id = StringField('Steam ID', validators=[DataRequired()])
    class Meta:
        csrf = False