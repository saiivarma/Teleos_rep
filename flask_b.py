from flask import Flask
from flask import url_for,flash
from flask import render_template
from flask import request,redirect
import db as database
import MySQLdb
app= Flask(__name__)
@app.route('/login', methods=['GET','POST'])
def login():
#Login page redirects
	if request.method == 'POST':
		Eid= request.form['empid']
		username= request.form['username']
		password= request.form['password']
#redirect to different dashboard based on the eid of the employee
		if database.login(username,password):
			if int(Eid) in range(1,100):
				return render_template('manager.html')
			elif int(Eid) in range(100,500):
				return render_template('teamleader.html')
			else:
				return render_template('emp.html')
		
			
	return render_template('login.html')
@app.route('/form_validation',methods=['GET','POST'])
def form_validation(): 
#send data from signup form to the database 
	if request.method=='POST':
		eid=request.form['empid']
		username=request.form['username']
		password=request.form['password']
		database.signup(username,eid,password)
	return render_template('form_validation.html')
	
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))
if __name__=='__main__':
	app.run()