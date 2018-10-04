# 0x01 - Global and Local Variables

Global and Local correspond to a variable's reach within a script or program.

## Global Variable

A global variable is one thant can be accessed anywhere.

## Local Variable

A local variable is the opposite, it can only accessed within its frame.

---

The difference is that global variables can be accessed locally, but not modified locally inherently. A local variable cannot be accessed globally, inherently.

## Code

### global_local_var.py

* Examlpe 01:

```
root@kali:~# python global_local_var.py 
10
```

* Examlpe 02:

```
root@kali:~# python global_local_var.py 
Traceback (most recent call last):
  File "global_local_var.py", line 34, in <module>
    example2()
  File "global_local_var.py", line 10, in example2
    x += 5
UnboundLocalError: local variable 'x' referenced before assignment
```

* Examlpe 03:

```
root@kali:~# python global_local_var.py 
15
```

* Examlpe 04:

```
root@kali:~# python global_local_var.py 
10
15
15
```

* Examlpe 05:

```
root@kali:~# python global_local_var.py 
10
35
```