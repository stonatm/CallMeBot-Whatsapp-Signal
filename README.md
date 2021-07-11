# CallMeBot-Whatsapp-Signal
Micropython / python rest api to send messages to Whatsap, Signal throught CallMeBot service (https://www.callmebot.com).

## source code:
file [callmebot.py](callmebot.py)

## Signal
Simple library to send text messages to your signal number.

### requirements:
Add the phone number **+34 603 21 25 97** into your Phone Contacts. (Name it it as you wish)
Send this message "**I allow callmebot to send me messages**" to the new Contact created (using Signal Messaging of course)
The bot will answer you with your personal apikey.

### usage:
```
# import library
from callmebot import signal

# initialize library (run once)
signal.init("YOUR_PHONE_NUMBER, "YOUR_API_KEY")
# send text message to your signal number
signal.send_message("text of your message")
# send image url do display
signal.send_image("IMAGE_URL")
```


## Whatsapp
Simple library to send text messages to your whatsapp number.

### requirements:
Add the phone number **+34 698 28 89 73** into your Phone Contacts. (Name it it as you wish)
Send this message "**I allow callmebot to send me messages**" to the new Contact created (using WhatsApp of course)
Wait until you receive the message "API Activated for your phone number. Your APIKEY is 123123" from the bot.

### usage:
```
# import library
from callmebot import whatsapp

# initialize library (run once)
whatsapp.init("YOUR_PHONE_NUMBER, "YOUR_API_KEY")
# send text message to your whatsapp number
whatsapp.send_message("text of your message")
```
