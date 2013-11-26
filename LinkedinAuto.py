import MySQLdb as mdb
import requests
import json
from pprint import pprint
from time import gmtime, strftime

#https://api.linkedin.com/v1/companies/1666:(id,num-followers)
#?oauth2_access_token=AQXqWy92Jtz6qa-qE5DazfVCNBHOI_4uy9abBqUuyagITGt1xFBTQg3BHkpUsXdO2s-3zmAXVj1XjuBzAEm-3Nudyyw-R9n4g8vOOza5evu_CMBzczb__-P3OGCDU2EpjHXkT4fClkiTle__UBEH5oL6FVfoG-pW2cpC81M_FNImZtNWCqs
payload={
		 'format':'json',		 
		 'oauth2_access_token':'AQXqWy92Jtz6qa-qE5DazfVCNBHOI_4uy9abBqUuyagITGt1xFBTQg3BHkpUsXdO2s-3zmAXVj1XjuBzAEm-3Nudyyw-R9n4g8vOOza5evu_CMBzczb__-P3OGCDU2EpjHXkT4fClkiTle__UBEH5oL6FVfoG-pW2cpC81M_FNImZtNWCqs',		 
		 }

r = requests.get("https://api.linkedin.com/v1/companies/1666:(id,num-followers)", params=payload)

#print r.text

data = json.loads(r.text)

#pprint(data)
#numfollowers=strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + str(data["numFollowers"])
numfollowers=str(data["numFollowers"])
Timestamp=strftime("%Y-%m-%d %H:%M:%S", gmtime())
print numfollowers
print Timestamp
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
	#cur.execute("INSERT INTO flash(Total_IOP_Signups, Total_IOP_Billed) VALUES('" + str(a[i]) + "', '" + str(b[i]) + "')" )
	#cur.execute("INSERT INTO API(LinkedINGroups_Num_Followers, Timestamp) VALUES('" + numfollowers + "', '" + Timestamp + "')" )
			#The first part of the string is from the <Insert statement to Values('> + <numfollowers is not a string> + <string 2: ','> + <Timestamp> + <string3: ')>																			
	sql = "INSERT INTO API(LinkedinCompany_Num_Followers, Timestamp) VALUES('" + numfollowers + "', '" + Timestamp + "')"
	print sql
	cur.execute(sql)

print "Done"