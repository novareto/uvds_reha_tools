from json import load
from icecream import ic

def convert_ds(filename):
    res = {}
    ds_content = load(filename)
    res['$schema'] = "https://json-schema.org/draft/2020-12/schema"
    res['$id'] = ds_content['name']
    res['description'] = ds_content['beschreibung']
    all_props = [x for x in ds_content['objekte']['objekt']]
    res["properties"] = [ x for x in all_props if x['typ'] == 'FORMULARVARIABLEN']
    ic(res["properties"])
    return res
