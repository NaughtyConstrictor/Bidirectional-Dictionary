# Inheriting from built-in containers in Python: Creating a bi-directionl mapping

When inheriting from built-in classes like `dict` or `list`, one would expect that methods like `pop` or `get` would use `__delitem__`,  or that methods like `setdefault` or `update` or `__init__` would call `__setitem__` under the hood, but that isn't the case.  
The reason is that a lot of the code for these methods is in-lined, that is the same code is copy-pasted for each method for performance reasons (to avoid the overhead of function calls).  
So inheriting from built-in containers directly would require a lot of code since you have to redifine a lot of methods. Other alternatives, depending on your needs and how much customization you want, are using: `collections.UserDict` or `collections.abc.MutableMapping`.

For more informations check:
- [The problem with inheriting from dict and list in Python](https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/) by Trey Hunner
- [Custom Python Dictionaries: Inheriting From dict vs UserDict](https://realpython.com/inherit-python-dict/) by Real Python
- [Custom Python Dictionaries: Inheriting From list vs UserList](https://realpython.com/inherit-python-list/) by Real Python
- [collectionsabc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
- [Python's collections.abc | InvertibleDict](https://www.youtube.com/watch?v=oUt1feRoyvI) by mCoding
