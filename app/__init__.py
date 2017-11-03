#!/usr/bin/env python
# _*_coding:utf-8_*_

from flask import Flask,request,render_template,redirect,session
from flask.ext.mail import Mail,Message
import json
import utils
import util

app = Flask(__name__)
app.secret_key="2134j1kjsdjfadsfl"
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '727548963',
    MAIL_PASSWORD = 'dvossgmprieqbejh',
    MAIL_DEBUG = True)


import user
import cmdb
import job
import log
import mem
import ansible_test
