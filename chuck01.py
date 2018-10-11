import rd
while True:
    command = input("$: ")
    if command == "rd":
        rd.index()
    else:
        print 'not valid'
