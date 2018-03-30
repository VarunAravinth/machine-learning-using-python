Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> newlist = [1,2,3,4,5,6,7,8,9]
>>> newlist[1]
2
>>> newlist[4:8]
[5, 6, 7, 8]
>>> range(10,10)
[]
>>> range(10,11)
[10]
>>> range(1.50,2.50)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    range(1.50,2.50)
TypeError: range() integer end argument expected, got float.
>>> newlist[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> newlist[:4]
[1, 2, 3, 4]
>>> newlist[4:]
[5, 6, 7, 8, 9]
>>> newlist[-1:]
[9]
>>> newlist[-1]
9
>>> newlist[-1:-5]
[]
>>> 
