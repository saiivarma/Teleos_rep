from flask import Flask,session
from flask import url_for,flash
from flask import render_template
from flask import request,redirect
import db as database
import MySQLdb
app= Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
@app.route('/login', methods=['GET','POST'])
def login():
#Login page redirects
	if request.method == 'POST':
		Eid= request.form['empid']
		username= request.form['username']
		password= request.form['password']
		session['user']=username
		top=session.get('top')
#redirect to different dashboard based on the eid of the employee
		if database.login(username,password):
			if int(Eid) in range(1,100):
				return render_template('manager.html',name=top)
			elif int(Eid) in range(100,500):
				return render_template('teamleader.html',name=top)
			else:
				return render_template('emp.html')
		
			
	return render_template('login.html')
@app.route('/form_validation',methods=['GET','POST'])
def form_validation(): 
#send data from signup form to the database 
	if request.method=='POST':
		error=None
		eid=request.form['empid']
		username=request.form['username']
		password=request.form['password']
		if not username:
			error = 'Username is required'
		elif not password:
			error ='Password is required'
		if error is None:	
			database.signup(eid,username,password)
			
			return redirect(url_for('login'))
		flash('user registration sucessfull')
		flash(error)
	return render_template('form_validation.html')
	
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))
@app.route('/emp')
def emp():
	name=database.best()
	session['top']=name
@app.route('/leaderboard')
def leaderboard():
	username=session.get('user')
	return render_template('leaderboard.html',username=username)


if __name__=='__main__':
	app.secret_key='some secret key'
	app.config['SESSION_TYPE']='filesystem'
	app.run()