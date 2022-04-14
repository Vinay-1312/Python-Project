# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:39:10 2022

@author: DELL

    xxyz91248@gmail.com
"""
import smtplib, ssl

from datetime import datetime
import requests
import time


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "xxyz91248@gmail.com"  # Enter your address
receiver_email = "vinaysld123@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

i = 0
try:
    t =5/0
    while i < 5:
        
        message = """\
    Subject: Hi there
    
    This message is sent from Python."""
        Response = requests.get(url = "http://api.open-notify.org/iss-now.json")
        Response.raise_for_status()
        data = Response.json()
        
        
        message = message + " Location\n" + str(data['iss_position'] )
       
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        i = i + 1 
        time.sleep(10)
        
except Exception as e:
    print(e)
    
        