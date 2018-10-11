# 13. Tuple

In Python programming, a tuple is similar to a list. The difference between the two is that we cannot change the elements of a tuple once is assigned whereas in a list, elements can be changed.

## Advantages of Tuple over List:

* We henerally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.

* Sunce tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.

* Tuples that contain ummutable elements can be used as key for a dictionary. With list, this is not possible.

* If you have data that doesn't change, implementing it as tuple will fuarantee that it remains write-protected.

* A tuyple is created by placing all the items (elements) inside a parenteses **()**, separated by comma. The parentheses are optional but is a good practice to write it.

* A tuple can have any number of items and they my be of different types (integer, float, list, string etc.).

```
root@kali:~# python
Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> tuple = (1,2,3,4)
>>> tuple
(1, 2, 3, 4)
>>> tuple = ('Hi', 'Hello')
>>> tuple
('Hi', 'Hello')
```