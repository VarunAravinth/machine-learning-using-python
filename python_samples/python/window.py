

import Tkinter
import random
import Image,ImageTk
top=Tkinter.Tk()

def mymethod(ch):
    ch1=random.choice(['rock','paper','scissors'])
    print "Computer chose:",ch1
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
    if(ch=="exit"):
        exit
    

B=Tkinter.Button(top,text="ROCK",command=lambda:mymethod("rock"))

B1=Tkinter.Button(top,text="PAPER",command=lambda:mymethod("paper"))
B2=Tkinter.Button(top,text="SCISSORS",command=lambda:mymethod("scissors"))
B3=Tkinter.Button(top,text="EXIT",command=lambda:mymethod("exit"))
B.pack()
B1.pack()
B2.pack()
B3.pack()
top.mainloop()
