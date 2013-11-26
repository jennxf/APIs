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

r = requests.get("https://api.linkedin.com/v1/companies/89760/company-statistics:(follow-statistics:(countsByMonth:(totalCount)))", params=payload)

#print r.text

data = json.loads(r.text)

# pprint(data)
#numfollowers=strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + str(data["numFollowers"])
#month=str(data["followStatistics"]["countsByMonth"]["values"]["date"]["month"])
followers=data["followStatistics"]["countsByMonth"]["values"]

i=0
for item in followers:
	print item['totalCount']
	print i
	i+=1