# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:59:55 2022

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:19:46 2022

@author: DELL
"""

import requests

from twilio.rest import Client

Api_Key = "2337b8189b7aac62bc3451453142b965"

response = requests.get(url= "http://api.openweathermap.org/data/2.5/onecall?lat=18&lon=73&exclude=current,minutely,daily&appid=" + Api_Key)
response.raise_for_status()
weather_data = response.json()
timewise_weather = {"7AM":"","8AM":"","9AM":"","10AM":"","11AM":"","12PM":"","1PM":"","2PM":"","3PM":"","4PM":"","5PM":"","6PM":"","7PM":""}
clear_time = dict()
rain_time = dict()

for i,j in zip(weather_data['hourly'],timewise_weather.keys()):
    ID = str(i['weather'][0]['id'])
    if(ID.startswith('2')):
        rain_time[j] = "Thunderstorm"
    elif (ID.startswith('3')):
        rain_time[j]= "Drizzle"
    elif (ID.startswith('5')):
        rain_time[j] = "Rain"
    elif (ID.startswith('8')):
        clear_time[j] = "Clear"
        
Message = ""

if (rain_time == {}):
    Message = "Don't Worry the weather is clear thorughout day! "
    
else:
    Message = "There is going to be rain at "
    for key in rain_time:
     Message += key + ","

Message = Message.rstrip(",")

#sending message
account_sid = 'ACa0c42781c8e3d2474fdc7a234689bb39' 
auth_token = '1c3545dd0f6877ab244f8cb34c694518' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG0076ddafb32bc492066a96d7e2e957ac',   
                              body = Message,
                              to='+919158695603' 
                          ) 
 
