import MySQLdb as mdb
import requests
import json
from pprint import pprint
from time import gmtime, strftime
import datetime

#https://api.linkedin.com/v1/companies/1666:(id,num-followers)
#?oauth2_access_token=AQXqWy92Jtz6qa-qE5DazfVCNBHOI_4uy9abBqUuyagITGt1xFBTQg3BHkpUsXdO2s-3zmAXVj1XjuBzAEm-3Nudyyw-R9n4g8vOOza5evu_CMBzczb__-P3OGCDU2EpjHXkT4fClkiTle__UBEH5oL6FVfoG-pW2cpC81M_FNImZtNWCqs
payload={
		 'format':'json',		 
		 'oauth2_access_token':'AQXqWy92Jtz6qa-qE5DazfVCNBHOI_4uy9abBqUuyagITGt1xFBTQg3BHkpUsXdO2s-3zmAXVj1XjuBzAEm-3Nudyyw-R9n4g8vOOza5evu_CMBzczb__-P3OGCDU2EpjHXkT4fClkiTle__UBEH5oL6FVfoG-pW2cpC81M_FNImZtNWCqs',		 
		 }

r = requests.get("https://api.linkedin.com/v1/companies/89760/company-statistics:(follow-statistics:(countsByMonth))", params=payload)

#print r.text

data = json.loads(r.text)

# pprint(data)
#numfollowers=strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + str(data["numFollowers"])
#month=str(data["followStatistics"]["countsByMonth"]["values"]["date"]["month"])
# followers=data["followStatistics"]["countsByMonth"]["values"]
period=data["followStatistics"]["countsByMonth"]["values"]
# print followers

# for item in followers:
# 	print item['totalCount']
# for item in period:
#  	print item['date']['month']
# for item in period:
#  	print item['date']['year']
followers_list=[]
dt_list=[]
for item in period:
	followers = item['totalCount']
	followers_list.append(followers)
 	month = item['date']['month']
 	year = item['date']['year']
 	dt = datetime.datetime(year=year, month=month, day=1)
 	dt_list.append(dt)
 	print dt
 	print followers
print "now printing the followers_list..."
print""
print followers_list
print dt_list	
print ""
print "Ok, we have successfully generated the followers_list!"

print "Now printing only the first item..."
print str(followers_list[0])
print str(dt_list[0])


# con = mdb.connect('localhost', 'root', 'root', 'jenndb', 8889, '/Applications/MAMP/tmp/mysql/mysql.sock');
con = mdb.connect('intuittest.cq2mgcdwryfy.us-west-1.rds.amazonaws.com', 'root', 'password', 'jenndb');
with con:
 	cur = con.cursor()
 	cur.execute("INSERT INTO Linkedin_DemandForce(Num_Followers, Timestamp) VALUES('" + str(followers_list[0]) + "', '" + str(dt_list[0]) +"')")

sql = "INSERT INTO DemandForce(Num_Followers, Timestamp) VALUES('" + str(followers_list[0]) + "', '" + str(dt_list[0]) + "')"
print sql

print "New Month Inserted!"