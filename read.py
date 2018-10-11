
import sys

def readfunc(path="./test/lorem.txt"):
    print('I\'m reading your text... \n')
    textfile = open(path, "r")
    print(textfile.read())
    print('\n')


if(sys.argv[1]=='rd'):
    #print (sys.argv[1])
    #readfunc("./test/lorem.txt")
    readfunc(sys.argv[2])
else:
    print ('Non valido')




