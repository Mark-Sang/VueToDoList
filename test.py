from flask import Flask, render_template, abort, redirect, url_for, request,session
from flask_bootstrap import Bootstrap
import pymongo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId
from time import time
from datetime import timedelta
import os
from bson import json_util
import datetime

app = Flask(__name__) 

#在flask当中使用 session 时，必须要做一个配置、即 flask的session中需要用到的秘钥字符串，可以是任意值
app.config['SECRET_KEY'] = "renyi"
app.config["SESSION_COOKIE_HTTPONLY"] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=20)  # 配置20天有效

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["todos"]["todos"]


@app.route('/SetID', methods=['GET','POST'])
def SetID_records():
    now = datetime.datetime.now()
    now = str(now)  
    mydb = myclient["todos"]["user"]
    while mydb.count_documents({ 'name': now}, limit = 1):
        now = datetime.datetime.now()
        now = str(now)   
    session["name"] = now
    session.permanent = True
    mydb.insert_one({"name":now})
    return json_util.dumps("SetID success")
    
@app.route('/GetID', methods=['GET','POST'])
def GetID_records():
    name = session.get("name")
    mydb = myclient["todos"]["user"]
    ID = mydb.find({"name" : name})
    return json_util.dumps(ID)

@app.route('/search', methods=['GET','POST'])
def search_records():
    dic = []
    my_json = request.get_json()
    mydb = myclient["todos"][my_json["ID"]]
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/add', methods=['GET','POST'])
def add_records():
    dic = []
    my_json = request.get_json()
    mydb = myclient["todos"][my_json["ID"]]
    mydb.insert_one(my_json)
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/delete', methods=['GET','POST'])
def delete_records():
    dic = []
    my_json = request.get_json()
    mydb = myclient["todos"][my_json["ID"]]
    mydb.delete_one({"_id" : ObjectId(my_json["_id"])})
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/change', methods=['GET','POST'])
def change_records():
    dic = []
    my_json = request.get_json()
    mydb = myclient["todos"][my_json["ID"]]
    myquery = { "_id":  ObjectId(my_json.pop("_id")) }
    newvalues = { "$set": my_json }
    mydb.update_one(myquery, newvalues)
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

if __name__ == '__main__':
    app.run()
