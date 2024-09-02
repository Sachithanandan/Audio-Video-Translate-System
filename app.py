import os
import sys
from flask import Flask
import pymongo
from json import load

# from modules.utils import *

STATIC_FOLDER = sys.path[0] + '/static/'
UPLOAD_FOLDER = sys.path[0] + '/static/uploads/'
TEMPLATES_FOLDER = sys.path[0] + '/templates/'

app = Flask(__name__, template_folder=TEMPLATES_FOLDER, static_folder=STATIC_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_URI'] = 'mongodb+srv://techtribes:techtribes123@cluster0.cmim8hl.mongodb.net/?retryWrites=true&w=majority'
app.secret_key = "SSKEY"

client = pymongo.MongoClient("mongodb://cluster0-shard-00-00.cmim8hl.mongodb.net:27017,cluster0-shard-00-01.cmim8hl.mongodb.net:27017,cluster0-shard-00-02.cmim8hl.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyz-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client.trans