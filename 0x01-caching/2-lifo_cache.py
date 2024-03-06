#!/usr/bin/env python3
"""stack cache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """queue cache class
    """

    def __init__(self):
        """intialize
        """
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """insert
        """
        if key is None or item is None:
            return
        self.__stack.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            del self.cache_data[self.__stack[-2]]
            print("DISCARD: {}".format(self.__stack.pop(-2)))

    def get(self, key):
        """retrieve
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
