from abc import ABCMeta, abstractmethod

class Cache(metaclass=ABCMeta):
    def __init__(self, cachesize):
        self.cachesize = cachesize

    @abstractmethod
    def ispresent(self, key):
        """
        This method has to be implemented by subclass
        :param key: Key of Cacheable Object
        :return: If key is present in cache or not
        """
        pass

    @abstractmethod
    def insert_into_cache(self, object):
        """
        This method has to be implemented by subclass
        :param object: Object
        :return:
        """
        pass

    @abstractmethod
    def delete_from_cache(self, key):
        """
        This method has to be implemented by subclass
        :param key: Delete the following key and corresponding object from cache
        :return:
        """
        pass

    @abstractmethod
    def get_from_cache(self,key):
        """
        Get object from cache for specified cache
        :param key:
        :return:
        """
        pass


