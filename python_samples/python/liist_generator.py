Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\DS_ML_PY\machine-learning-using-python\python_samples\python\dice_simulation.py 
press Enter key to roll the dice...
t
Rolling.....Stopped
Value= 2
press y to continue or n to quit..a
a
choose either y or n

Traceback (most recent call last):
  File "C:\DS_ML_PY\machine-learning-using-python\python_samples\python\dice_simulation.py", line 8, in <module>
    haha=raw_input("press Enter key to roll the dice...\n")
  File "C:\Python27\lib\idlelib\PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> [x for x in range(1,21) if x%2!=0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
 RESTART: C:/DS_ML_PY/machine-learning-using-python/python_samples/python/liist_generator.py 
1
2
3
4
5
6
7
8
9
10
>>> 
 RESTART: C:/DS_ML_PY/machine-learning-using-python/python_samples/python/liist_generator.py 
>>> l1
2
3
4
5
6
7
8
9
10l

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
 RESTART: C:/DS_ML_PY/machine-learning-using-python/python_samples/python/liist_generator.py 
>>> l2, 3, 4, 5, 6, 7, 8, 9, 10]
SyntaxError: invalid syntax
'
>>> l
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
 RESTART: C:/DS_ML_PY/machine-learning-using-python/python_samples/python/liist_generator.py 
>>> l[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
TypeError: list indices must be integers, not tuple
>>> [each for each in range(1,11)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [each for each in range(1,21) if each%2==0]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> [each for each in range(1,21) if each%2!=0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> [d for each in range(1,21) if each%2!=0]

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    [d for each in range(1,21) if each%2!=0]
NameError: name 'd' is not defined
>>> [d for each in range(1,21) if each%2!=0]

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    [d for each in range(1,21) if each%2!=0]
NameError: name 'd' is not defined
>>> [each for each in range(1,21) if each%2!=0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> [h for h in range(1,21) if h%2!=0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> [h for h in range(1,21) if h%2!=0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> h
20
>>> a =[h for h in range(1,21) if h%2!=0]
>>> a
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
