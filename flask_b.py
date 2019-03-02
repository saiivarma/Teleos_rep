from flask import Flask
from flask import url_for
from flask import render_template
from flask import request,redirect
import db
import MySQLdb
app= Flask(__name__)
@app.route('/')
def hello():
	redirect(url_for(login))

@app.route('/login',methods=('POST','GET')
def login():
#Login page redirects
	error=None
	if request.method=='POST':
		Eid= request.form['eid']
		username= request.form['username']
		password=request.form['password']
#redirect to different dashboard based on the eid of the employee
		if login(username,password):
			if Eid in range(1,100):
				session.clear()
				session['user_id'] = user['id']
				return render_template('manager.html')
			elif Eid in range(101,500):
				session.clear()
				session['user_id']=user['id']
				return render_template('teamleader.html')
			else:
				session.clear()
				session['user_id']=user[id]
				return render_template(emp.html)
		else:
			flash("Incorrect Credentials")
@app.route('/form_validation')
def create(): 
#send data from signup form to the database 
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		eid=request.form['eid']
		signup(username,eid,password)
		return redirect(url_for('login'))
		
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for(login))
if __name__=='__main__':
	app.run()