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

r = requests.get("https://api.linkedin.com/v1/companies/89760/company-statistics:(status-update-statistics)", params=payload)

#print r.text

data = json.loads(r.text)

# pprint(data)
#numfollowers=strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + str(data["numFollowers"])
#month=str(data["followStatistics"]["countsByMonth"]["values"]["date"]["month"])
# followers=data["followStatistics"]["countsByMonth"]["values"]
period=data["statusUpdateStatistics"]["viewsByMonth"]["values"]
# print followers

# for item in followers:
# 	print item['totalCount']
# for item in period:
#  	print item['date']['month']
# for item in period:
#  	print item['date']['year']
count=0
for item in period:
	count+=1
	clicks = 0
	if "clicks" in item:
		clicks = item['clicks']
	comments = 0
	if "comments" in item:
		comments= item['comments']
	month = item['date']['month']
	year = item['date']['year']
 	dt = datetime.datetime(year=year, month=month, day=1)
 	print dt
 	engagement = 0 # default
 	if "engagement" in item:
 		engagement = item['engagement']
 	impressions = 0
 	if "impressions" in item:
 		impressions = item['impressions']
 	likes = 0
 	if "likes" in item:
 		likes = item['likes']
 	shares = 0
 	if "shares" in item:
 		shares = item['shares']

 	
 	# insert mysql here
	
#Timestamp=strftime("%Y-%m-%d %H:%M:%S", gmtime())
# dt = datetime.datetime(year=2012, month=2, day=1)
# print dt
# print month
# print year
# print newfollowers
# print Totfollowers
# print Timestamp
# print "FROM HERE IS JENN"

# print data["_count"]

# print data["values"][0]
# print "\n"
# print data["values"][1]
# print "\n"
# print data["values"][3]
# print "\n"
# print data["values"][4]
	con = mdb.connect('intuittest.cq2mgcdwryfy.us-west-1.rds.amazonaws.com', 'root', 'password', 'jenndb');
	with con:
 		cur = con.cursor()
# 	#cur.execute("INSERT INTO flash(Total_IOP_Signups, Total_IOP_Billed) VALUES('" + str(a[i]) + "', '" + str(b[i]) + "')" )
 	#cur.execute("INSERT INTO DemandForce(Num_Followers, Timestamp) VALUES('" + followers + "', '" + dt + "')" )
 		#cur.execute("UPDATE DemandForce SET clicks=%s, comments=%s, engagement=%s, impressions=%s, likes=%s, shares=%s VALUES('" + str(clicks) + "', '" + str(comments) +"', '" + str(engagement) +"', '"+str(impressions)+"', '"+str(likes)+"', '"+str(shares) +"') WHERE id='" + str(count)+ "')")
 		print "eg:"
 		print engagement
 		cur.execute ("""
   				UPDATE DemandForce
   				SET clicks=%s, comments=%s, engagement=%s, impressions=%s, likes=%s, shares=%s
   				WHERE id=%s
				""", (clicks, comments, engagement, impressions, likes, shares, count))
# 	sql = "INSERT INTO API(LinkedINGroups_Num_Followers, Timestamp) VALUES('" + numfollowers + "', '" + Timestamp + "')"
# 	print sql
# 	cur.execute(sql)

print "Done"