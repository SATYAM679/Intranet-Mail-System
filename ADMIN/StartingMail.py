#!C:\Python27\python.exe
import exceptions
import urllib
import cgi, cgitb
import MySQLdb
import base64
import sys
cgitb . enable()
form = cgi.FieldStorage() 
try:
        sid = base64.b64decode(form.getvalue('sid'))
        db = MySQLdb.connect("localhost","root","system","IMS" )
        cursor = db.cursor()
	print "Content-type:text/html"
	print """
	<html>
	<head>"""
	a="select user_id from session where session_id='"+str(sid)+"'"
	v=cursor.execute(a)
	row=cursor.fetchall()
	if(v==0):
		print "<meta http-equiv='refresh' content='0;url=../index.py' />"
        for row in cursor:
                sname=row[0]
                        
        n=cursor.execute("select * from mailcon where sname=('"+sname+"') or rname=('"+sname+"')")

        print "Content-type:text/html"
        print """
        <html>
                <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>Dasboard</title>

                    <!-- BOOTSTRAP STYLES-->
                    <link href="assets/css/bootstrap.css" rel="stylesheet" />
                    <!-- FONTAWESOME STYLES-->
                    <link href="assets/css/font-awesome.css" rel="stylesheet" />
                    <!-- PAGE LEVEL STYLES -->
                    <link href="assets/css/prettyPhoto.css" rel="stylesheet" />
                    <!--CUSTOM BASIC STYLES-->
                    <link href="assets/css/basic.css" rel="stylesheet" />
                    <!--CUSTOM MAIN STYLES-->
                    <link href="assets/css/custom.css" rel="stylesheet" />
                    <!-- GOOGLE FONTS-->
                    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
                    
                       <style>
                    .button {
                        /* Green */
                        border: none;
                        color: white;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                            }

                    .button1 {
                    background-color:  #f0b27a;
;
                 
                    padding: 110px 110px;}
                    
                    .button2 {
                    background-color: #af7ac5;
                    padding: 100px 100px;}

                    .button3 {
                    background-color: #FF1245;
                    padding: 100px 100px;}

                    .button4 {
                    background-color: #00FFFF;
                    padding: 100px 100px;}

                    .button5 {
                    background-color: #FF00FF;
                    padding: 110px 110px;}

                    .button6 {
                    background-color: #FF00FF;
                    padding: 110px 110px;}

                    .button7 {
                    background-color: #800124;
                    padding: 110px 110px;}

                    .button8 {
                    background-color: #854610;
                    padding: 100px 100px;}

                    .button9 {
                    background-color: #325689;
                    padding: 100px 100px;}

                    .button1:hover {
                    background-color: #008CBA;
                    color: white;}
                    
                </style>
                </head>
                <body>
                    <div id="wrapper">
                        <nav class="navbar navbar-default navbar-cls-top " role="navigation" style="margin-bottom: 0">
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">
                                    <span class="sr-only">Toggle navigation</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                                <a class="navbar-brand" >Intranet Mail System</a>
                            </div>

                            <div class="header-right">
                """
        
        print """

                            </div>
                        </nav>
                        <!-- /. NAV TOP  -->
                        <nav class="navbar-default navbar-side" role="navigation">
                            <div class="sidebar-collapse">
                                <ul class="nav" id="main-menu">
                                    <li>
                                        <div class="user-img-div">
                                            <img src="user.png" class="img-thumbnail" />
                <div class="inner-text">"""
        print sname
        print """  
                                      
                                        </div>

                                    </li>


                                    <li>"""
        print "<a class='active-menu' href='index_admin.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-ge'></i>Dashboard</a>"
        print "</li><li>"       
        field="inbox"
        
        print "<a href='inbox.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Inbox</a>"
        print "</li><li>"
        print "<a href='Compose.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Compose</a>"
        print "</li><li>"
        print "<a href='sentmail.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Sent Mail</a>"
        print "</li><li>"
        print "<a href='Label.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-archive'></i>Label</a>"
        print "</li><li>"
        print "<a href='Group.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-group'></i>Group</a>"
        print "<a href='draft.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Draft</a>"
	print "</li><li>"
        print "<a href='dmail.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-recycle'></i>Recycle Now!</a>"
        print "</li><li>" 
        
                            
        print "<a href='logout.py?sid="+base64.b64encode(str(sid))+"&num="+base64.b64encode(str(1))+"'><i class='fa fa-sign-out'></i>Logout</a>"
        print """                    
       </li>
            </div>
                        </nav>
                <!-- /. NAV SIDE  -->
                <div id="page-wrapper">
                    <div id="page-inner">
                        <div class="row">
                            <div class="col-md-12">
                                <h1 class="page-head-line">welcome to ADMIN.</h1>
                                <h1 class="page-subhead-line">DASHBOARD </h1>
                                    </div>
                        </div>
                        
                           <!-- /. ROW  -->
                        <div id="port-folio">
                                      <div class="row " >
                             
                        <div class="col-md-4 ">"""
	print "<a href='inbox.py?sid="+base64.b64encode(str(sid))+"' class='button button1' >Inbox</a>"
	print "</div>"
	print "<div class='col-md-4'>"
	print "<a href='compose.py?sid="+base64.b64encode(str(sid))+"' class='button button2' > Compose Mail</a>"
	print """</div>"""
	print "<div class='col-md-4 '>"
	print "<a href='Sentmail.py?sid="+base64.b64encode(str(sid))+"' class='button button3' >Sent mail</a>"
	print "</div>"
	
	print "<div class='col-md-4 '>"
	print "<a href='Label.py?sid="+base64.b64encode(str(sid))+"' class='button button6' >Label </a>"
	print "</div>"
	print "<div class='col-md-4 '>"
	print "<a href='ForwardMail.py?sid="+base64.b64encode(str(sid))+"' class='button button4' >Forward Mail</a>"
	print"</div>"
        print "<div class='col-md-4 '>"
	print "<a href='Group.py?sid="+base64.b64encode(str(sid))+"' class='button button5 >GROUP</a>"
	print "</div>"	
        
	print """
                            
                    
                    
                            
                                
                                    
                                

                            </div>
                                </div>
                                              
                             </div></div>
                    <!-- /. WRAPPER  -->
                    <div id="footer-sec">
                        &copy; 2016-17 <b>I</b>NTRANET <b>M</b>AIL <b>S</b>ystem | Design By : unKnOwN$</a>
                    </div>
                    <!-- /. FOOTER  -->
                    <!-- SCRIPTS -AT THE BOTOM TO REDUCE THE LOAD TIME-->
                    <!-- JQUERY SCRIPTS -->
                    <script src="assets/js/jquery-1.10.2.js"></script>
                    <!-- BOOTSTRAP SCRIPTS -->
                    <script src="assets/js/bootstrap.js"></script>
                     <!-- PAGE LEVEL SCRIPTS -->
                    <script src="assets/js/jquery.prettyPhoto.js"></script>
                    <script src="assets/js/jquery.mixitup.min.js"></script>
                    <!-- METISMENU SCRIPTS -->
                    <script src="assets/js/jquery.metisMenu.js"></script>
                    <!-- CUSTOM SCRIPTS -->
                    <script src="assets/js/custom.js"></script>
                     <!-- CUSTOM Gallery Call SCRIPTS -->
                    <script src="assets/js/galleryCustom.js"></script>
                </body>
                </html>

                """
except Exception as e:
        print "Content-type:text/html\r\n\r\n"
        print """<html><head><meta http-equiv='refresh' content='0;url=../index.py' /></head><body></body></html>"""

