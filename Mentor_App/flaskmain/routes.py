
from flask import render_template, url_for, flash, redirect
from flaskmain import app, db
from flaskmain.loginform import LoginForm
from flaskmain.models import User
from flask import Flask, request, Response, render_template, jsonify, session
from flask_login import login_user, current_user, logout_user, login_required

name = None
email = None
calendly_link = None
dictionary=None
a= None

user={'name': 'Shefali Bansal', 'email': ' bansalshefali11@gmail.com',
 'mobile_number': '8447812100',
 'skills': 'c++, java, python ,etc..................................',
 'experience':'web dev, ML, etc.........................'
	
}

skills = ["UX_Design", "Machine Learning", "Graphic_Design", "Mathematics", "Web Development", "C++", "Java", "Android Development", "AUTOCAD", "Data Analytics", "Human Resources", "Physics", "Business Development", "Deep Learning", "Competitive Programming", "Open Source", "English Communication", "Economics", "Chemistry", "Blockchain"]
level = ["None", "Beginner", "Intermediate", "Advanced"]
location = ["Bangalore", "Pune", "Kolkata", "Patna", "Chennai", "Delhi"]
connections = ["1st", "2nd", "3rd+"]
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

@app.route('/findmentor', methods=['POST', 'GET'])
def findmentor():
	print(request.method)
	if(request.method=="POST"):
		print("here")
		skill = request.form.get('skills')
		print(skill)
		experience = request.form.get('levels')
		if skill == "UX_Design":
			a = User.query.order_by(User.UX_Design.desc()).all()
		elif skill == "Machine Learning":
			a = User.query.order_by(User.Machine_Learning.desc()).all()
		elif skill == "Graphic_Design":
			a = User.query.order_by(User.Graphic_Design.desc()).all()
		elif skill == "Mathematics":
			a = User.query.order_by(User.Mathematics.desc()).all()
		elif skill == "Web Development":
			a = User.query.order_by(User.Web_Development.desc()).all()
		elif skill == "C++":
			a = User.query.order_by(User.C.desc()).all()
		elif skill == "Java":
			a = User.query.order_by(User.Java.desc()).all()
		elif skill == "Android Development":
			a = User.query.order_by(User.Android_Development.desc()).all()
		elif skill == "AUTOCAD":
			a = User.query.order_by(User.AUTOCAD.desc()).all()
		elif skill == "Data Analytics":
			a = User.query.order_by(User.Data_Analytics.desc()).all()
		elif skill == "Human Resources":
			a = User.query.order_by(User.Human_Resources.desc()).all()
		elif skill == "Physics":
			a = User.query.order_by(User.Physics.desc()).all()
		elif skill == "Business Development":
			a = User.query.order_by(User.Business_dev.desc()).all()
		elif skill == "Deep Learning":
			a = User.query.order_by(User.Deep_Learning.desc()).all()
		elif skill == "Competitive Programming":
			a = User.query.order_by(User.Competitive_Prog.desc()).all()
		elif skill == "Open Source":
			a = User.query.order_by(User.Open_Source.desc()).all()
		elif skill == "Economics":
			a = User.query.order_by(User.Economics.desc()).all()
		elif skill == "Chemistry":
			a = User.query.order_by(User.Chemistry.desc()).all()
		elif skill == "Blockchain":
			a = User.query.order_by(User.Blockchain.desc()).all()
		else:
			a = User.query.order_by(User.English_Comm.desc()).all()
		print(a)
		return render_template('result.html', dictionary=a)

	return render_template('findmentor.html', skills=skills, levels=level, location=location, connections=connections)



@app.route("/store", methods=['GET', 'POST'])
def store():
	return render_template('store.html')


@app.route("/result",  methods=['GET', 'POST'])
def result():
	return render_template('result.html',dictionary=a)


@app.route("/becomementor", methods=['GET', 'POST'])
def becomementor():
	if request.method == "POST":
		skill = request.form.get('skills')
		experience = request.form.get('levels')
		calendly_link = request.form.get('clylink')
	return render_template('becomementor.html', skills=skills, levels=level)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/test')
def test():
	return redirect(url_for('test.html'))



