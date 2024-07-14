import json
import xml.etree.ElementTree as ET
import xmltodict
import yaml
from parseinput import d_File


#converts from one of the three formats to dict obj.
def source_to_dict(file : d_File):
    dictobj = {}

    if file.ext == '.json':
        dictobj = json.loads(file.handle)
    elif file.ext == '.xml':
        dictobj = xmltodict.parse(file.handle) 
    elif file.ext in ['.yml','.yaml']:
        dictobj = yaml.safe_load(file.handle)

    return dictobj

