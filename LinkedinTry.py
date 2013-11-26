import oauth2 as oauth
import httplib2
import time, os, simplejson
 
# Fill the keys and secrets you retrieved after registering your app
consumer_key      =   '61wuk0s2xdf9'
consumer_secret  =   'fokUAAvfLe5gcMLp'
access_token = 'AQXqWy92Jtz6qa-qE5DazfVCNBHOI_4uy9abBqUuyagITGt1xFBTQg3BHkpUsXdO2s-3zmAXVj1XjuBzAEm-3Nudyyw-R9n4g8vOOza5evu_CMBzczb__-P3OGCDU2EpjHXkT4fClkiTle__UBEH5oL6FVfoG-pW2cpC81M_FNImZtNWCqs'
 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)
 
# Use the consumer object to initialize the client object
client = oauth.Client(consumer)
 

 
# Make call to LinkedIn to retrieve your own profile
resp,content = request("http://api.linkedin.com/v1/people/~", "GET", "")
 
# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
