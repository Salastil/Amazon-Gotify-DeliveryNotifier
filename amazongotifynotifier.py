#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re
import subprocess

file = "deliveries.txt" # Path to deliveries.txt.
gotifytoken = "" # Enter application token.
gotifyserver = "" # Enter gotify server url or ip:port.
sshserver = "" # Enter user@ip or domain, SSH keys must be configured.
libnotify = "False"
sshlibnotify = "False"

params = (
    ('token', f'{gotifytoken}'),
)

files = {
    'title': (None, 'Delivery'),
    'message': (None, 'Package Delivered'),
    'priority': (None, '5'),
}

if libnotify == "True":
  libnotify=["notify-send", "-u", "critical", "'Package Delivery'", "'Amazon Package Delivered'"] #Uncomment this if notifications via libnotify are desired.
else:
  libnotify = None
if sshlibnotify == "True":
  sshlibnotify = ["ssh", f"{sshserver}", "-t", "notify-send -u critical \"Package Delivered\" \"Amazon Package Delivered\""] #Uncomment this if notifications using libnotify via ssh are desired.
else:
  sshlibnotify = None

outstanding = []

#Opens delivery url file and scrapes out the status from each url's page and a loop to search for the keyword "Delivered" and sends a notification to a Gotify server and libnotify.
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
      global matches
      matches = stringsearch.finditer(status)
      #Nabbing all urls that aren't delivered and appending it to a list to be written back into deliveres.txt file absent completed orders.
      if combined.find("Delivered") != -1:
        pass
      else:
        outstanding.append(line)

with open(file, 'w') as remaining:
  remaining.writelines(outstanding)

for match in matches:
    try:
      response = requests.post(f'{gotifyserver}/message', params=params, files=files)
    except:
      print("Failed to send notification using Gotify, check token and url configuration")
    if libnotify:
      try: 
        libnotify = subprocess.check_output(libnotify).decode("utf-8").strip() 
      except:
        print("Failed to send notification using libnotify, ensure that libnotify is installed")
    elif sshlibnotify:
      try: 
        sshlibnotify = subprocess.Popen(sshlibnotify, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      except:
        print("Failed to send notification using SSH, ensure that openssh is installed, ssh keys configured, and that libnotify is installed on remote box.")





