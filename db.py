from pymongo import MongoClient
import datetime
import os
import time

MONGO_URL = os.environ["mongo_server"]

client = MongoClient(MONGO_URL)

db = client.fbevents
events = db.events
queue = db.queue

def get_next_queue():
    next_id = list(queue.find({}).limit(1))[0]["_id"]
    return next_id

def delete_queue(id):
    queue.remove({"_id":id})
    return None

def insert_queue(unique_id, keyword):
    if type(id) is list:
        for unique_id in id:
            queue.update({"_id":unique_id}, {"$push": {"keywords" : keyword } }, upsert= True)
    else:
        queue.update({"_id":unique_id}, {"$push": {"keywords" : keyword } }, upsert= True)
    return None

def insert_event(document):
    events.update({"_id":document["_id"]}, document, upsert= True)
    return None
