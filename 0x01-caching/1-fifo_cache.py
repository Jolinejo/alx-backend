#!/usr/bin/env python3
"""queue cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """queue cache class
    """

    def __init__(self):
        """intialize
        """
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """insert
        """
        if key is None or item is None:
            return
        self.__queue.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            del self.cache_data[self.__queue[0]]
            print("DISCARD: {}".format(self.__queue.pop(0)))

    def get(self, key):
        """retrieve"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
