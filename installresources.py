
# tutaj importowane są wszystkie uzywane biblioteki

import pip

install_list = [
    "PyYAML",
    'xmltodict',
    'dicttoxml'
]

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# lista bibliotek do zainstalowania

def install_all():
    for package in install_list:
        install(package)


