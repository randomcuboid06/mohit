from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from PIL import Image 

# Creating list of Month and Share_buy for Plotting Line Graph 
Month = ['January', 'February', 'March'] 
Share_buy = [10, 17, 30] 

# Plotting Line Graph 
plt.title("Share's Buy in a month") 
plt.xlabel('Months') 
plt.ylabel("No of Share's") 
plt.plot(Month, Share_buy) 

plt.savefig(r'C:\Users\admin\Desktop\VNR\mohit\static\someimage.png') 


import os

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'mohit.db')
app.config['SECRET_KEY'] = 'very secret key'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String, primary_key=True)

@app.route('/')
def home():
    return render_template('some.html')

@app.route('/save', methods=['GET', "POST"])
def save():
    if request.method == "GET":
        return render_template('input.html')
    else:
        name = request.form.get('name')
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return 'USER SAVED'
    
@app.route('/users')
def users():
    names = User.query.all()
    print(names)
    return render_template('names.html', names=names)
        


db.create_all()
app.run(debug=True)
