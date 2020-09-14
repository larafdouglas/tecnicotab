from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User,Obra


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	submit= SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LevantamentoForm(FlaskForm):

	ponto=StringField('Ponto número')
	mira_superior=IntegerField('Leitura do fio superior')
	mira_medio=IntegerField('Leitura do fio medio')
	mira_inferior=IntegerField('Leitura do fio inferior')
	ang_vertical_g=IntegerField('Ângulo vertical em graus')
	ang_vertical_m=IntegerField('Ângulo vertical em minutos')
	ang_vertical_s=IntegerField('Ângulo vertical em segundos')
	ang_horizontal_g=IntegerField('Ângulo horizontal em graus')
	ang_horizontal_m=IntegerField('Ângulo horizontal em minutos')
	ang_horizontal_s=IntegerField('Ângulo horizontal em segundos')
	submit=SubmitField('Enviar')

class ObraForm(FlaskForm):
	nome_obra=StringField('Obra',validators=[DataRequired()])
	submit1=SubmitField('Enviar')
	
class DeleteForm(FlaskForm):
	submit=SubmitField('Deletar')


