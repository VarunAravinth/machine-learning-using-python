def blastoff(n):
    if n<0:
        print "BlastOff!"
    else:
        print n
        blastoff(n-1)

blastoff(10);
        
