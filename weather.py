#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

from config import WAPI_key

def lookup():
    # make HTTP request
    try:
        url = "https://api.darksky.net/forecast/{}/55.75,37.62?lang=ru&units=si".format(WAPI_key)
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            
            # return parsed data for bot
            return data_parsing(json_data)
        else: return None
    
    except:
        return None
    
        
def data_parsing(data):
    newlist = []
    timestamp = data["currently"]["time"]
    
    # if current time is 06:00 am
    
    # else if current time is 12:00 pm or 6:00 pm
        # if monday, wednesday or friday and 12:00 pm
        
        # else
        
    # else
    
    # append status to newlist
    
    # check if wind alert
        # append wind alert status to newlist
    
    return 
        
def degree_to_directions():
    return

def is_wind_alert(wind_speed, wind_gust):
    return

