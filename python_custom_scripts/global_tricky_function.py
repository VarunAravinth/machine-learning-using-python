def printer():

    global sample
    print(sample)     
    print('inside the fun')
    sample = 2
    print(sample)




sample = 1   #1 
printer()   #2
print('outside the fun')
print(sample)

