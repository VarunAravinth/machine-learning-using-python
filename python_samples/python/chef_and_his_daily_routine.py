test = input()

while test!=0:
    string = raw_input()
    length = len(string)
    for i in string:
        if i == 'C':
            if (i+1) == 'E' or 'S':
                print 'yes'

        elif i == 'E':
            if(i+1) == 'S':
                print "yes"
            else:
                print "no"
        else:
            print 'no'

    test-=1
