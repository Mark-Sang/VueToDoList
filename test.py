from flask import Flask, render_template, abort, redirect, url_for, request
from flask_bootstrap import Bootstrap
import pymongo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId
from time import time

from bson import json_util

app = Flask(__name__)
# app配置

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["todos"]["todos"]



@app.route('/search', methods=['GET','POST'])
def search_records():
    dic = []
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/add', methods=['GET','POST'])
def add_records():
    dic = []
    my_json = request.get_json()
    mydb.insert_one(my_json)
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/delete', methods=['GET','POST'])
def delete_records():
    dic = []
    my_json = request.get_json()
    mydb.delete_one({"_id" : ObjectId(my_json["_id"])})
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

@app.route('/change', methods=['GET','POST'])
def change_records():
    dic = []
    my_json = request.get_json()
    myquery = { "_id":  ObjectId(my_json.pop("_id")) }
    newvalues = { "$set": my_json }
    mydb.update_one(myquery, newvalues)
    for i in mydb.find():
        dic.append(i)
    return json_util.dumps(dic)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
