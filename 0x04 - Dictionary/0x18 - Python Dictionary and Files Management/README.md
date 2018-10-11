# 0x18 - Python Dictionary and Files Management

In this article, you'll learn about the file and directory management in Python, i.e. creating a directory, renaming it, listing all directories and working with them.

If there are a lager number of files to handle in your Python program, you can arrange your code within different directories to make things more manageable.

A directory or folder is a collection of files and sub directories. Python has the **os** module, which provides us with useful methods to work with directories (and files as well).

```
root@kali:~/Desktop# python
Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/root/Desktop'
>>> os.chdir('/root/')
>>> os.getcwd()
'/root'
>>> os.chdir('/root/Desktop')
>>> os.getcwd()
'/root/Desktop'
>>> os.listdir('/root/Desktop')
['mount-shared-folders.sh', 'restart-vm-tools.sh']
>>> os.mkdir('new-folder')
>>> os.listdir('/root/Desktop')
['mount-shared-folders.sh', 'restart-vm-tools.sh', 'new-folder']
>>> os.rename('new-folder', 'rename-new-folder')
>>> os.listdir('/root/Desktop')
['mount-shared-folders.sh', 'restart-vm-tools.sh', 'rename-new-folder']
>>> os.rmdir('rename-new-folder')
>>> os.listdir('/root/Desktop')
['mount-shared-folders.sh', 'restart-vm-tools.sh']
```