from app import db,login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(UserMixin, db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),index=True,unique=True)
	email=db.Column(db.String(120),index=True,unique=True)
	password_hash=db.Column(db.String(128))
	posts=db.relationship('Post',backref='author',lazy='dynamic')
	obras=db.relationship('Obra',backref='author',lazy='dynamic')
	

	def set_password(self,password):
		self.password_hash=generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.password_hash, password)


	def __repr__(self):
		return 'User {}'.format(self.username)


class Post(db.Model):
	id= db.Column(db.Integer, primary_key=True)
	body=db.Column(db.String(140))
	timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


	def __repr__(self):
		return 'Post {}'.format(self.body)


class Obra(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	nome_obra=db.Column(db.String(140))
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
	pontos=db.relationship('Ponto',backref='obra',lazy='dynamic')

	def __repr__(self):
		return '{}'.format(self.nome_obra)


class Ponto(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	ponto=db.Column(db.Integer)
	mira_superior=db.Column(db.Integer)
	mira_medio=db.Column(db.Integer)
	mira_inferior=db.Column(db.Integer)
	ang_vertical_g=db.Column(db.Integer)
	ang_vertical_m=db.Column(db.Integer)
	ang_vertical_s=db.Column(db.Integer)
	ang_horizontal_g=db.Column(db.Integer)
	ang_horizontal_m=db.Column(db.Integer)
	ang_horizontal_s=db.Column(db.Integer)
	dist_horizontal=db.Column(db.Integer)
	obra_id=db.Column(db.Integer, db.ForeignKey('obra.id'))

	def __repr__(self):
		return 'Ponto numero {}'.format(self.ponto)







