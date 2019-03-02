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
def get_week_time(eid,date):
	cur.execute("select clicks,time,programs,efficiency from weekly where eid=%s and date=%s",(eid,date,))
	for row in cur.fetchall():
		clicks,time,program,efficiency=row[0],row[1],row[2],row[3]
	conn.commit()
	return clicks,time,program,efficiency
#adding the daily data to the weekly table
def add_week_time(eid,date,clicks,time,programs,efficiency):
	cur.execute("insert into weekly values(%s,%s,%s,%s,%s,%s)",(eid,date,clicks,time,programs,efficiency))
	conn.commit()
#adding today details
def add_today_time(eid,clicks,time,programs,efficiency):
	cur.execute("insert into daily values(%s,%s,%s,%s,%s)",(eid,clicks,time,programs,efficiency,))
	conn.commit()
#get today data by the end of the day such that the retrieved data is summed up and updated to the weekly	
def get_today_time(eid):
	time = []
	clicks = []
	programs = []
	efficiency = []
	cur.execute("select * from daily where eid=%s",(eid,))
	for row in cur.fetchall():
		print(row)
		time.append(row[2])
		clicks.append(row[1])
		programs.append(row[3])
		efficiency.append(row[4])
	return time,clicks,programs,efficiency

#adding overall employee details for the first time or the program is not available previously
def add_overall_first(eid,time,clicks,programs,efficiency):
	cur.execute("insert into overall values(%s,%s,%s,%s,%s)",(eid,time,clicks,programs,efficiency,))
	conn.commit()
#adding the overall data to the table.
'''Before adding fetch the overall data using get_overall()
		and compare it with the output of the algorithm and then use add_overall_first		'''
def add_overall(eid,time,employee,programs,efficiency):
	cur.execute("update overall set time=%s,clicks=%s,programs=%s,efficiency=%s where eid=%s",(time,clicks,programs,efficiency,eid,))
#get the whole data of an employee
def get_overall(eid):
	prog_list = []
	cur.execute("select * from overall where eid=%s",(eid,))
	for row in cur.fetchall():
		prog_list.append(row)
	conn.commit()
	return prog_list
#testing the queries

#inserting the data
add_week_time('123','765234','234',"python",12,"2019-01-31")
add_week_time('123','7654','214',"web",72,"2019-01-31")
add_today_time('123','543','700',"pyhton",34)
add_overall_first('123','543','700',"pyhton",64)

# reading the data
print(get_overall("123"))
print(".................")
print(get_today_time("123"))
print(".................")
print(get_week_time("123","2019-01-31"))