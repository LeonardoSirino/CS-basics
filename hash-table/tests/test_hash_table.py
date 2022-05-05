from src.hash_table import HashTable


def test_creation():
    hash_table = HashTable()

    assert hash_table is not None


def test_insertion():
    hash_table = HashTable()

    hash_table['a'] = 'nothing'
    hash_table['b'] = 1
    hash_table[[]] = 1
