'''
Created on Mar 20, 2019

@author: rfai3591
'''

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT') or 5000)