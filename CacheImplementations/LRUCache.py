# Copyright 2016-17 Abhisar Mohapatra
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from pycache import BaseCache
from collections import deque

class LRUCache(BaseCache.Cache):
    def __init__(self, cachesize):
        super().__init__(cachesize)
        self.__hashmap = {}
        self.__lru_queue = deque(maxlen=cachesize)
        self.__count = 0

    def ispresent(self, key):
        try:
            self.__hashmap[key]
            return True
        except KeyError:
            return False

    def insert_into_cache(self, object):

        #Case 1 : When key is Already present in cache
        if self.ispresent(object.key()) is True:
            #Update LRU for the present Key
            self.__lru_queue.remove(self.__hashmap[object.key()])
            self.__lru_queue.append(object)
            return

        #Case 2 : When cache is not full and has still space for
        #incoming objects
        if self.__count < self.cachesize:
            #print(self.__count)
            self.__hashmap[object.key()] = object
            self.__lru_queue.append(object)
            self.__count+=1
            return

        #Case 3 : When cache is full but you have to insert new Object.
        #Eviction and Insert based on LRU scheme
        if self.__count == self.cachesize:
            del self.__hashmap[self.__lru_queue.popleft().key()]
            self.__hashmap[object.key()] = object
            self.__lru_queue.append(object)
            return

    def get_from_cache(self, object):
        """
        Method to get from cache and updates LRU queue
        :param object: Oject to be retrieved from cache
        :return:
        """
        try:
            self.__lru_queue.remove(self.__hashmap[object.key()])
            self.__lru_queue.append(object)
            return self.__hashmap[object.key()]
        except:
            raise "No key found in cache"

    def delete_from_cache(self, object):
        try:
            self.__lru_queue.remove(self.__hashmap[object.key()])
            del self.__hashmap[object.key()]
            self.count-=1
        except:
            return False

    def printcache(self):
        print(self.__lru_queue)
        print (len(self.__hashmap))
        for x in self.__lru_queue:
            print (str(x.name)+ " ")