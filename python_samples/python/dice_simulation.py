#random simulation
from __future__ import print_function
import time
import random
mylist=[1,2,3,4,5,6]
a=True
while(a):
    haha=raw_input("press Enter key to roll the dice...\n")
    print('Rolling.',end='')
    for i in range(1,5):
        
        time.sleep(1)
        print('.', end='')
        if(i==4):
            print("Stopped")
            time.sleep(1)
    ans=random.choice(mylist)
    print("Value= %d"%(ans))
    loop=raw_input("press y to continue or n to quit..")
    print(loop)
    if(loop=='y'or loop=='Y'):
        a=True
    elif(loop=='N' or loop=='n'):
        a=False
    else:
        print('choose either y or n')
print("Thank you!")        
