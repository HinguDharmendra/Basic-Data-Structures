"""
    file_name   :   insthashable.py
    version     :   12/05/2016 19:12, v1.0
    description :   This file contains DictionaryTable class. It contains implementation of two hash functions
"""
import re
from collections import namedtuple

from hashmap import HashMap

Entry = namedtuple('Entry', ('key', 'value'))


class DictionaryTable:
    __slots__ = 'hash_table'

    def __init__(self, hash_function, initial_size=10, max_load_factor=0.7):
        """
        This function is used to initialize the hashtable based on the hashfunction provided with a certain load factor
        which is used to increase the size of the hash table
        :param hash_function: a particular hash value calculating function
        :param initial_size: initial size of the table
        :param max_load_factor: loac factor for a table
        """
        self.hash_table = HashMap(initsz=initial_size, hash_func=hash_function, maxload=max_load_factor)

    def process_file(self, file_name):
        """
        This function is used to take input of words from the file with a provided filename
        :param file_name: name of the file along with the extension
        :return: None
        """
        with open(file_name) as file_pointer:
            for each_line in file_pointer:
                each_line = each_line.strip()
                list_of_words = re.split('\W+', each_line)
                for word in list_of_words:
                    if len(word) > 0:
                        self.count_frequency(word.lower())

    def count_frequency(self, word):
        """
        This function is used to keep the count of repetative words given in a particular file
        :param word: current word to check the count of
        :return: None
        """
        try:
            self.hash_table.put(word, self.hash_table.get(word) + 1)
        except KeyError:
            self.hash_table.put(word, 1)

    def print_hash_table(self):
        """
        This function is used to make a call to the print_map function print the entire hash table
        :return: None
        """
        self.hash_table.print_map()

    def get_max_occurred_word(self):
        """
        This method is used to return the word with maximum count
        :return: word which occured maximum time in a particular file
        """
        element = Entry(None, 0)
        for named_tuple in self.hash_table.table:
            if named_tuple is not None:
                if named_tuple.value > element.value:
                    element = named_tuple
        return element


def hash_function_ex_or(key):
    """
    This is a hash function which calculates the hash value for a key using XOR method.
    :param key: particular word from the file
    :return: hash value for that key(word)
    """
    prime_number = 1709
    result = 0
    for index in range(len(key)):
        result ^= (ord(key[index])) * (prime_number ** index) + len(key)
    return result


def hash_function_prime(key):
    """
    This is a hash function which calculates the hash value for a key using a particular prime number to
    generate a randam hash value
    :param key: particular word from the file
    :return: hash value for that key(word)
    """
    prime_number = 1709
    result = 0
    for index in range(len(key)):
        result += ((ord(key[index]) - 96) ** len(key)) * prime_number
    return result


def test_builtin(file_name, initial_table_size, load_factor):
    """
    This method is used to test the python's built in hash function
    :param file_name: name of the file
    :param initial_table_size: initial size of the table
    :param load_factor: load factor used for rehashing the table
    :return: None
    """
    print('\nTesting with load factor of', load_factor)
    dictionary = DictionaryTable(hash_function=lambda x: hash(x),
                                 initial_size=initial_table_size,
                                 max_load_factor=load_factor)
    dictionary.process_file(file_name)
    dictionary.hash_table.get_stats()
    element = dictionary.get_max_occurred_word()
    print_max(element)


def test_hash_function_ex_or(file_name, initial_table_size, load_factor):
    """
    This method is used to test user defined XOR hash function
    :param file_name: name of the file
    :param initial_table_size: initial size of the table
    :param load_factor: load factor used for rehashing the table
    :return: None
    """
    print('\nTesting with load factor of', load_factor)
    dictionary = DictionaryTable(hash_function=hash_function_ex_or,
                                 initial_size=initial_table_size,
                                 max_load_factor=load_factor)
    dictionary.process_file(file_name)
    dictionary.hash_table.get_stats()
    element = dictionary.get_max_occurred_word()
    print_max(element)


def test_hash_function_prime(file_name, initial_table_size, load_factor):
    """
    This method is used to test user defined prime hash function
    :param file_name: name of the file
    :param initial_table_size: initial size of the table
    :param load_factor: load factor used for rehashing the table
    :return: None
    """
    print('\nTesting with load factor of', load_factor)
    dictionary = DictionaryTable(hash_function=hash_function_prime,
                                 initial_size=initial_table_size,
                                 max_load_factor=load_factor)
    dictionary.process_file(file_name)
    dictionary.hash_table.get_stats()
    element = dictionary.get_max_occurred_word()
    print_max(element)


def print_max(element):
    """
    This method is used to print out the word which occurred maximum times is a particular file
    :param element: word in a file with maximum occurrence
    :return:
    """
    print('The word "', element.key, '" has appeared', element.value, 'times')


def test_hash_table():
    """
    This method is used to take the input of the file name and make a call to each and every test functions
    :return: None
    """
    file_name = input("Enter the file name: ")
    initial_table_size = 100
    '''
    dictionary = InstantiateHashTable(hash_function=lambda x: len(x), initial_size=100)
    dictionary = InstantiateHashTable(hash_function=lambda string: sum([(ord(x) - 96) for x in string]),
                                     initial_size=100)
    dictionary = InstantiateHashTable(hash_function=lambda string: sum([ord(x) for x in string]),
                                     initial_size=100)
    '''
    print()
    print(' ***** Python in-built hash function results: ***** ')

    load_factor = 0.7
    test_builtin(file_name, initial_table_size, load_factor)

    load_factor += 0.2
    test_builtin(file_name, initial_table_size, load_factor)

    print()
    print(' ***** Hash function involving ex-or results: ***** ')

    load_factor = 0.7
    test_hash_function_ex_or(file_name, initial_table_size, load_factor)

    load_factor += 0.2
    test_hash_function_ex_or(file_name, initial_table_size, load_factor)

    print()
    print(' ***** Hash function involving prime number multiplication results: ***** ')

    load_factor = 0.7
    test_hash_function_prime(file_name, initial_table_size, load_factor)

    load_factor += 0.2
    test_hash_function_prime(file_name, initial_table_size, load_factor)


if __name__ == '__main__':
    test_hash_table()
