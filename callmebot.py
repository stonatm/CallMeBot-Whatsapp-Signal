# (c) stonatm@gmail.com
# CallMeBot REST API to send messages to Signal, WhatsApp messenger

'''
SIGNAL BOT
Add the phone number +34 603 21 25 97 into your Phone Contacts. (Name it it as you wish)
Send this message "I allow callmebot to send me messages" to the new Contact created (using Signal Messaging of course)
The bot will answer you with your personal apikey.
'''
class signal:

  import requests as urequests

  PHONE = ''
  APIKEY = ''
  initialise = False

  def _parse_out(text):
    out = str(text)
    out = out.replace(' ','%20')
    out = out.replace(':','%3A')
    out = out.replace('/','%2F')
    return out

  def init(phone, apikey):
    signal.PHONE = phone
    signal.APIKEY = apikey
    signal.initialise = True

  def send_message(message):
    if not signal.initialise:
      return
    url =  'https://api.callmebot.com/signal/send.php?phone=' + str(signal.PHONE) + '&apikey=' + str(signal.APIKEY) + '&text=' + str( signal._parse_out(message) )
    response = signal.urequests.get( url )
    return (response.text)

  def send_image(image_url):
    if not signal.initialise:
      return
    url =  'https://api.callmebot.com/signal/send.php?phone=' + str(signal.PHONE) + '&apikey=' + str(signal.APIKEY) + '&image=' + str( signal._parse_out(image_url) )
    response = signal.urequests.get( url )
    return (response.text)

'''
WHATSAPP BOT
Add the phone number +34 698 28 89 73 into your Phone Contacts. (Name it it as you wish)
Send this message "I allow callmebot to send me messages" to the new Contact created (using WhatsApp of course)
Wait until you receive the message "API Activated for your phone number. Your APIKEY is 123123" from the bot.
'''

class whatsapp:
#import urequests
  import requests as urequests

  PHONE = ''
  APIKEY = ''
  initialise = False

  def _parse_out(text):
    out = str(text)
    out = out.replace(' ','%20')
    out = out.replace(':','%3A')
    out = out.replace('/','%2F')
    out =  out.replace('\n','%0A')
    return out

  def init(phone, apikey):
    whatsapp.PHONE = phone
    whatsapp.APIKEY = apikey
    whatsapp.initialise = True

  def send_message(message):
    if not whatsapp.initialise:
      return
    url =  'https://api.callmebot.com/whatsapp.php?phone=' + str(whatsapp.PHONE) + '&apikey=' + str(whatsapp.APIKEY) + '&text=' + str( whatsapp._parse_out(message) )
    response = whatsapp.urequests.get( url )
    return (response.text)
