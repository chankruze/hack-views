"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Aug 26 2020 23:46:53 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""

import requests
import time

count = 0

while(True):
    print(count, " - " ,requests.get('https://camo.githubusercontent.com/d9998672ad9d7eff95458e325a071e94b8b836ee/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6368616e6b72757a65').status_code)
    count += 1
    time.sleep(1)