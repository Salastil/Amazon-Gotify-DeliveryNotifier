# Amazon-Gotify-DeliveryNotifier
An Amazon delivery status scraper for sending notifications to a Gotify server.


![gotify](https://user-images.githubusercontent.com/46979341/95823923-7807c880-0cfc-11eb-8739-b11b61b4a219.png)


### Requirements
Python >=3.6 [Uses formatted string literals](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498)
- bs4
- lxml
- requests
- libnotify (optional)
- openssh (optional, requires libnotify on remote box)

## How to Install
``` 
git clone https://github.com/Salastil/Amazon-Gotify-DeliveryNotifier
cd Amazon-Gotify-DeliveryNotifier
pip3 install -r requirements.txt
Using a text editor enter Gotify credentials into config.py
sudo ./install.sh
crontab -e
Paste in:
*/5 * * * * /usr/bin/python3 /usr/bin/amazongotifynotifier.py >/dev/null 2>&1
````

## Usage
Add in Gotify application token and url into amazongotifynotifier.py and call it via a timer application such as cron or systemd timers. 

An option to test your notification configuration exists by calling amazongotifynotifier -t

Copy url from the tracking page and run amazongotifynotifier.py -a "urlhere"
Be mindful of the shell bracing, or not bracing characters, if the url is malformed it will throw an exception. 
![trackingpage](https://user-images.githubusercontent.com/46979341/95823925-78a05f00-0cfc-11eb-9e2c-48ac4436d2f2.png)



This program is capable of printing the current progress of outstanding orders entered into deliveries.txt however, this is not the intended purpose of the program. It should be run via a timer program such as cron or systemd timers. It will automatically prune delivered orders as it sends a notification out.
![output](https://user-images.githubusercontent.com/46979341/95823924-7807c880-0cfc-11eb-9427-b7744a4845e8.png)

