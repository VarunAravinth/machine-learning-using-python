def isBetween(x,y,z):
    if(x>=y and x<=z):
        return True
    else:
        return False

y=input("Enter the lower boundary:\n");
z=input("Enter the upper boundary:\n");
x=input("Enter the number to be checked:\n");
if isBetween(x,y,z):
    print x,"is between",y,"and",z;
else:
    print x,"is not between",y,"and",z;
    
        
