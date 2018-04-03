def tables(n):
    print n,"Tables upto 10 :\n"
    i=1;
    while i<=12:
        print i,"*",n,"=",i*n
        i=i+1

print" TABLES "
c=input("Enter a number to know its tables:")
tables(c)
