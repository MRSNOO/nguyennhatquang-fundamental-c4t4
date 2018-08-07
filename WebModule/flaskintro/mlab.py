# mongodb://<dbuser>:<dbpassword>@ds017432.mlab.com:17432/c4t4_movie

import mongoengine

host = "ds017432.mlab.com"
port = 17432
db_name = "c4t4_movie"
user_name = "mrsnoo1234"
password = "Nhatminh123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())