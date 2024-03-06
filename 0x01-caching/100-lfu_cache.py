#!/usr/bin/env python3
"""queue cache
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """queue cache class
    """

    def __init__(self):
        """intialize
        """
        super().__init__()
        self.__queue = []
        self.__freq = {}

    def put(self, key, item):
        """insert
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.__queue.remove(key)
            self.__queue.append(key)
            self.cache_data[key] = item
            self.__freq[key] += 1
            return
        if len(self.cache_data) + 1 > super().MAX_ITEMS:
            temp = min(self.__freq.values())
            for i in self.__queue:
                if self.__freq[i] == temp:
                    del self.cache_data[i]
                    del self.__freq[i]
                    self.__queue.remove(i)
                    print("DISCARD: {}".format(i))
                    break
        self.__queue.append(key)
        self.cache_data[key] = item
        self.__freq[key] = 1

    def get(self, key):
        """retrieve
        """
        if key not in self.cache_data or key is None:
            return None
        self.__queue.remove(key)
        self.__queue.append(key)
        self.__freq[key] += 1
        return self.cache_data.get(key)
