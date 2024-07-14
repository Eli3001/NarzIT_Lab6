
# tutaj importowane są wszystkie uzywane biblioteki

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# lista bibliotek do zainstalowania

install_list = [
    "json",
    "xml.etree.ElementTree",
    "PyYAML",
    'xmltodict'
]

for package in install_list:
    install(package)


