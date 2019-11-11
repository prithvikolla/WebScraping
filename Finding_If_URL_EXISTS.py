# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:13:22 2019

@author: spk0057
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://github.com/prithvikolla")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print('URL PRESENT IN INTERNET')
    
