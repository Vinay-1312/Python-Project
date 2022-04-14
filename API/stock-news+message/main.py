
from datetime import datetime, timedelta, date
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client
import os

Stock_api_key = os.environ.get("Stock_api_key")
pos = 1
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
#get yesterday's date
today = date.today() - timedelta(days=1)
d1 = today.strftime("%Y-%m-%d")

#get 2 days before date
today = date.today() - timedelta(days=2)
d2 = today.strftime("%Y-%m-%d")

Response = requests.get(url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+STOCK+"&apikey="+Stock_api_key)
close1 = float(Response.json()["Time Series (Daily)"][d1]['4. close'])
close2 = float(Response.json()["Time Series (Daily)"][d2]['4. close'])
diff = close1-close2
#sending message

#Twilio Account_sid
account_sid = os.environ.get("Tw_SID")


#Twlio Auth Token
auth_token = os.environ.get("Tw_Auth")

message_sid = os.environ.get("messaging_service_sid")

#Your phone number
phn_no = os.environ.get("phn_no")
#phn_no = "+919158695603"
#proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token)

if diff >0:
    pos = 1 
elif diff<0:
    pos = -1
else:
    pos = 0
per = (diff/close1) * 100
message = STOCK +": "
news_api_key = os.environ.get("News_api_key")
news = requests.get(url = "https://newsapi.org/v2/top-headlines?q="+COMPANY_NAME+"&apiKey="+news_api_key)
total_results = news.json()['totalResults']
for i in range(0,total_results):
    message =  STOCK +": "
    headline = news.json()['articles'][i]['title']+"."
    Brief = news.json()['articles'][i]['description']
    
    if (pos==1):
        message = message + "🔺" + str(round(per,2)) +"%"
    else:
        message = message + "🔻" + str(round(per,2)).replce("-","") +"%"
    message = message + "\n" + "Headline: " + headline + "\n" + "Brief: " + Brief
    
    Message = client.messages.create(
                              messaging_service_sid= message_sid,
                              body = message,
                              to=phn_no
                          )
  