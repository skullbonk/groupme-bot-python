'''
Created on Mar 20, 2019

@author: rfai3591
'''

from os import environ
from flask import Flask

Bot = Flask(__name__)
Bot.run(environ.get('PORT') or 5000)