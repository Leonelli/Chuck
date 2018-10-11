import os.path

def index():
    textfile = open("./test/lorem.txt", "r") 
    print(textfile.read()) 


def readfunc(path="./test/lorem.txt"):
    print('I\'m reading your text... \n')
    if(os.path.exists(path)):
        #print('File exist')
        textfile = open(path, "r")
        print(textfile.read())
        print('\n')
    else:
        print('File doesnt exist!!')
        print('\n')
