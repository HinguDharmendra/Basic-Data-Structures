"""
    file_name   :   hashmap.py
    version     :   12/05/2016 19:12, v1.0
    description :   This is HashMap class. It contains implementation of two hash functions
                    This is a referred code given by instructor in mycourses
"""
from collections import namedtuple

__author__ = ['Dharmendra Hingu (dph7305@g.rit.edu)', 'Kushal Gevaria (kgg5247@g,rit.edu']

Entry = namedtuple('Entry', ('key', 'value'))
'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class DeleteObject:
    pass


DELETED = Entry(DeleteObject(), None)


class HashMap:
    __slots__ = 'table', 'hash_function', 'number_of_keys', 'cap', 'max_load', 'collisions', 'probes'

    def __init__(self, hash_func, initsz=100, maxload=0.7):
        """
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        """
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.number_of_keys = 0
        self.max_load = maxload
        self.collisions = 0
        self.probes = 0
        self.hash_function = hash_func

    def put(self, key, value):
        """
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        """
        index = self.hash_function(key) % self.cap
        collision_flag = False
        while self.table[index] is not None \
                and self.table[index] != DELETED \
                and self.table[index].key != key:
            if collision_flag is False:
                self.collisions += 1
                collision_flag = True
            index += 1
            self.probes += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.number_of_keys += 1
        self.probes += 1
        self.table[index] = Entry(key, value)

        if self.number_of_keys / self.cap > self.max_load:
            # rehashing
            # self.collisions = 0
            # self.probes = 0
            old_table = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.number_of_keys = 0
            # put items in new table
            for entry in old_table:
                if entry is not None:
                    self.put(entry[0], entry[1])

    def remove(self, key):
        """
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        """
        index = self.hash_function(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            # self.probes += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            # self.probes += 1
            self.table[index] = DELETED

    def get(self, key):
        """
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        """
        index = self.hash_function(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            self.probes += 1
            return self.table[index].value
        else:
            self.probes += 1
            raise KeyError('Key ' + str(key) + ' not present')

    def __contains__(self, key):
        """
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        """
        index = self.hash_function(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            self.probes += 1
            index += 1
            if index == self.cap:
                index = 0
        else:
            self.probes += 1
        return self.table[index] is not None

    def get_probes(self):
        """
        This method is used to return the number of probes
        :return: total number of probes
        """
        return self.probes

    def get_collisions(self):
        """
        This method is used to return the number of collisions
        :return: total number of collisions
        """
        return self.collisions

    def get_stats(self):
        """
        This method is used to print total number of collisions and probes
        :return: None
        """
        print('Collisions :', self.collisions)
        print('Probe count:', self.probes)

    def print_map(self):
        """
        This method is used to print all the elements present in the hash table
        :return: None
        """
        for i in range(self.cap):
            print(str(i) + ": " + str(self.table[i]))


def test_map1():
    """
    This is a test method used to test one of the hash functions and all it's methods
    :return: None
    """
    dict_map = HashMap(hash_func=lambda x: len(x), initsz=5)
    dict_map.put('apple', 1)
    dict_map.put('banana', 2)
    dict_map.put('orange', 15)
    dict_map.print_map()
    print('apple?', 'apple' in dict_map)
    print('grape?', 'grape' in dict_map)
    print('orange = ', dict_map.get('orange'))

    print('--------- adding one more to force table resize ')
    dict_map.put('grape', 7)
    dict_map.print_map()

    print('--------- testing remove')
    dict_map.remove('apple')
    dict_map.print_map()
    print(dict_map.get('grape'))

    print('--------- testing add to a DELETED location')
    dict_map.put('peach', 16)
    dict_map.print_map()
    print(dict_map.get('grape'))
    dict_map.get_stats()


def test_map2():
    """
    This is a test method used to test one of the hash functions and all it's methods
    :return: None
    """
    dict_map = HashMap(hash_func=lambda string: sum([(ord(x) - 96) for x in string]), initsz=12)
    dict_map.put('lad', 2)
    dict_map.put('but', 32)
    dict_map.put('is', 43)
    dict_map.put('chin', 2)
    dict_map.put('be', 24)
    dict_map.put('fun', 235)
    dict_map.put('blab', 456)
    dict_map.put('too', 47)
    dict_map.print_map()
    dict_map.get_stats()


if __name__ == '__main__':
    test_map1()
    # test_map2()
