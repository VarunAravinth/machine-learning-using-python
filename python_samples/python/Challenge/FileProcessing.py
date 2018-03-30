# Reading from a file
print "# MAGIC POTIONS OF DR.SNAPE ! \n"
print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "

#CREATE A FUNCTION FOR FILE READING ( GOOD APPROACH :P)
def filereader():
    
    #opening a file
    file = open("snape.txt","r")

    #COUNTER
    step=1
    #reading from a file
    for line in file:
        print ("line "+str(step)+": " + line)
        #print ("\n")
        step += 1

    file.close()


filereader()

