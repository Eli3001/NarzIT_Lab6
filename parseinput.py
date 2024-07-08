# - Task1: parsowanie argumentów przekazywanych przy uruchomieniu programu

"""

Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)
Sposób użycia: program.exe pathFile1.x pathFile2.y
gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).
Powyższe wywołanie programu powinno prawidłowo rozpoznać format, pobrać dane z pathFile1.x, a
następnie utworzyć nowy plik pathFile2.y i przekonwertować dane zgodnie z nowym formatem.

"""

import sys

class d_File:
    def __init__(self,path,mode):
        try:
            self.handle = open(path,mode)
            self.ext = self.handle.name.split('.')[1]
        except Exception as e:
            self.handle = None
            self.ext = None
            raise IOError(f"Nie udało się otworzyc pliku {path}.")

def importdata():
    try:
        #read the 2nd and 3rd args from console call (the first one is the scriptname)
        file1 = d_File(sys.argv[1],'r')
        file2 = d_File(sys.argv[2],'w')

    except IOError as e:
        print(e)
        return None

    allowed = ['.xml','.json','.yml']

    if file1.ext not in allowed or file2.ext not in allowed:
        print('Niepoprawny format.')
        return None
    
    return (file1,file2)



