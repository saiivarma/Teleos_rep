from flask import Flask,session
from flask import url_for,flash
from flask import render_template
from operator import itemgetter
from datetime import datetime
from flask import request,redirect
import threading,os
from threading import Timer
import psutil
import subprocess
from subprocess import call
import model_data
import db as database
import db_keylog
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
		session['id']=Eid # Use this Eid according the requirement in the below routes using session.get('id') method
		top=session.get('top')
#redirect to different dashboard based on the eid of the employee
		if database.login(username,password):
			if int(Eid) in range(1,100):
				return redirect(url_for('manager'))
			elif int(Eid) in range(100,500):
				return redirect(url_for('teamleader'))
			else:
				return redirect(url_for('emp'))
		
	path="keylog.py"
	def thread_second():
		call(['python',path])
	processThread= threading.Thread(target=thread_second)
	processThread.start()	
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
# All the data related to the manager 	
@app.route('/manager')
def manager():
	username=session.get('user')
	return render_template('manager.html',username=username)
#All the data related to the employee
@app.route('/emp')
def emp():
	username=session.get('user')
	eid=session.get('id')
	v1=v2=v3=v4=v5=v6=v7=0
	v1=database.get_week_time(eid,'2019-03-05')*80
	v2=database.get_week_time(eid,'2019-03-04')*10
	v3=database.get_week_time(eid,'2019-03-03')*90
	v4=database.get_week_time(eid,'2019-03-02')*78
	v5=database.get_week_time(eid,'2019-03-01')*23
	v6=database.get_week_time(eid,'2019-03-03')*32
	v7=database.get_week_time(eid,'2019-03-04')*42
	v8=database.get_today_clicks(eid,'coding')*100
	v9=database.get_today_clicks(eid,'web')*100
	v10=database.get_today_time(eid)
	v11=database.get_today_time(eid)
	v12=100-v8+v9
	v13=database.get_prog_time(eid,'coding')*100
	v14=database.get_prog_time(eid,'web')*100
	psutil
	x=datetime.today()
	y=x.replace(day=x.day+1, hour=0, minute=1, second=0, microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	time_var=0
	def cpu_time():
		global time_var
		time_var=psutil.cpu_times_percent(interval=30)
		print(time_var)

	t= Timer(secs,cpu_time)

	return render_template('emp.html',username=username,val1=v13,val2=v14,mon=v1,tue=v2,wed=v3,thu=v4,fri=v5,sat=v6,sun=v7,click=v8,click2=v9,time1=v8,time2=v9,click3=v12)
#All the data related to the teamleader
@app.route('/teamleader')
def teamleader():
	username=session.get('user')
	return render_template('teamleader.html',username=username)
#All the data related to the leader board
@app.route('/leaderboard')
def leaderboard():
	username=session.get('user')
	id=session.get('id')
	if int(id) in range(1,100):
		page='manager'
		page2='manager'
	elif int(id) in range(101,500):
		page='teamleader'
		page2='teamleader'

	else:
		page='emp'
		page2='svg'

	return render_template('leaderboard.html',username=username,page=url_for(page),page2=url_for(page2))
#All the data related to the efficiency meter
@app.route('/svg')
def svg():
	username=session.get('user')
	id=session.get('id')
	if int(id) in range(1,100):
		page='manager'
		
	elif int(id) in range(101,500):
		page='teamleader'
		
	else:
		page='emp'
	list_prog=[0]*4
	overall=db_keylog.get_overall(int(id))
	sorted(overall, key=itemgetter(3))
	sum1=0
	for i in range(0,len(overall)):
		list_prog[i]=overall[i][4]
		sum1+=list_prog[i]
	x=model_data.model(int(id))		
	return render_template('svg.html',username=username,page=url_for(page),val=x*100,val1=round(list_prog[0]*100/sum1,2),val2=round(list_prog[1]*100/sum1,2),val3=round(list_prog[2]*100/sum1,2),val4=round(list_prog[3]*100/sum1,2))

#Method to run the Flask App
if __name__=='__main__':
	app.secret_key='some secret key'
	app.config['SESSION_TYPE']='filesystem'
	app.run()