from flask import Flask
from flask import request
from lite import db
from lite import User
from lite import app
from flask import render_template


@app.route('/name',methods=['GET','POST'])

def Home():
  val = request.form["name"]
  print(val)
  #val= val["name"]
  #val2=request.args.get("age")
  val2=request.form["password"]
  #val2=10
  print(val2)
  val3 = request.form["email"]
  print(val3)
  user1 = User(username=val, email=val3, password=val2)
  #guest = User(username='guest1', email='guest1@example.com', password='54321')
  db.session.add(user1)
  #db.session.add(guest)
  db.session.commit()
  return "Hello World "+val+" age= "+str(val2)

@app.route('/query',methods=['GET'])
def query():
  val = request.args.get("email")
  ad = User.query.filter_by(email=val).first()
  print(ad.username)
  name=ad.username
  #return str(ad)
  return render_template('edit.html', name=ad.username,email=val)

@app.route('/delQuery',methods=['GET'])
def delQuery():
  val = request.args.get("email")
  ad = User.query.filter_by(email=val).first()
  print(ad.username)
  name=ad.username
  #return str(ad)
  return render_template('delete.html', name=ad.username,email=val)
  
@app.route('/update',methods=['POST'])
def update():
  em=request.form["email"]
  na=request.form["user"]
  up=User.query.filter_by(email=em).first()
  up.username=na
  db.session.commit()
  return "success"

@app.route('/delete',methods=['GET','DELETE'])
def delete():
  em=request.args.get("email")
  User.query.filter_by(email=em).delete()
  db.session.commit()
  return "deleted"

@app.route('/displayAll',methods=['GET'])
def displayAll():
  data=User.query.all()
  return render_template('display.html',dataAll=data)

if __name__ == "__main__":
  db.create_all()
 
  al = User.query.all()
  print(al)
  
  app.run(debug=True)