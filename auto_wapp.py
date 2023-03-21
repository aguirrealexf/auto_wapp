# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:46:00 2020

@author: Alex
"""

from twilio.rest import Client 
 
account_sid = 'ACda5705fd74129e51c3f240e98a573252' 
auth_token = '1e474dcd6fbb5e06c43ec2d03afdd636' 
client = Client(account_sid, auth_token) 

alex = 'whatsapp:+549351*******'

def send_msj():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Domingo 04/10/2020. APScheduler a cada 15 seg',      
                              to=alex
                              ) 
 
    print(message.sid)
