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
def signup(uname,eid,passwd):
	cur.execute("insert into login values(%s,%s,%s)",(uname,eid,passwd,))
	conn.commit()
#To obtain the day-wise data for the week wise report
