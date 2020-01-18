
from flask import render_template, url_for, flash, redirect
from flaskmain import app, db
from flaskmain.loginform import LoginForm
from flaskmain.models import User
from flask_login import login_user, current_user, logout_user, login_required


user={'name': 'Shefali Bansal', 'email': ' bansalshefali11@gmail.com',
 'mobile_number': '8447812100',
 'skills': 'c++, java, python ,etc..................................',
 'experience':'web dev, ML, etc.........................'
	
}

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			login_user(user, remember=form.remember.data)
			# next_page = request.args.get('next')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')

	return render_template('login.html',title='login',form=form)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('profile.html')

@app.route('/findmentor', methods=['GET', 'POST'])
def findmentor():
	colours = ['Red', 'Blue', 'Black', 'Orange']
	return render_template('findmentor.html', colours=colours)


@app.route("/store", methods=['GET', 'POST'])
def store():
	return render_template('store.html')

@app.route("/becomementor", methods=['GET', 'POST'])
def becomementor():

	return render_template('becomementor.html')


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/test')
def test():

	return redirect(url_for(''))



