'''
Created on Mar 15, 2019

@author: rfai3591
'''

import string
import requests
import time
import random
import fileinput as fi

request_params = {'token': 'asPGAP0QNdGPnsDC8yoOb0uryWzHqzybrsOCF8nn'}
member_list = {'chonk', 'Dillon Foster', 'Gayhanderson', 'LABE', 'Rillo notPillo', 'Sack', 'Zo'}


def analyze_message(sender, received_message) -> str:
    received_message = received_message.casefold()
    generic_responses = ['m hahahaha', 'aRe yOu GuyS ChAtTiNG wiThOuT mEeE???', 'friggin city slicker', 'ok why would you say that to me', 'it doesn\'t matter', 'are you sure about that']
    tagged_user = ''
    full_response = ''

    if 'xo' in received_message:
        tagged_user = '@' + get_nickname(sender) + ' '
        incl_tag = True
        if 'fake' in received_message:
            if 'not fake' in received_message or 'isn\'t fake' in received_message:
                full_response = tagged_user + 'yeye'
            else:
                full_response = tagged_user + 'bet'

        if 'nickname' in received_message:
            incl_tag = False
            for member in member_list:
                if member in received_message:
                    name_to_nick = member
                else:
                    name_to_nick = sender

            if 'change' or 'set' or 'give' or 'new' in received_message:
                full_response = name_to_nick + '\'s nickname is now ' + add_nickname(name_to_nick)

            elif 'what' and not 'new' in received_message:
                full_response = name_to_nick + '\'s nickname is ' + get_nickname(name_to_nick)

        else:
            full_response = random.choice(generic_responses)

    else:
        incl_tag = False
        if 'smash' in received_message:
            smash_responses = ['I\'ll have you know, my wii fit is ranked', 'melee bad', 'i only play brawl', 'you don\'t even know how to wavedash']
            full_response = random.choice(smash_responses)

        if 'hang' in received_message:
            hang_responses = ['jazz game', 'effing snales', 'gimme 20', 'i\'ll be there in an hour and a half', 'nah i can\'t hang i have weener stuff to be doing instead', 'will there be girls?']
            full_response = random.choice(hang_responses)
        if 'car' in received_message:
            car_response = ['i used to have a car, but i crashed it on the information highway', 'bro i\'m a biker', 'i actually have a turbo in my transmission', 'i can only drive automatics']
            full_response = random.choice(car_response)

    if incl_tag:
        return tagged_user + full_response
    else:
        return full_response

# TODO: try making a separate txt file for every member of the group and rewriting it every time someone's nickname is changed

def add_nickname(name_to_nick) -> str:
    nick = name_to_nick
    nicknames_read = open('nicknames.txt').readlines()
    if name_to_nick in nicknames_read:
        nick = generate_nickname(name_to_nick)
        with open('nicknames.txt', 'w') as nicknames_write:
            to_write = ''
            for line in nicknames_read:
                if name_to_nick not in line:
                    to_write += line + '\n'
            to_write += '\n' + name_to_nick + '-' + nick
            if to_write:
                nicknames_write.write(to_write)
    else:
        nick = generate_nickname(name_to_nick)
        with open('nicknames.txt', 'a') as nicknames_append:
            to_append = '\n' + name_to_nick + '-' + nick
            nicknames_append.write(to_append)
    return nick


def generate_nickname(name_to_nick) -> str:
    nick_bank_1 = ['bingle', 'long', 'fink', 'chunk', 'nut', 'gonk', 'lorkus', 'chungus', 'bungus', 'dungus']
    nick_bank_2 = ['ton', 'bun', 'doink', 'dorf', 'florf', 'stein', 'heiny', 'beef', 'wink', 'boi', 'boy', 'town', 'man', 'guy']
    sender_bank = ['bum']
    if name_to_nick == 'chonk':
        sender_bank = ['ch', 'cho', 'chon', 'chonk', 'chod']
    if name_to_nick == 'Dillon Foster':
        sender_bank = ['Dill', 'Chilly', 'Fos', 'Dillon']
    if name_to_nick == 'LABE':
        sender_bank = ['La', 'Labe']
    if name_to_nick == 'Rillo notPillo':
        sender_bank = ['Rill', 'Pill', 'Rillo', 'Pillo', 'not', 'Rop', 'Pop']
    if name_to_nick == 'Sack':
        sender_bank = ['Sack', 'Sacc', 'Snack', 'Snacc']
    if name_to_nick == 'Gayhanderson':
        sender_bank = ['Goy', 'Hend', 'Guy', 'Gay', 'Hender', 'Hendz']

    prefix = random.choice(sender_bank)
    final_nickname = prefix + random.choice(nick_bank_1) + random.choice(nick_bank_2)
    return final_nickname


def get_nickname(sender) -> str:
    with open('nicknames.txt', 'r') as nicknames_file:
        for line in nicknames_file:
            if sender in line:
                return line.split('-', 1)[1]
        else:
            return sender


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


