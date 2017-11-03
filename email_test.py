#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask
from flask.ext.mail import Mail,Message
import os

app=Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '727548963',
    MAIL_PASSWORD = 'dvossgmprieqbejh',
    MAIL_DEBUG = True)

mail=Mail(app)
@app.route("/")
def index():
    msg=Message('this is a test',sender="727548963@qq.com",recipients=['651002081@qq.com'])
    msg.body="haha ,a test"
    mail.send(msg)
    print 'mail is ok'
    return "<h1>ok</h1>"

if __name__=="__main__":
   app.run(host='0.0.0.0',debug=True)
