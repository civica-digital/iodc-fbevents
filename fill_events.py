import db
import fb

next_id = db.get_next_queue()
while "_id" in next_id:
    try:
        print(next_id["_id"])
        profile = fb.get_event_profile(next_id["_id"])
        profile["keywords"] = next_id["keywords"]
        db.insert_event(profile)
        db.delete_queue(next_id["_id"])
        next_id = db.get_next_queue()
    except:
        print("Finished")
