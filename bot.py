import os
import json
import redis
import time
import requests
from flask import Flask, request, Response
from urllib.parse import urlparse
from slackclient import SlackClient
from twilio.rest import Client

TWILIO_PHONE = ''
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
SLACK_BOT_TOKEN = ''
SLACK_BOT_ID = ''
ADMIN_CHANNEL = ''
REDIS_CLOUD_URL = None
REDIS = ''

# initialize Flask, Slack, Twilio
app = Flask(__name__)
sc = SlackClient(SLACK_TOKEN)
tc = Client()

# connect to redis
# TODO: do redis or redis cloud? Try both, but in which order?
if REDISCLOUD_URL:   
    redis_url = urlparse(REDIS_CLOUD_URL)
    r = redis.StrictRedis(host=redis_url.hostname, port=redis_url.port, password=redis_url.password, decode_responses=True)


####################
# 
# Functions
# 
####################

# Prepare slack attachments for twilio
def get_slack_images_for_twilio():
    # Only handle images
    # TODO: what if attachment is not image
    return True

def get_twilio_images_for_slack():
    # TODO
    return True

def archive_channel(channel_id):
    # TODO
    return True

def new_text_alert():
    # TODO: send alert to admin channel
    return True

def auto_reply():
    # TODO: send auto reply
    return True

####################
# 
# Routes
# 
####################

# add new number
@app.route('/add', methods=['POST'])
def add_number():
    # Process submission of the add number dialog
    ## Name, number, message, send msg T/F, channel name (optional)
    # Creates user in DB
    # Creates user's slack channel
    # Sends welcome message to user's phone number via SMS
    # Posts welcome message in user's slack channel
    msg = "OK"
    return Response(msg), 200

# serve the add number dialog to slack
@app.route('/adddialog', methods=['POST'])
def trigger_add_dialog():
    # Handles slash command request
    # Triggers a dialog in slack for user to add phone number
    return Response(), 200

# remove user
@app.route('/remove', methods=['POST'])
def remove_number():
    # Remove from the DB
    # Archive the slack channel
    return Response(), 200

# List all users
@app.route('/list', methods=['POST'])
def list_numbers():
    # Get list of all numbers and channels
    # Post list in admin channel
    return Response(), 200

# set alert rules
@app.route('/alerts', methods=['POST', 'GET'])
def manage_alerts():
    # TODO
    return Response(), 200

# set auto reply rules
@app.route('/autoreplies', methods=['POST', 'GET'])
    # TODO
    return Response(), 200

# slack to twilio
@app.route('/slack', methods=['POST'])
def slack_to_twilio():
    # Process request payload
    # Handle challenge (TODO: is there a way around this?)
    # confirm token
    # ignore slack noise (not text, or fileshare)
    # get number's slack channel
    # handle images (if any)
    # send message via Twilio

    return Response(), 200

# twilio to slack
@app.route('/twilio', methods=['POST'])
def twilio_to_slack():
    # Get number, message, attachments from request
    # Lookup channel ID from number
    # Handle if lookup fails (TODO: alert in admin channel with details to create user if necessary)
    # Post message in user's slack channel

    return Response(), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    # TODO: change debug after working
    app.run(debug=True, port=port, host='0.0.0.0')
