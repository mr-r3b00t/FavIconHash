#!/usr/bin/env python3
#pip install mmh3
import mmh3
import base64
import requests

print("Get those favicon hashes for all your Shodan hunting needs.")

print("Making HTTP request to get favicon.ico") 
response = requests.get('https://outlook.com/owa/favicon.ico', verify=False)
print("Here's the BASE64 of the icon file:")
print(response.content)
favicon = base64.encodebytes(response.content)
print('Here is the MD5 hash for SHODAN searches e.g. https://www.shodan.io/sear>
hash = mmh3.hash(favicon)
print(hash)
