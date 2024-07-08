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
    def __init__(self,path):
        try:
            self.handle = open(path)
            self.ext = self.handle.name.split('.')[1]
        except Exception as e:
            self.handle = None
            self.ext = None
            print('failed to open file.')

def importdata():
    
    #read the 2nd and 3rd args from console call (the first one is the scriptname)
    file1 = d_File(sys.argv[1])
    file2 = d_File(sys.argv[2])

    print(file1.ext,file2.ext)






importdata()




