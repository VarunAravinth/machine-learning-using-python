

import random
print "Welcome to rock paper scissors game"
ch="oo"

print " Enter one of the following strings:\n"
print "rock\n","paper\n","scissors\n"

while ch!="exit":
    
    ch=raw_input("Enter your choice:")
    if ch=="exit":
        quit
    ch1=random.choice(['rock','paper','scissors'])
    print " You chose",ch
    print "Computer chose",ch1
    if ch=="rock" and ch1=="paper":
        print "You lost"
    if ch=="rock" and ch1=="scissors":
        print "You won"
    if ch=="rock" and ch1=="rock":
        print " Draw"
    
    if ch=="paper" and ch1=="paper":
        print "draw"
    if ch=="paper" and ch1=="scissors":
        print "You lost"
    if ch=="paper" and ch1=="rock":
        print "you won"
    
    if ch=="scissors" and ch1=="paper":
        print "You won"
    if ch=="scissors" and ch1=="scissors":
        print "draw"
    if ch=="scissors" and ch1=="rock":
        print " you lost"
   
        
    
