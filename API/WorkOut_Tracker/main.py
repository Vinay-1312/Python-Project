# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:56:48 2022

@author: DELL
"""
from datetime import date
from datetime import datetime
import json
import requests 
import os


#sheety auth token


query = input("What exercise did you do today?:")

#app id of nutritionix
Api_id = os.environ["Api_id"]

#auth token for nutrituonix 
API_Auth = os.environ["API_Auth"]
headers = {
    "x-app-id":Api_id,
    "x-app-key":API_Auth,
    "Content-Type": "application/json"
    }


auth_token_shetty = os.environ["auth_token_shetty "]
headers_1 = {
    "Authorization":auth_token_shetty
    }

body = {
        "query":query,
        "gender":"male"
        }

today = date.today()
dt = today.strftime("%d/%m/%Y")
now = datetime.now()
#H:M:S
time = now.strftime("%H:%M:%S")

try:
    response = requests.post(url ="https://trackapi.nutritionix.com/v2/natural/exercise",json = body,headers = headers)
    #output received from track api about the exercise
    received_data = response.json()
    for i in received_data['exercises']:
        data = {
            "workout":
            {
            "date" : dt,
            "time" : time,
            "exercise" : i["name"].title(),
            "duration" :i["duration_min"],
            "calories" : i["nf_calories"]
            }
        } 
        response = requests.post(url = "https://api.sheety.co/cc2b4ad76bd17ddaba4e8f529d301745/myWorkouts/workouts", json =data, headers = headers_1  )
  

    
except Exception as e:
    print(e)