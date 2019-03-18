'''
Created on Mar 15, 2019

@author: rfai3591
'''

import requests
import time

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}

while True:
    response = requests.get('https://api.groupme.com/v3/groups/35396592/messages', params = request_params)
    
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']
    
        for message in response_messages:
            print(message['text'])
            if ('xo' in message):
                botResponse = 'oi piss off'
                
                # send response to the group
                post_params = {'bot_id' : '9ac5c52ec5efaee1bce225eb92', 'text' : botResponse}
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                request_params['since_id'] = message['id']
                break
    time.sleep(5)