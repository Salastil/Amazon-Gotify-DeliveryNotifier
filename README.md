# Amazon-Gotify-DeliveryNotifier
An Amazon delivery status scraper for sending notifications to a Gotify server.


![gotify](https://user-images.githubusercontent.com/46979341/95823923-7807c880-0cfc-11eb-8739-b11b61b4a219.png)


### Requirements
Python >=3.6 [Uses formatted string literals](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498)
- bs4
- lxml
- requests
- libnotify (optional)
## How to Install
``` 
git clone https://github.com/Salastil/Amazon-Gotify-DeliveryNotifier
cd Amazon-Gotify-DeliveryNotifier
pip3 install -r requirements.txt
Using a text editior enter Gotify credentials into amazongotifynotifier.py
mv amazongotifynotifier.py /usr/bin/amazongotifynotifier.py
crontab -e
Paste in:
*/5 * * * * /usr/bin/python3 /usr/bin/amazongotifynotifier.py >/dev/null 2>&1
````
## Usage
Add in Gotify application token and url into amazongotifynotifier.py, uncomment line 41 if libnotify is installed on local box and notifications via libnotify are desired

Copy url from the tracking page into deliveries.txt
![trackingpage](https://user-images.githubusercontent.com/46979341/95823925-78a05f00-0cfc-11eb-9e2c-48ac4436d2f2.png)


This program is capable of printing the current progress of outstanding orders entered into deliveries.txt but this is not the intended purpose of the program. It should be run via a timer program such as cron or systemd timers. It will automatically prune delivered orders as it sends a notification out.
![output](https://user-images.githubusercontent.com/46979341/95823924-7807c880-0cfc-11eb-9427-b7744a4845e8.png)

## TODO:

Write command line options to enter in tracking urls using argparse ie: "amazongotifynotifier.py -a https://amazon.com/trackingurlhere" or -q for squelching print statements.
