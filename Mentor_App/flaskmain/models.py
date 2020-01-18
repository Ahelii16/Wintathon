from datetime import datetime
from flaskmain import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    skills = db.Column(db.String(1000), nullable=False)
    experience = db.Column(db.String(1000), nullable=False)
    UX_Design = db.Column(db.Integer, nullable=False)
    Machine_Learning = db.Column(db.Integer, nullable=False)
    Mathematics = db.Column(db.Integer, nullable=False)
    Web_Development = db.Column(db.Integer, nullable=False)
    C = db.Column(db.Integer, nullable=False)
    Java = db.Column(db.Integer, nullable=False)
    Android_Development = db.Column(db.Integer, nullable=False)
    AUTOCAD = db.Column(db.Integer, nullable=False)
    Data_Analytics = db.Column(db.Integer, nullable=False)
    Human_Resources = db.Column(db.Integer, nullable=False)
    Physics = db.Column(db.Integer, nullable=False)
    Business_dev = db.Column(db.Integer, nullable=False)
    Deep_Learning = db.Column(db.Integer, nullable=False)
    Competitive_Prog = db.Column(db.Integer, nullable=False)
    Open_Source = db.Column(db.Integer, nullable=False)
    English_Comm = db.Column(db.Integer, nullable=False)
    Economics = db.Column(db.Integer, nullable=False)
    Chemistry = db.Column(db.Integer, nullable=False)
    Blockchain = db.Column(db.Integer, nullable=False)
    Available_Time = db.Column(db.String(200), nullable=False)
    Is_Mentor = db.Column(db.Integer, nullable=False)
    Graphic_Design= db.Column(db.Integer, nullable=False)



    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.mobile_number}')"