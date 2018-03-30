from __future__ import print_function
n=int(input("Enter a num:"))
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(1,n-1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    
