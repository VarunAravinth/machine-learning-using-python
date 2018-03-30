from __future__ import print_function

def main():
    for line in readfile('file12.txt'): print(line,end='')

def readfile(filename):
    fh=open(filename)
    return fh.readlines()

try:
    main()
except IOError as e:
    print("Cannot open the file:")
    s='aaa'
    s=str(e)
    print(s.)



    
    
    
