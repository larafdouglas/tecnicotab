from app import app,db
from flask import Flask,render_template, flash, redirect, request, url_for, jsonify
from app.forms import LoginForm,RegistrationForm,LevantamentoForm,ObraForm, DeleteForm
from app.models import User,Post,Obra,Ponto
from app.mathfunctions import PontoMath

from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,'Obra':Obra,'Ponto':Ponto}



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html') 


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/lancar_obra',methods=['GET','POST'])
@login_required
def lancar_obra():
	form = ObraForm()
	obras2=Obra.query.all()


	if current_user.is_authenticated:
		g=User.query.get(current_user.get_id())

	if form.submit1.data and form.validate():
		obra=Obra(nome_obra=form.nome_obra.data,author=g)
		db.session.add(obra)
		db.session.commit()
		flash('Obra cadastrada com sucesso!')
		return redirect(url_for('topotab'))
	return render_template('lancar_obra.html',form=form,obras=obras2) 


@app.route('/delete/<int:obra_id>', methods=['GET','POST'])
def delete(obra_id):
	obra = Obra.query.get(obra_id)
	db.session.delete(obra)
	db.session.commit()
	return redirect(url_for('topotab'))


@app.route('/deletepoint/<int:point_id>', methods=['GET','POST'])
def deletepoint(point_id):
	point = Ponto.query.get(point_id)
	db.session.delete(point)
	db.session.commit()
	obra_do_ponto=point.obra_id
	levantamento=Obra.query.get(obra_do_ponto)


	pontos=Ponto.query.filter_by(obra_id=obra_do_ponto).all()

	keys=[]
	iss=[]

	for key,i in enumerate(pontos):
		keys.append(key)
		iss.append(i.id)

	for n,i in enumerate(iss):
		update=Ponto.query.filter_by(id=i).first()
		update.ponto=n+1
	db.session.commit()
	#print(keys)
	#print(iss)
	return redirect(url_for('tabela',obra_id=levantamento.id))
	#return jsonify(levantamento.id)




@app.route('/lancar_ponto/<int:obra_id>',methods=['GET','POST'])
def lancar_ponto(obra_id):
	o=Obra.query.get(obra_id)
	obra = Obra.query.filter_by(id=obra_id).one()
	form = LevantamentoForm()
	pontos=Ponto.query.filter_by(obra_id=obra_id).all()

	if form.validate_on_submit():
		pontomath1=PontoMath(form.mira_superior.data,form.mira_medio.data,form.mira_inferior.data,form.ang_vertical_g.data,form.ang_vertical_m.data,form.ang_vertical_s.data)
		ponto=Ponto(ponto=(len(pontos))+1,mira_superior=form.mira_superior.data,mira_medio=form.mira_medio.data,mira_inferior=form.mira_inferior.data,ang_vertical_g=form.ang_vertical_g.data,ang_vertical_m=form.ang_vertical_m.data,ang_vertical_s=form.ang_vertical_s.data,ang_horizontal_g=form.ang_horizontal_g.data, ang_horizontal_m=form.ang_horizontal_m.data,ang_horizontal_s=form.ang_horizontal_s.data,obra=o,dist_horizontal=(pontomath1.calc_dist()/1000))
		db.session.add(ponto)
		db.session.commit()
		#form.ponto.data=(len(pontos))+1
		print(len(pontos))

		flash('Ponto %s lançado com sucesso!' %form.ponto.data)
		return redirect(url_for('lancar_ponto',obra_id=obra_id))
	return render_template('lancar_ponto.html', form=form, obra=obra) 

@app.route('/tabela/<int:obra_id>',methods=['GET','POST'])
def tabela(obra_id):
	pontos=Ponto.query.filter_by(obra_id=obra_id).all()
	return render_template('tabela.html',pontos=pontos)



@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect('/login')
		login_user(user,remember=form.remember_me.data)
		next_page=request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('topotab')
		return redirect(next_page)
		
	return render_template('login.html', form=form) 


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/topotab')
@login_required
def topotab():
	if current_user.is_authenticated:
		g=User.query.get(current_user.get_id())
	obras=g.obras.all()
	return render_template('topotab.html',obras=obras)










'''@app.route('/lancar_ponto')
def lancar_ponto():
    form = LevantamentoForm()
    
    return render_template('lancar_ponto.html', title='Register', form=form)




		#flash('Você está logado como {}, remember_me{}'.format(form.username.data, form.remember_me.data))'''
		


