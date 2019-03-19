'''
Created on Mar 15, 2019

@author: rfai3591
'''

import requests
import time

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}
# members = requests.get('https://api.groupme.com/v3/groups/35396592/members/')

while True:
    response = requests.get('https://api.groupme.com/v3/groups/35396592/messages', params=request_params)
    
    if response.status_code == 200:
        response_messages = response.json()['response']['messages']
        for message in response_messages:
            latestMessageSender = message['name']
            latestMessage = message['text']
            print(latestMessageSender, ': ', latestMessage)
            if ('xo' or 'Xo' in message['text']):
                if (latestMessageSender == 'xo-python'):
                    break
                elif (latestMessageSender == 'LABE'):
                    botResponse = 'labe lul more like lame'
                elif (latestMessageSender == 'Sack'):
                    botResponse = 'shut'
                elif (latestMessageSender == 'Rillo notPillo'):
                    botResponse = 'you would say ' + latestMessage
                elif (latestMessageSender == 'chonk'):
                    botResponse = 'why yes'
                
                else:    
                    botResponse = 'wear my socks'
                    
                # send response to the group
                post_params = {'bot_id': '9ac5c52ec5efaee1bce225eb92', 'text': botResponse}
                requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                request_params['since_id'] = message['id']
                break
    time.sleep(5)