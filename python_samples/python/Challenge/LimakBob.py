#s=int(input('Test:'))
a=int(input())
b=int(input())
i=1
while (a>0 and b>0):
    #print('ss')
    a-=i
    print('a=',a)
    if (a<=0):
        print('Bob')
        break
    i=i+1
    b-=i
    print('b=',b)
    if (b<0):
        print('Limak')
        break
    i=i+1

print('Out')
