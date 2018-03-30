Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> #2 Dictionary
>>> 
>>> student = {'name': ' }
	   
SyntaxError: EOL while scanning string literal
'
>>> dict1 = {'name': 'virat','age':29,'role':'top_order_batsman'}
>>> dict1 = {'name': 'Dhoni','age':35,'role':'wicket_keeper_batsman'}
>>> dict2 = {'name': 'Dhoni','age':35,'role':'wicket_keeper_batsman'}
>>> dict1 = {'name': 'virat','age':29,'role':'top_order_batsman'}
>>> dict1
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict2
{'age': 35, 'role': 'wicket_keeper_batsman', 'name': 'Dhoni'}
>>> dict3 = {'name': 'R Ashwin','age':32,'role':'All-rounder'}
>>> dict1;dict2;dict3
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
{'age': 35, 'role': 'wicket_keeper_batsman', 'name': 'Dhoni'}
{'age': 32, 'role': 'All-rounder', 'name': 'R Ashwin'}
>>> dict4={}
>>> import scrapy

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    import scrapy
ImportError: No module named scrapy
>>> import scrapy

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import scrapy
  File "C:\Python27\lib\site-packages\scrapy\__init__.py", line 27, in <module>
    from . import _monkeypatches
  File "C:\Python27\lib\site-packages\scrapy\_monkeypatches.py", line 20, in <module>
    import twisted.persisted.styles  # NOQA
  File "C:\Python27\lib\site-packages\twisted\persisted\styles.py", line 24, in <module>
    from twisted.python import log
  File "C:\Python27\lib\site-packages\twisted\python\log.py", line 17, in <module>
    from zope.interface import Interface
ImportError: No module named zope.interface
>>> dict1;dict2;dict3;dict4
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
{'age': 35, 'role': 'wicket_keeper_batsman', 'name': 'Dhoni'}
{'age': 32, 'role': 'All-rounder', 'name': 'R Ashwin'}
{}
>>> dict1
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict5 = dict1
>>> dict5
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict1
{'age': 29, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict1['age'] = 30
>>> dict1
{'age': 30, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict5
{'age': 30, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict5 = dict1.copy()
>>> dict5['name'] = 'S Raina'
>>> dict5
{'age': 30, 'role': 'top_order_batsman', 'name': 'S Raina'}
>>> dict1
{'age': 30, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict5.fromkeys()

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict5.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> fall= ('name','age','role')
>>> dict6 ={}
>>> dict6.fromkeys(fall)
{'age': None, 'role': None, 'name': None}
>>> dict6['age']

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict6['age']
KeyError: 'age'
>>> dict6['age'] = 27
>>> fall_l = ['name','age']
>>> dict7={}
>>> dict7.fromkeys(fall_1)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict7.fromkeys(fall_1)
NameError: name 'fall_1' is not defined
>>> dict7.fromkeys(fall_l)
{'age': None, 'name': None}
>>> type(fall)
<type 'tuple'>
>>> fall.count()

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    fall.count()
TypeError: count() takes exactly one argument (0 given)
>>> fall.count('name')
1
>>> fall.index('name')
0
>>> fall[0]
'name'
>>> fall[1]
'age'
>>> fall[2]
'role'
>>> fall[3]

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    fall[3]
IndexError: tuple index out of range
>>> fall[0] = 'namessss'

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    fall[0] = 'namessss'
TypeError: 'tuple' object does not support item assignment
>>> fall = ('hello','ll')
>>> a = 10
>>> a = 'ajfhajf'
>>> student = ('name','age','roll')
>>> newdict1 = {}
>>> newdict1.fromkeys(student)
{'age': None, 'name': None, 'roll': None}
>>> newdict1.fromkeys(student,'new_student')
{'age': 'new_student', 'name': 'new_student', 'roll': 'new_student'}
>>> newdict1
{}
>>> newdict1.fromkeys(student,'new_student')
{'age': 'new_student', 'name': 'new_student', 'roll': 'new_student'}
>>> newdict1
{}
>>> str(newdict1)
'{}'
>>> newdict1.fromkeys(student,'new_student')
{'age': 'new_student', 'name': 'new_student', 'roll': 'new_student'}
>>> str(newdict1)
'{}'
>>> newdict1 = dict.fromkeys(student)
>>> newdict1
{'age': None, 'name': None, 'roll': None}
>>> str(newdict1)
"{'age': None, 'name': None, 'roll': None}"
>>> newdict1={}
>>> newdict1.fromkeys(student)
{'age': None, 'name': None, 'roll': None}
>>> newdict1
{}
>>> aj = dict.fromkeys(student)
>>> aj
{'age': None, 'name': None, 'roll': None}
>>> a = list.append('10')

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a = list.append('10')
TypeError: descriptor 'append' requires a 'list' object but received a 'str'
>>> a
'ajfhajf'
>>> a
'ajfhajf'
>>> a = list.append([1,2,3])

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a = list.append([1,2,3])
TypeError: append() takes exactly one argument (0 given)
>>> a = list.append()

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = list.append()
TypeError: descriptor 'append' of 'list' object needs an argument
>>> dict1
{'age': 30, 'role': 'top_order_batsman', 'name': 'virat'}
>>> dict1.get('role')
'top_order_batsman'
>>> dict1['role']
'top_order_batsman'
>>> dict1.has_key('role')
True
>>> dict1.has_key('role2')
False
>>> dict1.update(dict2)
>>> dict1
{'role': 'wicket_keeper_batsman', 'name': 'Dhoni', 'age': 35}
>>> sample = ('one','two','three')
>>> g1 = dict.fromkeys(sample)
>>> g1
{'three': None, 'two': None, 'one': None}
>>> g2 ={'four':None,'five':None}
>>> g1.update(g2)
>>> g1
{'four': None, 'three': None, 'five': None, 'two': None, 'one': None}
>>> g1
{'four': None, 'three': None, 'five': None, 'two': None, 'one': None}
>>> g1.keys()
['four', 'three', 'five', 'two', 'one']
>>> g1.values()
[None, None, None, None, None]
>>> g1.values()
[None, None, None, None, None]
>>> gg = [4,2,4,6,9,1,4,2]
>>> reversed(gg)
<listreverseiterator object at 0x032DFF50>
>>> list(reversed(gg))
[2, 4, 1, 9, 6, 4, 2, 4]
>>> type(reversed(gg))
<type 'listreverseiterator'>
>>> print reversed(gg)
<listreverseiterator object at 0x032DFF50>
>>> gg
[4, 2, 4, 6, 9, 1, 4, 2]
>>> gg.extend('jiii')
>>> gg
[4, 2, 4, 6, 9, 1, 4, 2, 'j', 'i', 'i', 'i']
>>> strr= 'hello'
>>> gg.extend(strr)
>>> gg
[4, 2, 4, 6, 9, 1, 4, 2, 'j', 'i', 'i', 'i', 'h', 'e', 'l', 'l', 'o']
>>> gg.index(1,'hiii')

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    gg.index(1,'hiii')
TypeError: slice indices must be integers or have an __index__ method
>>> gg.insert(1,'hiii')
>>> gg
[4, 'hiii', 2, 4, 6, 9, 1, 4, 2, 'j', 'i', 'i', 'i', 'h', 'e', 'l', 'l', 'o']
>>> 
