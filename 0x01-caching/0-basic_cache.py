#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """ BaseCaching:
      - Simple class to implement a cache system
      - Learn the basis to cache algorithnms
    """

    def __init__(self):
        """ 
        CONSTRUCTOR 
        """
        super().__init__()

    def put(self, key, item):
        """
        update the key in the cache data
        """
        if key is not None:
            self.cache_data.update({key: item})
        else:
            pass

    def get(self, key):
        """
        Return the valur from the given key if exists
        """
        return (self.cache_data.get(key))
