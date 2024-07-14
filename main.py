from installresources import install_all
from parseinput import d_File, importdata
from convert import source_to_dict
from savefile import savef


if __name__== "__main__":
    try:
        print('installing dependencies...')
        install_all()

        print('importing...')    
        infile, outfile = importdata()

        print('converting...')
        data = source_to_dict(infile)
        #print(data)

        print('saving...')
        savef(data,outfile)
        print('gotowe!')
    except Exception as e:
        print(e)
        input()


