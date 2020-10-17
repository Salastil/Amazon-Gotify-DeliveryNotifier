file = "/usr/lib/amazongotifynotifier/deliveries.txt" # Path to deliveries.txt.
gotifytoken = "" # Enter Gotify application token.
gotifyserver = "" # Enter Gotify server url or ip:port.
sshserver = "" # Enter user@ip or domain, SSH keys must be configured.
libnotify = "False"
sshlibnotify = "False"

params = (
  ('token', f'{gotifytoken}'),
)

files = {
  'title': (None, 'Order Delivery'),
  'message': (None, 'Amazon Package Delivered'),
  'priority': (None, '5'),
}