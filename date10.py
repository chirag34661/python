Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=2
c=a**3
print(c)
8
0 and 10
0
10 and 20
20
false and 10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    false and 10
NameError: name 'false' is not defined. Did you mean: 'False'?
"false" and 10
10
0 or 10
10
10 or 20
10
"" and 10
''
"chirag" and "dewangan"
'dewangan'
0 and 20/10
0
10 and 20/10
2.0
10 and 20/0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    10 and 20/0
ZeroDivisionError: division by zero
8>>2
2
9>>2
2
10>>2
2
4>>2
1
#Assignment operator
#normal assignment and compound assignment
x=10
x+=10
print(x)
20
a,b,c,d,e=1,2,3,4,5
print(a,b,c,d,e)
1 2 3 4 5
a,b=b,a
a,b=1,3
a,b=b,a
print(a,b)
3 1
a,b,c,d,e=1,2,3,4
print(a,b,c,d,e)
SyntaxError: multiple statements found while compiling a single statement
a,b,c,d,e=1,2,3,4
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a,b,c,d,e=1,2,3,4
ValueError: not enough values to unpack (expected 5, got 4)
print(a,b,c,d,e)
3 1 3 4 5

a=10
b=10
a is b
True
a is not b
False
t=(1,2,3,4,5)
7 in t
False
7 in not t
SyntaxError: invalid syntax
7 not t
SyntaxError: incomplete input
7 not in t
True
d={1:}
SyntaxError: incomplete input
d={1:"chirag",2:}
SyntaxError: incomplete input

d={1:"chirag",2:"dewangan"}
>>> 'chirag' in d.values()
True
>>> d={1:"chirag",2:"dewangan"}
>>> for i in d.values()
SyntaxError: incomplete input
>>> x=(input("Enter anything "))
Enter anything 5
>>> l=x.split()
>>> l=x.split(",")
>>> x=(input("Enter anything "))
Enter anything 1,2,3,4,5
>>> l=x.split(",")
>>> print(l)
['1', '2', '3', '4', '5']
>>> x=(int(i) for i in input("Enter the data").split(','))
Enter the data1,2,4,6
>>> print(x)
<generator object <genexpr> at 0x0000021ACC259A80>
>>> x=(int(i) for i in input("Enter the data ").split(','))
Enter the data 1,2,3,4,5
>>> print(x)
<generator object <genexpr> at 0x0000021ACC2C66C0>
>>> x=[int(i) for i in input("Enter the data ").split(',')]
Enter the data 1,2,3,4,5
>>> print(x)
[1, 2, 3, 4, 5]
>>> sum-0
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sum-0
TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'int'
>>> sum=0
>>> for i in x:
...     sum+=int(i)
... 
...     
>>> print(sum)
15
>>> x=[int(i) for i in input("enter the data ").split('#')]
enter the data 1,2,3,4,5
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x=[int(i) for i in input("enter the data ").split('#')]
  File "<pyshell#67>", line 1, in <listcomp>
    x=[int(i) for i in input("enter the data ").split('#')]
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
>>> x=[int(i) for i in input("enter the data ").split('#')]
enter the data 1#2#3#4#5
>>> print(x)
[1, 2, 3, 4, 5]
>>> x=[eval(p) for p in input("Enter the data ").split()]
Enter the data 1 2 {1:"chirag"} (1,2,3,4)
>>> for i in x:
...     print(type(i))
... 
...     
<class 'int'>
<class 'int'>
<class 'dict'>
<class 'tuple'>
