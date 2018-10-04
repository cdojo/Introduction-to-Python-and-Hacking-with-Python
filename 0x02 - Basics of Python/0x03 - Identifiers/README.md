# 0x03 - Identifiers

Identifier is the name given to entities like class, function, variables etc, in Python. It helps differentiating one entity from another.

Identifiers can be a combination of letters in lowecase **(a to z)** or uppercase **(A to Z)**  or digits **(0 to 9)** or an underscore **(_)**. Names like **myClass**, **var_1** and **print_this_to_screen**, all are valid example.

```
root@kali:~# python
Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> var_1=10
>>> var_1
10
>>> 1variable
  File "<stdin>", line 1
    1variable
            ^
SyntaxError: invalid syntax
>>> variable1=10
>>> variable1
10
>>> global=100
  File "<stdin>", line 1
    global=100
          ^
SyntaxError: invalid syntax
>>> var@123=200
  File "<stdin>", line 1
    var@123=200
       ^
SyntaxError: invalid syntax
>>> var123=200
>>> var123
200
>>> variable123456789variable123456789=200
>>> variable123456789variable123456789
200
```