#!/usr/bin/env python3
"""Base Caching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCaching:
      - Simple class to implement a cache system
      - Learn the basis to cache algorithnms
    """

    def __init__(self):
        """
        CONSTRUCTOR
        """
        super().__init__()
        self.__last_update: str

    def put(self, key, item):
        """
        update the key in the cache data
        """

        def IsCacheFull() -> bool:
            if len(self.cache_data) == self.MAX_ITEMS:
                return True
            return False

        def IsNewKey(key):
            keys = [x for x in self.cache_data]
            if key in keys:
                return False
            return True

        def PopLast():
            self.cache_data.pop(self.__last_update)

        def AddToCache(key, item):
            self.cache_data.update({key: item})

        def UpdateLast(key):
            self.__last_update = key

        isFull: bool = IsCacheFull()
        isNew: bool = IsNewKey(key)
        if isFull:
            if isNew:
                print('DISCARD: {}'.format(self.__last_update))
                PopLast()

        AddToCache(key, item)
        UpdateLast(key)

    def get(self, key):
        """
        Return the valur from the given key if exists
        """
        return self.cache_data.get(key)
