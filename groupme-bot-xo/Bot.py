'''
Created on Mar 15, 2019

@author: rfai3591
'''

import string
import requests
import time
import random
import fileinput

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}
member_list = {'chonk', 'Dillon Foster', 'Gayhanderson', 'LABE', 'Rillo notPillo', 'Sack', 'Zo'}


def analyze_message(sender, received_message) -> str:
    received_message = received_message.casefold()
    generic_responses = ['m hahahahahahaha', 'aRe yOu GuyS ChAtTiNG wiThOuT mEeE???', 'friggin city slicker']
    tagged_user = ''
    full_response = ''

    if 'xo' in received_message:
        tagged_user = '@' + get_nickname(sender) + ' '

        if 'fake' in received_message:
            if 'not fake' in received_message or 'isn\'t fake' in received_message:
                full_response = 'yeye'
            else:
                full_response = 'bet'
        elif 'car' in received_message:
            full_response = 'i used to have a car, but i crashed it on the information highway'

        if 'nickname' in received_message:
            for member in member_list:
                if member in received_message:
                    name_to_nick = member
                else:
                    name_to_nick = sender

            if 'change' or 'set' or 'give' or 'new' in received_message:
                full_response = add_nickname(name_to_nick)
            elif 'what' in received_message:
                for member in member_list:
                    if member in received_message:
                        name_to_nick = member
                    else:
                        name_to_nick = sender
                full_response = get_nickname(name_to_nick)
        else:
            full_response = random.choice(generic_responses)
    else:
        if 'smash' in received_message:
            full_response = 'I\'ll have you know, my wii fit is ranked'

        if 'hang' in received_message:
            hang_responses = ['jazz game', 'effing snales', 'gimme 20', 'i\'ll be there in an hour and a half', 'nah i can\'t hang i have weener stuff to be doing instead']
            full_response = random.choice(hang_responses)

    return tagged_user + full_response


def add_nickname(sender) -> str:
    nick = ''
    with open('nicknames.txt', 'r+') as nicknames_file:
        nicknames_string = nicknames_file.read()
        print(nicknames_file.read())
        if sender in nicknames_string:
            for line in nicknames_file:
                if sender in line:
                    nick = generate_nickname(sender)
                    line = sender + '- ' + nick
                    nicknames_file.writeline()
        else:
            nick = generate_nickname(sender)
            nicknames_file.write(sender + '-' + nick)
        print(nick)
    return nick



def get_nickname(sender) -> str:
    with open('nicknames.txt', 'r') as nicknames_file:
        for line in nicknames_file:
            if sender in line:
                return line.split('-', 1)[1]
        else:
            return sender



def generate_nickname(name_to_nick) -> str:
    nick_bank_1 = ['Bingle', 'Long', 'Fink', 'Chunk', 'Nut', 'Gonk', 'Lorkus', 'Chungus', 'Bungus', 'Dungus']
    nick_bank_2 = ['ton', 'bun', 'doink', 'dorf', 'florf', 'stein', 'heiny', 'beef', 'wink', 'boi', 'boy', 'town', 'man', 'guy']
    sender_bank = ['bum']
    if name_to_nick == 'chonk':
        sender_bank = ['c', 'ch', 'cho', 'chon', 'chonk', 'cheese']
    if name_to_nick == 'Dillon Foster':
        sender_bank = ['Dill', 'Chilly', 'Fos', 'Dillon']
    if name_to_nick == 'LABE':
        sender_bank = ['La', 'Lab', 'Labe']
    if name_to_nick == 'Rillo notPillo':
        sender_bank = ['Rill', 'Pill', 'Rillo', 'Pillo', 'not', 'Rop', 'Pop']
    if name_to_nick == 'Sack':
        sender_bank = ['Sack', 'Sacc', 'Snack', 'Snacc']
    if name_to_nick == 'Gayhanderson':
        sender_bank = ['Goy', 'Hend', 'Guy', 'Gay', 'Hender', 'Hendz']

    prefix = random.choice(sender_bank)
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

            if message_sender in member_list:
                to_send = analyze_message(message_sender, latest_message)
                if to_send:
                    # send response to the group
                    post_params = {'bot_id': '9ac5c52ec5efaee1bce225eb92', 'text': to_send}
                    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                    request_params['since_id'] = message['id']
                    break
    time.sleep(5)


