#!/usr/bin/python3
"""basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching class"""

    def __init__(self):
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        """insert in dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieve key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
