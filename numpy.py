Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([1,2,3,4,5])
>>> a
array([1, 2, 3, 4, 5])
>>> b=np.array([1,2,3,4,5])
>>> b
array([1, 2, 3, 4, 5])
>>> a+b
array([ 2,  4,  6,  8, 10])
>>> c=a+b
>>> type(c)
<type 'numpy.ndarray'>
>>> bb=list(c)
>>> bb
[2, 4, 6, 8, 10]
>>> type(bb)
<type 'list'>
>>> a.max
<built-in method max of numpy.ndarray object at 0x037D6458>
>>> a.max()
5
>>> a
array([1, 2, 3, 4, 5])
>>> b
array([1, 2, 3, 4, 5])
>>> b.ndim()

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.ndim()
TypeError: 'int' object is not callable
>>> b.size()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.size()
TypeError: 'int' object is not callable
>>> type(b)
<type 'numpy.ndarray'>
>>> b.si

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.si
AttributeError: 'numpy.ndarray' object has no attribute 'si'
>>> b.size()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b.size()
TypeError: 'int' object is not callable
>>> b.size
5
>>> b.dtype
dtype('int32')
>>> b.dtype()

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.dtype()
TypeError: 'numpy.dtype' object is not callable
>>> b.dtype
dtype('int32')
>>> d=np.array([2+4j,3+9j])
>>> e=np.array([3+5j,4+10j])
>>> d.dtype
dtype('complex128')
>>> d+e
array([5. +9.j, 7.+19.j])
>>> d.dtype.name
'complex128'
>>> d.dtype.type
<type 'numpy.complex128'>
>>> type(d)
<type 'numpy.ndarray'>
>>> d.dtype
dtype('complex128')
>>> ff=np.array([1,23,4],dtype=int32)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    ff=np.array([1,23,4],dtype=int32)
NameError: name 'int32' is not defined
>>> ff=np.array([1,23,4],dtype='int32')
>>> ff
array([ 1, 23,  4])
>>> ff=np.array([1,23,4],dtype='int64')
>>> ff
array([ 1, 23,  4], dtype=int64)
>>> ff=np.array([1,23,4],dtype='float32')
>>> ff
array([ 1., 23.,  4.], dtype=float32)
>>> ff=np.array([1,23,4],dtype='float32')
>>> q=np.array([1,2,3,4])
>>> q.ndim
1
>>> w=np.array([1,2,3,4],[5,6,7,8])

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    w=np.array([1,2,3,4],[5,6,7,8])
TypeError: data type not understood
>>> w=np.array([[1,2,3,4],[5,6,7,8]])
>>> w
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
>>> w=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
>>> w
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> np.zeros(2,5)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    np.zeros(2,5)
TypeError: data type not understood
>>> np.zeros((2,5))
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> e = np.zeros((2,5))
>>> e.dtype
dtype('float64')
>>> e=np.ones((2,4))
>>> e
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> e.ndim
2
>>> w
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> w.ndim
2
>>> np.linspace(2,35,10)
array([ 2.        ,  5.66666667,  9.33333333, 13.        , 16.66666667,
       20.33333333, 24.        , 27.66666667, 31.33333333, 35.        ])
>>> np.arange(2,4,0.1)
array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3. , 3.1, 3.2,
       3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9])
>>> np.random.random((2,3))
array([[0.11126958, 0.95434242, 0.80295018],
       [0.10504667, 0.9168514 , 0.84592375]])
>>> rr = np.random.random((2,3))
>>> rr*10
array([[4.53863714, 5.98018964, 7.8157878 ],
       [6.46496493, 0.17311948, 7.11279937]])
>>> rr
array([[0.45386371, 0.59801896, 0.78157878],
       [0.64649649, 0.01731195, 0.71127994]])
>>> rr*10
array([[4.53863714, 5.98018964, 7.8157878 ],
       [6.46496493, 0.17311948, 7.11279937]])
>>> ww=list(int(rr*10))

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    ww=list(int(rr*10))
TypeError: only size-1 arrays can be converted to Python scalars
>>> ww=list((rr*10))
>>> ww
[array([4.53863714, 5.98018964, 7.8157878 ]), array([6.46496493, 0.17311948, 7.11279937])]
>>> ww[0]
array([4.53863714, 5.98018964, 7.8157878 ])
>>> w=ww[0]
>>> w
array([4.53863714, 5.98018964, 7.8157878 ])
>>> type(w)
<type 'numpy.ndarray'>
>>> www= list(w)
>>> www
[4.538637141637931, 5.980189638815662, 7.815787801239775]
>>> int(www)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(www)
TypeError: int() argument must be a string or a number, not 'list'
>>> for e in www[:]:
	print(int(e))

	
4
5
7
>>> ww
[array([4.53863714, 5.98018964, 7.8157878 ]), array([6.46496493, 0.17311948, 7.11279937])]
>>> q=np.array([1,2,3,4],[1,2,3,4])

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    q=np.array([1,2,3,4],[1,2,3,4])
TypeError: data type not understood
>>> q=np.array([[1,2,3,4],[1,2,3,4]])
>>> q
array([[1, 2, 3, 4],
       [1, 2, 3, 4]])
>>> q.shape
(2, 4)
>>> q.reshape(4,2)
array([[1, 2],
       [3, 4],
       [1, 2],
       [3, 4]])
>>> q
array([[1, 2, 3, 4],
       [1, 2, 3, 4]])
>>> q.reshape(4,3)

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    q.reshape(4,3)
ValueError: cannot reshape array of size 8 into shape (4,3)
>>> q.reshape(4,1)

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    q.reshape(4,1)
ValueError: cannot reshape array of size 8 into shape (4,1)
>>> q.reshape(8,1)
array([[1],
       [2],
       [3],
       [4],
       [1],
       [2],
       [3],
       [4]])
>>> q=np.array([[1,2,3,4])
	   
SyntaxError: invalid syntax
>>> q=np.array([1,2,3,4])
>>> q.shape()

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    q.shape()
TypeError: 'tuple' object is not callable
>>> q.shape
(4,)
>>> q
array([1, 2, 3, 4])
>>> q=np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    q=np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])
ValueError: only 2 non-keyword arguments accepted
>>> q=np.array([1,2,3,4],[5,6,7,8],[9,10,11,12]])
SyntaxError: invalid syntax
>>> q=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
>>> q.shape
(3, 4)
>>> q.ndim
2
>>> q[:]
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> q[:,0]
array([1, 5, 9])
>>> q[:2,0]
array([1, 5])
>>> q[:2,1]
array([2, 6])
>>> q[:2,0,2]

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    q[:2,0,2]
IndexError: too many indices for array
>>> q[:2,0:2]
array([[1, 2],
       [5, 6]])
>>> q[:]
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> q[:]
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> q=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
>>> q[1:3,2]
array([ 7, 11])
>>> q[1:3,2:]
array([[ 7,  8],
       [11, 12]])
>>> qq = np.linspace(2,35,10)
>>> qq.reshape(2,5)
array([[ 2.        ,  5.66666667,  9.33333333, 13.        , 16.66666667],
       [20.33333333, 24.        , 27.66666667, 31.33333333, 35.        ]])
>>> qq.reshape(5,2)
array([[ 2.        ,  5.66666667],
       [ 9.33333333, 13.        ],
       [16.66666667, 20.33333333],
       [24.        , 27.66666667],
       [31.33333333, 35.        ]])
>>> qq.max(axis=0)
35.0
>>> qq
array([ 2.        ,  5.66666667,  9.33333333, 13.        , 16.66666667,
       20.33333333, 24.        , 27.66666667, 31.33333333, 35.        ])
>>> qq.max(axis=1)

Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    qq.max(axis=1)
  File "C:\Python27\lib\site-packages\numpy\core\_methods.py", line 26, in _amax
    return umr_maximum(a, axis, None, out, keepdims)
AxisError: axis 1 is out of bounds for array of dimension 1
>>> qq.ndim
1
>>> qq=np.array([[1,2,3,4],[5,6,7,8]])
>>> qq.max(axis=0)
array([5, 6, 7, 8])
>>> qq.max(axis=1)
array([4, 8])
>>> qq.max
<built-in method max of numpy.ndarray object at 0x037F3DE0>
>>> qq.max()
8
>>> qq.transpose()
array([[1, 5],
       [2, 6],
       [3, 7],
       [4, 8]])
>>> qq.shape
(2, 4)
>>> qq
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
>>> uu = eye(2)

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    uu = eye(2)
NameError: name 'eye' is not defined
>>> a=[2,3,4,5]
>>> a=np.array([2,3,4,5])
>>> b=np.array([12,11,10,10])
>>> c=a/b**2
>>> c
array([0, 0, 0, 0])
>>> c=a/(b**2)
>>> c
array([0, 0, 0, 0])
>>> c=b/(a**2)
>>> c
array([3, 1, 0, 0])
>>> 
