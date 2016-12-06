# PyCache
License : **Apache 2.0**

This library aims to solve the problem of generic object(Python) caching without depending on 3rd party caching systems 
like Memcached or Redis for cases where it isn't really required.

Library has been written in such a way it can be extensible by following standards through implementations of 
Python Abstract Base Classes.

**pycache folder** : It has all the base classes. One that ensures ensures all cache schemes follow a similar implemntation i.e
                 https://github.com/Abhisar/PyCache/blob/master/pycache/BaseCache.py
                 and 
                 Other one is for the Objects to be cacheable they have to subclass this Base class
                 https://github.com/Abhisar/PyCache/blob/master/pycache/BaseCacheable.py
                 
**CacheImplenations folder**: This folder contains different caching schemes.
                   Currently for my use case only **LRU** scheme has been implemented by me.Feel free to add a pull request incase                    you want to add new implementations.
                   
# A sample working example :
https://github.com/Abhisar/PyCache/blob/master/client.py
