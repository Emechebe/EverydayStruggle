# Since I will be getting data from the web, I need  urllib
#import urllib.request, urllib.parse, urllib.error
import requests
import json
import ssl
import sqlite3
import aniso8601
import datetime
from datetime import timedelta

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#We build the database we want to dump the data into
conn = sqlite3.connect('EveryDayStruggle.sqlite')
# Create the database filehandle
cur = conn.cursor()

# This prompts for the url
url = "https://www.googleapis.com/youtube/v3/search"
url1='https://www.googleapis.com/youtube/v3/playlists'

api_key ='AIzaSyAjKHMECCdtEqhz6ORJRtbqRVZVJWPCHwE'

lastdate  = "2017-12-21T00:00:00Z"
startdate ="2017-04-01T00:00:00Z"

for i in xrange(10):
   print (startdate,lastdate)
   parameters = {"part": "snippet", "maxResults": 50,"type": "video", "order": "date","pageToken": "","publishedAfter": startdate,"publishedBefore": lastdate,
   "q": "EVERYDAY STRUGGLE | Joe Budden & Akademiks",'channelId':'UCpFHkjOa7ia6bH5_6cDsDXg',"key": api_key,}

   parameters1 = {"part": "snippet", "maxResults": 50,"type": "video", "order": "date","pageToken": "","q": "EVERYDAY STRUGGLE | Joe Budden & Akademiks",'channelId':'UCpFHkjOa7ia6bH5_6cDsDXg',"key": api_key,}

   parameter = {"part": "snippet", "maxResults": 1,"channelTitle": "Complex News", "order": "date","pageToken": "","publishedAfter": "2017-04-01T00:00:00Z",
   "q": "Joe Budden & DJ Akademiks ",
   "key": api_key, "type": "video",}

   page = requests.request(method="get", url=url, params=parameters)
   j_results = json.loads(page.text)
   if len(j_results['items']) == 0:
          break 
   id_video = []
   title_video = []
   Date_video = []
   count = 0
   for j in j_results['items']:
	   id_video.append(j['id']['videoId'])
	   title_video.append(j['snippet']['title'])
	   Date_video.append(j['snippet']['publishedAt'])
	   count = count + 1
	   if count == len(title_video):
		   lastdate = j['snippet']['publishedAt']
   date = lastdate


   # Now we have the id's , get statistics for every id
   url_vid = "https://www.googleapis.com/youtube/v3/videos"
   Statistics = []
   for k in id_video:
       parameters_stat = {"part": "statistics","id": k,"key": api_key,}
       page = requests.request(method="get", url=url_vid, params=parameters_stat)
       j_results = json.loads(page.text)
       Statistics.append(j_results)
   print len(Statistics)

   # I also wanted to get duration of the video

   Duration = []
   for d in id_video:
	   parameters_duration = {"part": "contentDetails",'id':d,'key':api_key,}
	   page = requests.request(method="get", url=url_vid, params=parameters_duration)
	   d_results = json.loads(page.text)
	   Duration.append(d_results)
   # Put together title of podcast and stats of podcasts
   #print (Duration)
   myList=[]
   Data =[]
   for l in range(len(title_video)):
	   title = title_video[l]
	   viewCount = Statistics[l]['items'][0]['statistics']['viewCount']
	   commentCount = Statistics[l]['items'][0]['statistics']['commentCount']
	   dislikeCount = Statistics[l]['items'][0]['statistics']['dislikeCount']
	   favCount = Statistics[l]['items'][0]['statistics']['favoriteCount']
	   Date = Date_video[l]
	   Video_length = Duration[l]['items'][0]['contentDetails']['duration']
	   parsed_Video_length = aniso8601.parse_duration(Video_length)

	   #print parsed_Video_length
	   cur.execute('''CREATE TABLE IF NOT EXISTS EveryDayStruggle (Date_published DATE,title VARCHAR,viewCount Number,commentCount Number,dislikeCount Number, favCount Number,Video_length Number)''')
	   cur.execute('''INSERT INTO EveryDayStruggle (Date_published,title,viewCount,commentCount,dislikeCount,favCount,Video_length) VALUES ( ?, ?,?,?,?,?,? )''',(Date,title,viewCount,commentCount,dislikeCount,favCount,Video_length))
	   conn.commit()