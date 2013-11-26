import time
from time import gmtime, strftime
import MySQLdb as mdb
import datetime
import requests
import json
import hashlib
import calendar
from BeautifulSoup import BeautifulSoup

Api_Key= "6N2eThpp"
Api_Secret= "vYEMPVao"
slideshow_id= ['27501589','26992327','23200252','21227585','17723995','16738477','2368684','2368487','2368123','2367965','2366795','2366794','2366793','2366790','2367965']
ts = str(calendar.timegm(time.gmtime()))
username='intuitquickbase'
password='machoman33'
Timestamp=strftime("%Y-%m-%d %H:%M:%S", gmtime())

def getSignature(ts):
	return hashlib.sha1(str(Api_Secret)+str(ts)).hexdigest()

for item in slideshow_id:

	payload={'username': username,
		 'password' : password,
		 'api_key':Api_Key,
		 'format':'json',		 
		 'ts':ts,
		 'hash':getSignature(ts),	
		 'slideshow_id':item,
		 'detailed':'1',
		 'exclude_tags':'1',
		 }


	r = requests.get("https://www.slideshare.net/api/2/get_slideshow", params=payload)
	r=r.text

	y=BeautifulSoup(r)
	print "This is for slideshow id " + item
	print "Date Created " + str(y.slideshow.created.text)
	print "Title = " +str(y.slideshow.strippedtitle.text)
	print "Views = "+ str(y.slideshow.numviews.text)
	print "Downloads = "+ str(y.slideshow.numdownloads.text)
	print "Favorites = "+ str(y.slideshow.numfavorites.text)
	print "Comments = "+ str(y.slideshow.numcomments.text)
	print "Shares = "+ str(y.slideshow.sharewithcontacts.text)

	intuittest.cq2mgcdwryfy.us-west-1.rds.amazonaws.com
	con = mdb.connect('localhost', 'root', 'root', 'jenndb', 8889, '/Applications/MAMP/tmp/mysql/mysql.sock');
	# con = mdb.connect('intuittest.cq2mgcdwryfy.us-west-1.rds.amazonaws.com', 'root', 'password', 'jenndb');
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO slideshare_quickbase(Timestamp,Presentation, Views, Downloads, Favorites, Comments) VALUES('" + Timestamp+ "','"
																													  + str(y.slideshow.created.text)+ "', '"	
																													  + str(y.slideshow.strippedtitle.text)+ "', '"
																												      + str(y.slideshow.numviews.text) + "', '"
																												      + str(y.slideshow.numdownloads.text) + "', '" 
																												      + str(y.slideshow.numfavorites.text) + "', '" 
																												      + str(y.slideshow.numcomments.text) + "')")
		#the small quotation marks is just a string. The variables have on quotation marks on them. everything in the big quotation marks are string. 
		#The first part of the string is from the <Insert statement to Values('> + <numfollowers is not a string> + <string 2: ','> + <Timestamp> + <string3: ')>
		#print itemlist[0].attributes['NumDownloads'].value
# Views = xmldoc.getElementsByTagName('NumViews')
# print downloads.value 



