'''
Created on Mar 15, 2019

@author: rfai3591
'''

import requests
import time
import random

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}
member_list = {'chonk', 'Dillon Foster', 'Gayhanderson', 'LABE', 'Rillo notPillo', 'Sack', 'Zo'}


def analyze_message(received_message) -> str:
    generic_responses = ['m hahahahahahaha', 'what am i, your big stinky corndog?']
    
    
    if 'fake' in received_message:
        if 'not fake' in received_message:
            full_response = 'yeye'
        else:
            full_response = 'bet'
    elif 'car' in received_message:
        full_response = 'i used to have a car, but i crashed it on the information highway'
    else:
        full_response = random.choice(generic_responses)
    return full_response
                
                
def buildBotResponse(sender, message: str) -> str:
    message = message.casefold()
    bot_response = ''
    if 'xo' in message:
        bot_response = '@' + sender + ' '
        bot_response += analyze_message(message)
    return bot_response






while True:
    response_page = requests.get('https://api.groupme.com/v3/groups/35396592/messages', params=request_params)
    if response_page.status_code == 200:
        response_messages = response_page.json()['response']['messages']
        for message in response_messages:
            message_sender = message['name']
            latest_message = message['text']
            print(message['name'], ': ', message['text'])
            
            if message_sender in member_list:
                
                to_send = buildBotResponse(message_sender, latest_message)
                if to_send:
                    # send response to the group
                    post_params = {'bot_id': '9ac5c52ec5efaee1bce225eb92', 'text': to_send}
                    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                    request_params['since_id'] = message['id']
                    break
    
    time.sleep(5)


