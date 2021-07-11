# CallMeBot-Whatsapp-Signal
Micropython / python lrest api to send messages to Whatsap, Signal throught CallMeBot service

## Signal
Simple library to send text messages to your signal number.

### usage:
'''
# import library
from callmebot import signal

# initialize library (run once)
signal.init("YOUR_PHONE_NUMBER, "YOUR_API_KEY")
# send text message to your signal number
signal.send_message("text of your message")
# send image url do display
signal.send_image("IMAGE_URL")
'''


## Whatsapp
Simple library to send text messages to your whatsapp number.

### usage:
'''
# import library
from callmebot import whatsapp

# initialize library (run once)
whatsapp.init("YOUR_PHONE_NUMBER, "YOUR_API_KEY")
# send text message to your whatsapp number
whatsapp.send_message("text of your message")
'''
