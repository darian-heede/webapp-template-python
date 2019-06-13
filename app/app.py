#!/usr/bin/env python

"""
This is a simple webapp template
using flask and pymongo.
"""

from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request
from pymongo import MongoClient, DESCENDING, ASCENDING
from datetime import datetime

__author__ = "Darian Heede"
__license__ = "ISC"
__status__ = "Prototype"

dotenv = join(dirname(__file__), '.env')
load_dotenv(dotenv)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
	client = MongoClient(getenv('APP_DB'))
	db = client.app
	entry = {
		"timestamp": datetime.now()
		,"ip": request.remote_addr
		,"method": request.method
		,"agent": str(request.user_agent)
	}
	entries = db.entries
	entry_id = entries.insert_one(entry).inserted_id
	data = entries.find().sort('timestamp', DESCENDING)
	client.close()
	return(render_template('index.html', data=data))

#if __name__ == '__main__':
#	app.run(
#		host=getenv('FLASK_HOST')
#		,port=getenv('FLASK_PORT')
#	)
