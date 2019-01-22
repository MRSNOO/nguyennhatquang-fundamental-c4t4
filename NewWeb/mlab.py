# mongodb://<dbuser>:<dbpassword>@ds163014.mlab.com:63014/newweb

import mongoengine

host = "ds163014.mlab.com"
port = 63014
db_name = "newweb"
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