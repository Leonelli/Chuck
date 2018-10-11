import sys
import rd

#print(len(sys.argv))
if len(sys.argv) == 3:
    if(sys.argv[1]=='rd'):
        rd.readfunc(sys.argv[2])
    else:
        print ('comando sconosciuto')
else:
    print ('Numero di parametri non valido')






