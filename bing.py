import os
from py_bing_search import PyBingWebSearch

API_KEY = os.environ["bing_api"]

def get_id(incoming_url):
    event_id = incoming_url.split("events/")[1]
    event_id  = event_id.split("/")[0]
    event_id = event_id.split("?")[0]
    return event_id

def extract_pages(set_ids, input_results):
    output_ids = []
    for result in input_results:
        user_id = get_id(result.url)
        try:
            int(user_id)
            output_ids.append(user_id)
        except:
            None
    set_ids = set_ids.union(output_ids)
    return(set_ids)

def get_results_ids_fb(query):
    search_term = query + "  site:facebook.com/events"
    bing_web = PyBingWebSearch(API_KEY, search_term)
    results = bing_web.search(limit=50, format='json')
    set_ids = set([])
    while len(results)>0:
        print(len(results))
        set_ids = extract_pages(set_ids,results)
        results = bing_web.search(limit=50, format='json') #1-50
    return(set_ids)
