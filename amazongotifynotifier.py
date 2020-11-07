#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re
import subprocess
import argparse
import config

parser = argparse.ArgumentParser(description="Check the delivery status of Amazon orders")
parser.add_argument("-a", "--add", type=str, metavar="", required=False, help="Add a package to deliveries.txt")
parser.add_argument("-t", "--test", action="store_true", help="Test active notification services")
parser.add_argument("-c", "--clean", action="store_true", help="Clean Deliveries file of all results")
args = parser.parse_args()

outstanding = []


def clean():
  open(config.file, 'w').close()

def notifications():
    try:
      response = requests.post(f'{config.gotifyserver}/message', params=config.params, files=config.files)
    except:
      print("Failed to send notification using Gotify, check token and url configuration")
    if config.libnotify == "True":
        try:
          libnotify = ["notify-send", "-u", "critical", "'Order Delivery'", "'Amazon Package Delivered'"]
          libnotify = subprocess.check_output(libnotify).decode("utf-8").strip() 
        except:
          print("Failed to send notification using libnotify, ensure that libnotify is installed or set libnotify to False")
    elif config.sshlibnotify == "True":
        try: 
          sshlibnotify = ["ssh", f"{config.sshserver}", "-t", "notify-send -u critical \"Order Delivered\" \"Amazon Package Delivered\""]
          sshlibnotify = subprocess.Popen(sshlibnotify, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except:
          print("Failed to send notification using SSH, ensure that openssh is installed, ssh keys configured, and that libnotify is installed on remote box, or set sshlibnotify to false")

if __name__ == "__main__":
  if args.add:
        with open(config.file, 'a') as deliveries:
          deliveries.write(args.add + "\n")
  elif args.test:
    notifications()
  elif args.clean:
    clean()
  else:
    #Opens delivery url file and scrapes out the status from each url's page and a loop to search for the keyword "Delivered" and sends a notification to a Gotify server and libnotify.
    with open(config.file) as deliveries:
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
    with open(config.file, 'w') as remaining:
       remaining.writelines(outstanding)
    #Notifications   
    try: 
      for match in matches:
        notifications()
    except:
      print('Malformed urls or empty deliveries file')  