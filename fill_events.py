import db
import fb

next_id = db.get_next_queue()
while "_id" in next_id:
    try:
        profile = get_event_profile(next_id["_id"])
        profile["keywords"] = next_id["keywords"]
        db.delete_queue(next_id["_id"])
        next_id = db.get_next_queue()
    except:
        "Terminé"
