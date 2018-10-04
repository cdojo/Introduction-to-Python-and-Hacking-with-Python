# 0x05 - Pandas Basics

* Pandas is a high-level dara manipulation tool developed by **Wes McKinney**
* It is built on the Numpy package and its key data structure is called the **DataFrame**
* DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

```
root@kali:~# pip install pandas
Collecting pandas
  Downloading https://files.pythonhosted.org/packages/b7/e3/f52d484244105fa3d558ce8217a5190cd3d40536076bef66d92d01566325/pandas-0.23.4-cp27-cp27mu-manylinux1_x86_64.whl (8.9MB)
    100% |████████████████████████████████| 8.9MB 180kB/s 
Requirement already satisfied: pytz>=2011k in /usr/lib/python2.7/dist-packages (from pandas)
Requirement already satisfied: numpy>=1.9.0 in /usr/lib/python2.7/dist-packages (from pandas)
Requirement already satisfied: python-dateutil>=2.5.0 in /usr/lib/python2.7/dist-packages (from pandas)
Installing collected packages: pandas
Successfully installed pandas-0.23.4
```

## Code

### example_pandas.py

```
python example_pandas.py 
     area    capital        coutry  pupulation
0   8.516   Brasilia        Brazil      200.40
1  17.100     Moscow        Russia      143.50
2   3.286  New Dehli         India     1252.00
3   9.597    Beijing         China     1357.00
4   1.221   Pretoria  South Africa       52.98
```