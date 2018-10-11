# 0x17 - Tuple Methods and Operations

```
root@kali:~# python
Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> my_tuple = ('a', 'p', 'p', 'l', 'e')
>>> my_tuple
('a', 'p', 'p', 'l', 'e')
>>> my_tuple.count('p')
2
>>> my_tuple.index('l')
3
>>> print('a' in my_tuple)
True
>>> print('b' in my_tuple)
False
>>> print('b' not in my_tuple)
True
>>> for name in ('Hello', 'World'):
...     print(name)
... 
Hello
World
>>> s = (1,2,3)
>>> sum = sum(s)
>>> sum
6
```