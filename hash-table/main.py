from pprint import pprint
from string import printable

from src.hash_table import HashTable

hash_table = HashTable()

for k, letter in enumerate(range(1000)):
    hash_table[letter] = k


# pprint(hash_table._data)
# print(hash_table._colisions_count)

# print(hash_table['a'])