import MySQLdb
import datetime
import random

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
def get_week(eid):
	week_list=[]
	cur.execute("select * from weekly where eid=%s",(eid,))
	for row in cur.fetchall():
		week_list.append(list(row))
	conn.commit()
	return week_list
#adding the daily data to the weekly table
def add_week_time(eid,time,clicks,programs,efficiency,date):
	cur.execute("insert into weekly values(%s,%s,%s,%s,%s,%s)",(eid,time,clicks,programs,efficiency,date))
	conn.commit()
#adding today details
def add_today(eid,time,clicks,programs,efficiency,category):
	cur.execute("insert into daily values(%s,%s,%s,%s,%s,%s)",(eid,time,clicks,programs,efficiency,category,))
	conn.commit()

def update_today(eid,time,clicks,programs,efficiency):
	cur.execute("update daily set time=%s,clicks=%s,efficiency=%s where eid=%s and programs=%s",(time,clicks,efficiency,eid,programs,))
	conn.commit()

#get today data by the end of the day such that the retrieved data is summed up and updated to the weekly	
def get_today(eid):
	today_list= []
	cur.execute("select * from daily where eid=%s",(eid,))
	for row in cur.fetchall():
		today_list.append(list(row))
		
	return today_list

#adding overall employee details for the first time or the program is not available previously
def add_overall(eid,time,clicks,programs,efficiency):
	#print(eid,time,clicks,programs,efficiency)
	cur.execute("insert into overall values(%s,%s,%s,%s,%s)",(eid,time,clicks,programs,efficiency,))
	conn.commit()
#adding the overall data to the table.
'''Before adding fetch the overall data using get_overall()
		and compare it with the output of the algorithm and then use add_overall_first		'''
def update_overall(eid,time,clicks,programs,efficiency):
	cur.execute("update overall set time=%s,clicks=%s,efficiency=%s where eid=%s and programs=%s",(time,clicks,efficiency,eid,programs,))
	conn.commit()
#get the whole data of an employee
def get_overall(eid):
	prog_list = []
	cur.execute("select * from overall where eid=%s",(eid,))
	for row in cur.fetchall():
		prog_list.append(list(row))
	conn.commit()
	return prog_list


#######
####### define model
def efficiency(oplist, ):#### example
	eff = 1
	for i in oplist:
		i.append(eff)
	return oplist

def add_today_to_week(prev_date, eid):
	#print(datetime.datetime.now().date() != prev_date)
	#print(datetime.datetime.now().date(), prev_date)
	if datetime.datetime.now().date() != prev_date:
	#	print("lakshfdlahfoadkajllf")
		for i in get_today(eid):
			print('today to week')
			add_week_time(i[0], i[1], i[2], i[5], i[4], prev_date)
		#prev_date = datetime.datetime.now().date()
		cur.execute("delete from daily")
		conn.commit()
	#return prev_date

def clear_every_week(prev_date,eid):

	if datetime.datetime.now().date().weekday() == 0 and prev_date < datetime.datetime.now().date(): # 0 is Monday
		#print('week',(prev_date),datetime.datetime.now().date())
		prev_date = datetime.datetime.now().date()
		cur.execute("delete from weekly where eid=%s",(eid,))
		conn.commit()
	return prev_date

def merge_content(eid,val):
	if val == 0:
		dblist=get_overall(eid)
	elif val == 1:
		dblist = get_today(eid)
	elif val == 2:
		dblist = get_week(eid)

	#print('merge_content')

	count = 1
	modi_list=[]
	if dblist != []:
		modi_list=[dblist[0]]
		dblist=dblist[1:]
	
	for i in dblist:
		for j in modi_list:
			if i[3] == j[3]:
				j[1]+=round(i[1],3)
				j[2]+=i[2]
				j[4]+=round(i[4],3)
				count = 0
		if count ==1:
			modi_list.append(i)
	
	if val == 0:
		cur.execute('delete from overall where eid=%s',(eid,))
		for i in modi_list:
			add_overall(i[0],i[1],i[2],i[3],i[4])
	elif val == 1:
		cur.execute('delete from daily where eid=%s',(eid,))
		for i in modi_list:
			add_today(i[0],i[1],i[2],i[3],i[4],i[5])
	elif val == 2:
		cur.execute('delete from weekly where eid=%s',(eid,))
		for i in modi_list:
			add_week_time(i[0],i[1],i[2],i[3],i[4],i[5])
	
	conn.commit()
	


			
def update(dblist,oplist,prev_date):
	#print(dblist)
	dblist =list(dblist)
	oplist = list(oplist)
	eid_list =[]
	oplist = efficiency(oplist)
	#print("update")
	for i in oplist:
		i[1] =round((i[1]),3)
		i[2] =int(i[2])
		i[5] =round((i[5]),3)

		#print(i)
		#for j in dblist:
		
#		print("new entry")
		add_overall(i[0], i[1], i[2], i[3], i[5])
		add_today(i[0], i[1], i[2], i[4], i[5], i[3])
		#print(i)
	for i in dblist:
		if i[0] not in eid_list:
			eid_list.append(i[0])
	print(eid_list)
	for val in [0,1,2]:
		for i in eid_list:
			merge_content(i,val)
	
	for i in eid_list:
		add_today_to_week(prev_date,i) 

		prev_date = clear_every_week(prev_date,i)	##emove after every week i.e. after every sunday

	return dblist



#add_today_to_week(datetime.date(2019, 3, 2), 123)
#add_today_to_week(datetime.date(2019, 3, 2),123)