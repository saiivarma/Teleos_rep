import MySQLdb

conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="time_productivity")

cur=conn.cursor()

uname='varma'

passwd='123456'
#returns true if the login is successful
def login(uname,passwd):
	cur.execute("select password from login where username=%s",(uname,))
	conn.commit()
	for row in cur.fetchall():
		print(row[0])
		if row[0]==passwd:
			return True
#To register into the web app
def signup(eid,uname,passwd):
	cur.execute("insert into login values(%s,%s,%s)",(eid,uname,passwd,))
	conn.commit()
#To obtain the day-wise data for the week wise report
def get_week_time(eid,date):
	time = cur.execute("select time from weekly where eid=%s and date=%s",(eid,date,))
	
	conn.commit()
	return time
def get_today_time(eid):
	time=cur.execute("select time from daily where eid=%s",(eid,))
	return time
def get_today_clicks(eid,programs):
	clicks=cur.execute("select clicks from daily where eid=%s and programs=%s",(eid,programs,))
	return clicks