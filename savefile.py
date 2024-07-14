import json
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
import yaml


def savef(data : dict, file):

    if file.ext == "json":            
        json.dump(data,file.handle, indent=4)

    elif file.ext == 'xml':
        xmldata = dicttoxml(data).decode('utf-8')
        print('\n\n',xmldata)
        file.handle.write(xmldata)
        
    elif file.ext in ['yml','yaml']:
        yaml.dump(data, file.handle)


