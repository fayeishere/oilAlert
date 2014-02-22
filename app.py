from flask import Flask
import twilio.twiml
from twilio.rest import TwilioRestClient
import ystockquote
ACCOUNT_SID = "Twilio ID"
AUTH_TOKEN = "Twilio Token"
FOLLOWER_ALERT_PHONE_NUMBER = "Phone number to message"
FROM_PHONE_NUMBER = "Generic"
 
app = Flask(__name__) 

def oil():
  # crude oil
  crude = ystockquote.get_price('CLJ14.NYM')
  print crude
  # heating oil
  heat = ystockquote.get_price('HOH14.NYM')
  print heat
  if float(crude) < 98:
    body = "Low price alert! Crude: " + crude + " Heat: " + heat
    messager(body)
    print body
  return

def messager(body):
  twilio_client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
  message = twilio_client.sms.messages.create(to=FOLLOWER_ALERT_PHONE_NUMBER, from_=FROM_PHONE_NUMBER, body=body)
  return
if __name__ == '__main__':
  oil()