from src.hash_table import HashTable
import pytest


def test_creation():
    hash_table = HashTable()

    assert hash_table is not None


def test_insertion():
    hash_table = HashTable()

    hash_table['a'] = 'nothing'
    hash_table['b'] = 1

    with pytest.raises(TypeError):
        hash_table[[]] = 1


def test_retrieve():
    hash_table = HashTable()

    hash_table['a'] = 'nothing'

    assert hash_table['a'] == 'nothing'
