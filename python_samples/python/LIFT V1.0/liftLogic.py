# LIFT LOGIC
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
        time.sleep(1)
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
    if pos==0:
        call=raw_input("Press 'u' to go up - ")
    else:
        call=raw_input("Press 'u' to go up or 'd' to go down - ")
        
        
    
    if call=='u':
        lift(call)

    if call=='d':
        lift(call)
        
    else:
        print("Please press u to go up!")
    print("lift is in=%d"%(pos))






