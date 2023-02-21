# crt/__init__.py

import requests

'''
Connection setup ....
'''

session = requests.Session()
session.params = {}

# import all the things
from .crtlib import *
from .api import *