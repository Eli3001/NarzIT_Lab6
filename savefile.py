import json
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
import yaml


def save(data : dict, fname : str, ext : str):

    if ext == ".json":
        with open(fname, "w") as outfile: 
            json.dump(data, outfile)

    elif ext == '.xml':
        xmldata = dicttoxml(data)
        with open(fname, "w") as outfile: 
            outfile.write(xmldata)
       
    elif ext in ['.yml','.yaml']:
        with open(fname, "w") as outfile: 
            yaml.dump(data, outfile)


