from flask import Flask
from flask import url_for
from flask import render_template
from flask import request,redirect
import MySQLdb
app= Flask(__name__)
@app.route('/')
def hello():
	redirect(url_for(login))

@app.route('/login',methods=['POST','GET'])
def login():
	error=None
	if request.method=='POST':
		if valid_login(request.form['eid'],request.form['username'],request.form['password']):
			if request.form['eid'] in range(1,100):
				return render_template('manager.html')
			elif request.form['eid'] in range(101,500):
				return render_template('teamleader.html')
			else:
				return render_template('emp.html')

		else:
			error = 'Invalid username/password'
			flash(error)
	return render_template('login.html',error=error)
@app.route('/form_validation')
def create():
	if request.method=='POST':
		if valid_login():
			return redirect(url_for('login'))
if __name__=='__main__':
	app.run()