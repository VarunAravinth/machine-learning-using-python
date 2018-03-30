# LIFT LOGIC
from __future__ import print_function
import time


def lifting(floors):      #going up action method
    global pos
    print("Lift moving up to %d"%(floors))
    for i in range(pos+1,floors+1):
        print(i)
        time.sleep(1)    #A MAGIC METHOD IN PROGRESS 
    print("reached")
    pos=floors

def _lifting(floors):    #going down action method
    global pos
    print("Lift moving down to %d"%(floors))

    for i in range(pos,floors-1,-1):
        print(i)
        time.sleep(1)    #A MAGIC METHOD IN PROGRESS
    print("reached")
    pos=floors
    
    


def lift(value):
    flag=0
    #flag=1 for UP and flag =0 for down
    
    global pos
    global maxx
    if (value=='u'):
        if pos==0:
            flag=1
            print("UP")
        if flag==1:
            floor=int(input("Enter floor :"))
            if floor<=maxx:
                lifting(floor)
            else:
                print("Max floors is %d" %maxx)
                print("Please provide something else")

                
        else:
            flag=1
            print("UP")

            floor=int(input("Enter floor:"))
            if floor<=maxx:
                lifting(floor)
            else:
                print("Max floors is %d"%maxx)
                print("Please provide something else")


    elif (value=='d'):
        print("down")
        flag=0
        floor=int(input("Enter floor:"))
        if floor<=pos:
            _lifting(floor)
        else:
            print("Enter a valid floor")
                
            
            

print("===================WELCOME TO THE LIFT SIMULATOR (VERSION ALPHA)===============")

pos=0#initially the lift will start from ground
maxx=int(input("Enter Max Floor:"))
while(1):
    if pos==0:     #CODE IS LOOPING HERE !! FIGURE OUT WHY
        print("Press ",end='')
        upicon = u'\N{BLACK UP-POINTING TRIANGLE}'
        print(upicon,end='')
        print(" to go up:",end='')
        call=raw_input()
        print (call)
    else:
        call=raw_input("Press 'u' for up or 'd' to go down - ")
    if call=='u':
        print("Entered this loop")
        lift(call)
    
    if call=='d':
        lift(call)
        






