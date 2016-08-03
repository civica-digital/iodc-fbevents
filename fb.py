import requests
import os

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']


def token():
    r = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret)
    access_token = r.text.split('=')[1]
    return access_token

def event_info(facebook_id, token):
    #when object type = "posts", gets posts, when "comments", gets comments.
    url = 'https://graph.facebook.com/v2.5/'+facebook_id + "?fields=description,end_time,place,name,start_time,id,attending_count,category,cover,is_page_owned&access_token=" + token
    r = requests.get(url)
    facebook_data= r.json()
    return(facebook_data)

def event_data(facebook_id, data_type, token):
    url  =  'https://graph.facebook.com/v2.5/'+facebook_id + "/"+data_type+ "?limit=100&access_token=" + token
    r = requests.get(url)
    incoming_data =  r.json()["data"]
    data = []
    while len(incoming_data) > 0:
        try:
            data = data + incoming_data
            url = r.json()["paging"]["next"]
            r = requests.get(url)
            incoming_data =  r.json()["data"]
        except:
            incoming_data = []
    return data

def get_event_profile(facebook_id):
    data = event_info(facebook_id, token())
    data["_id"] = facebook_id
    data["attending"] = event_data(facebook_id,"attending", token())
    data["feed"] =  event_data(facebook_id,"feed", token())
    return data
