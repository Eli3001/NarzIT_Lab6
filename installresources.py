
# tutaj importowane są wszystkie uzywane biblioteki

from pip._internal import main as pipmain

install_list = [
    "PyYAML",
    'xmltodict',
    'dicttoxml'
]

# lista bibliotek do zainstalowania

def install_all():
    for package in install_list:
        pipmain(['install', package])


