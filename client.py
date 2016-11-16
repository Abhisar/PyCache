from pycache.BaseCacheable import Cacheable
from CacheImplementations.LRUCache import LRUCache


class Employee(Cacheable):
    def __init__(self,id, name):
        self.id = id
        self.name = name

    def key(self):
        return self.id


if __name__ == "__main__":
    cache = LRUCache(3)
    e1 = Employee(1, "E1")
    e2 = Employee(2, "E2")
    e3 = Employee(3 ,"E3")
    e4 = Employee(4, "E4")
    cache.insert_into_cache(e1)
    cache.insert_into_cache(e2)
    cache.insert_into_cache(e3)
    cache.insert_into_cache(e4)
    cache.get_from_cache(e2)
    #cache.delete_from_cache(e4)
    cache.printcache()

