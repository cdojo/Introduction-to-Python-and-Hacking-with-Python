# 0x19 - Lists

The most basic data structure in Python is the sequence. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

Python has six built-in types of sequences, but the most common ones are lists and tuples.
These operations include indexing, slicing, adding, multiplying, and checking for membership.
Python has built-in functions for finding the length of a sequence and for finding its largest and smallest elements.

Python list is a data structure which is used to store various types of data like integer, floating values, strings, character and so on.
In python, lists are mutable that is Python will not create a new list if we modify an element of the list.
It works as a container that holds other objects in a given order.

We can perform various operations like insertion and deletions on list.
A list can be composed by storing a sequence of different type of values separated by commas.
Python list is enclosed between square **[]** brackets and elements are stored in the index basis with starting index 0.

```
root@kali:~/Desktop# python
Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> data1 = [1,2,3,4]
>>> data2 = ['x', 'y', 'z']
>>> data3 = [12.5, 11.6]
>>> data4 = ['hello', 'world']
>>> data5 = []
>>> data6 = ['house', 10, 5.66, 'a']
>>> list1 = [10,20]
>>> list2 = [30,40]
>>> list3 = list1 + list2
>>> list3
[10, 20, 30, 40]
```