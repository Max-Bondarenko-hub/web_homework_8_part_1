import connect
import json
from models import Authors, Quotes


Authors.drop_collection()
Quotes.drop_collection()


with open(r"json_files\authors.json", "r") as jf:
    data = json.load(jf)

    for dict in data:
        auth = Authors()
        auth.fullname = dict["fullname"]
        auth.born_date = dict["born_date"]
        auth.born_location = dict["born_location"]
        auth.description = dict["description"]
        auth.save()

with open(r"json_files\quotes.json", "r", encoding="utf8") as jf:
    data = json.load(jf)

    for dict in data:
        qt = Quotes()
        qt.tags = dict["tags"]
        auth = Authors.objects.get(fullname=dict["author"])
        qt.author = auth
        qt.quote = dict["quote"]
        qt.save()
