from __future__ import print_function

try:
    fh=open('file1.txt')
except:
    print('Cannot open file')
else:
    for line in fh: print(line,end='')
