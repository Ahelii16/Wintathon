
from flaskmain import db
from flaskmain.models import User
import pandas as pd
db.drop_all()

db.create_all()
data = pd.read_csv("/Users/shefalibansal/Downloads/finaldata.csv")
exec("for i in range(data.shape[0]): db.session.add( User(UX_Design=data['UX_Design'][i], Machine_Learning=data['Machine Learning'][i], Graphic_Design=data['Graphic_Design'][i], Mathematics=data['Mathematics'][i], Web_Development=data['Web Development'][i], C=data['C++'][i], Java=data['Java'][i],Android_Development= data['Android Development'][i], AUTOCAD = data['AUTOCAD'][i], Data_Analytics=data['Data Analytics'][i], Human_Resources=data['Human Resources'][i], Physics=data['Physics'][i], Business_dev= data['Business Development'][i], Deep_Learning=data['Deep Learning'][i],Competitive_Prog= data['Competitive Programming'][i], Open_Source=data['Open Source'][i], English_Comm=data['English Communication'][i], Economics=data['Economics'][i], Chemistry=data['Chemistry'][i], Blockchain=data['Blockchain'][i], Available_Time=data['Available_Time'][i], username=data['name'][i], email=data['email'][i], mobile_number=data['mobile_number'][i], experience=data['experience'][i],Is_Mentor= data['Is_Mentor'][i], skills=data['skills'][i]) )")
db.session.commit()