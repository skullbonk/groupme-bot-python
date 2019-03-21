'''
Created on Mar 15, 2019

@author: rfai3591
'''

import string
import requests
import time
import random

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}
member_list = {'chonk', 'Dillon Foster', 'Gayhanderson', 'LABE', 'Rillo notPillo', 'Sack', 'Zo'}

def analyze_message(received_message) -> str:
    received_message = received_message.casefold()
    generic_responses = ['m hahahahahahaha', 'aRe yOu GuyS ChAtTiNG wiThOuT mEeE???', 'friggin city slicker']

    if 'fake' in received_message:
        if 'not fake' in received_message or 'isn\'t fake' in received_message:
            full_response = 'yeye'
        else:
            full_response = 'bet'
    elif 'car' in received_message:
        full_response = 'i used to have a car, but i crashed it on the information highway'
    else:
        full_response = random.choice(generic_responses)
        
    return full_response

def build_bot_response(sender, received_message) -> str:
    received_message = received_message.casefold()
    bot_response = ''
    if 'xo' in received_message:
        bot_response = '@' + sender + ' '
        bot_response += analyze_message(received_message)
    return bot_response

def unsolicited_interjections(received_message):
    received_message = received_message.casefold()
    interjection = ''
    if 'smash' in received_message:
        interjection = 'I\'ll have you know, my wii fit is ranked'

    if interjection:
        post_params = {'bot_id': '9ac5c52ec5efaee1bce225eb92', 'text': interjection}
        requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
        request_params['since_id'] = message['id']

def add_nickname(sender):

    nicknames_file = open('nicknames.txt', 'r+')
    nicknames_string = nicknames_file.read()
    print(nicknames_file.read())
    if sender in nicknames_string:
        for line in nicknames_file:
            if sender in line:
                string.replace(line.index)
        string.replace()


def generate_nickname(sender) -> str:
    nick_bank_1 = ['Bingle', 'Long', 'Fink', 'Chunk', 'Nut', 'Gonk', 'Lorkus', 'Chungus', 'Bungus', 'Dungus']
    nick_bank_2 = ['ton', 'bun', 'doink', 'dorf', 'florf', 'stein', 'heiny', 'beef', 'wink', 'boi', 'boy', 'town', 'man', 'guy']
    if sender == 'chonk':
        prefix = random.choice(['c', 'ch', 'cho', 'chon', 'chonk', 'cheese'])
    elif sender == 'Dillon Foster':
        prefix = random.choice(['Dill', 'Chilly', 'Fos', 'Dillon'])
    elif sender == 'LABE':
        prefix = random.choice(['La', 'Lab', 'Labe'])
    elif sender == 'Rillo notPillo':
        prefix = random.choice(['Rill', 'Pill', 'Rillo', 'Pillo', 'not', 'Rop', 'Pop'])
    elif sender == 'Sack':
        prefix = random.choice(['Sack', 'S', 'Sacc', 'Snack', 'Snacc'])
    elif sender == 'Gayhanderson':
        prefix = random.choice(['Goy', 'Hend', 'Guy', 'Gay', 'Hender', 'Hendz'])

    final_nickname = prefix + random.choice(nick_bank_1) + random.choice(nick_bank_2)
    return final_nickname

while True:
    response_page = requests.get('https://api.groupme.com/v3/groups/35396592/messages', params=request_params)
    if response_page.status_code == 200:
        response_messages = response_page.json()['response']['messages']
        for message in response_messages:
            message_sender = message['name']
            latest_message = message['text']
            print(message['name'], ': ', message['text'])
            unsolicited_interjections(latest_message)

            if 'change' and 'nickname' in latest_message:
                add_nickname(message_sender)
            
            if message_sender in member_list:
                
                to_send = build_bot_response(message_sender, latest_message)
                if to_send:
                    # send response to the group
                    post_params = {'bot_id': '9ac5c52ec5efaee1bce225eb92', 'text': to_send}
                    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                    request_params['since_id'] = message['id']
                    break
    
    time.sleep(5)


