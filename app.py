#!/usr/bin/python3
# -*- coding:utf8 -*-
import json
import time
from flask import Flask, request, make_response, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from fbchat import Client
from fbchat.models import *

# CONSTANT
bichdiep_uid = 100004095614111

email = "minhdq99hp@gmail.com"
password = "facebookminh0110"
uid = 100003944511010



app = Flask("Love Advisor")
client = Client(email, password)

def respond(fullfilment):
    return make_response(jsonify({'fulfillmentText': fullfilment}))

def send_message(uid, text):
    client.send(Message(text=text), thread_id=uid, thread_type=ThreadType.USER)


@app.route('/love-advisor', methods=['POST'])
def handler():
    try:
        req = request.get_json(silent=True, force=True)
       
        # print(json.dumps(req))
        # location = req.get('queryResult').get('parameters').get('current-location')

        if "good night" in req.get('queryResult').get('queryText'):
            send_message(uid, "Em ngủ ngon nhé <3")
            return respond("Done !")
        else:
            return respond("Sorry, I don't understand.")
    except Exception as e:
        print(e)
        return respond("Sorry, an error occurred. Please check the server logs.")


def exit_signal_handler(sig, frame):
    client.logout()
    sys.exit()

def main():
    signal.signal(signal.SIGINT, exit_signal_handler)

    app.run()


if __name__ == '__main__':
    main()
