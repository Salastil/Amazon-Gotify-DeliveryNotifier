#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re
import subprocess

file = "deliveries.txt" # Path to deliveries.txt
gotifytoken = "EnterToken" # Enter application token
gotifyserver = "http://gotify.example.tld" # Enter gotify server url or ip:port


params = (
    ('token', f'{gotifytoken}'),
)

files = {
    'title': (None, 'Delivery'),
    'message': (None, 'Package Delivered'),
    'priority': (None, '5'),
}

notification=["notify-send", "-u", "critical", "'Package Delivery'", "'Amazon Package Delivered'"]
outstanding = []

#Opens delivery url file and scrapes out the status from each url's page and a loop to search for the keyword "Delivered" and sends a notification to a Gotify server and libnotify
with open(file) as deliveries:
    url = deliveries.readlines()
    for line in url:
      webpage = requests.get(line).text
      soup = BeautifulSoup(webpage, 'lxml')
      div = soup.find('div')
      status = div.find('span', id='primaryStatus').text
      status = status.strip()
      stringsearch = re.compile(r'^Delivered.')
      combined = status + " " + line
      print(combined)
      matches = stringsearch.finditer(status)
      for match in matches:
        response = requests.post(f'{gotifyserver}/message', params=params, files=files)
#        notify = subprocess.check_output(notification).decode("utf-8").strip() #Uncomment this if notifications via libnotify are desired.
#Nabbing all urls that aren't delivered and appending it to variable to be written back into url file absent completed orders.
      if combined.find("Delivered") != -1:
        pass
      else:
        outstanding.append(line)

with open(file, 'w') as remaining:
  remaining.writelines(outstanding)


