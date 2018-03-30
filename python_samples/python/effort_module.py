from __future__ import print_function
from random import shuffle

i=int(input("Enter the effort in hours:"))
n=int(input("Enter the total number of incidents:"))

#mylogic
quo=int(i/n)
rem=int(i%n)

for ii in range(1,n+1):
    print(str(ii)+'.'+str(quo))
        
