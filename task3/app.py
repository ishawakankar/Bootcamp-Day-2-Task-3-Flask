import os
from flask import Flask,render_template,url_for, json

def showjson():
    SITE_ROOT=os.path.realpath(os.path.dirname(__file__))
    json_url=os.path.join(SITE_ROOT,"static/data","taiw.json")
    data=json.load(open("D:\taiw.json"))
    return render_template('showjson.jade', data=data)