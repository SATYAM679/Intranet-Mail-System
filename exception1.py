#!C:\Python27\python.exe

# Import modules for CGI handling 
import random



import cgi, cgitb
cgitb . enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
uname = form.getvalue('uname')
password = form.getvalue('pass')


#first_name = "Hello"
#last_name  = "World"
if(uname is None):
	uname="NULL"
import MySQLdb
#import sys

try:
	db = MySQLdb.connect("localhost","root","system","IMS" )
	cursor = db.cursor()
	#cursor.execute("select * from login",(uname,password))
	a="select * from user where user_id=('"+uname+"') and password=('"+password+"')"
	v=cursor.execute("select * from user where user_id=%s && password=%s",(uname,password))

	#v="""cursor.execute("select * from login where user_name=%s && password=%s",(uname,password))"""
	row=cursor.fetchall()
	#\cursor.execute(v)
	print "Content-type:text/html\r\n\r\n"
	print "<html>"
	print "<head>"
	print "<title>login</title>"
	print "</head>"
	print "<body>"
	#v=10	
	if(v==1):
		for row in cursor:
			sid=random.randrange(100000000000,999999999999)
			print "sucessful login",row[5], row[6],"<br>"
			cursor.execute("insert into session values(%s,%s)",(sid,uname))
			cursor.execute("commit")
			print sid
			print "<meta http-equiv='refresh' content='0;url=exception2.py?sid="+str(sid)+"' />"
			#print "<a href='index_admin.py?sid="+str(sid)+"'>Inbox</a>"
	else:
		print "<meta http-equiv='refresh' content='0;url=exception.py' />"


	#print """<a href="sent.html">sent mail</a> """
	#print "<input type="""""
	#print "Location: sent.html\n"
	print "</body>"
	print "</html>"

	#cursor.execute(sql)
	cursor.close()
	db.close()
	#sys.exit()
except Exception as e:
        print "Content-type:text/html\r\n\r\n"
        print """<html><head><meta http-equiv='refresh' content='0;url=exception.py' /></head><body></body></html>"""
