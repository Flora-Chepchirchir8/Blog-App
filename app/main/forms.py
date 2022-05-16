from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


class PitchForm(FlaskForm):
    title = StringField('Blog Title')
    category = SelectField(u'Blog Category', choices=[('inspiration', 'Blog')])
    pitch = TextAreaField('Blog content')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Drop Comment')
    submit = SubmitField('Post Comments')

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class Downvote(FlaskForm):
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')