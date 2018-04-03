def print3():
    global num
    num = 2
    print(num)   #2


num = 1
print3()
print('outside the fun')
print(num)


