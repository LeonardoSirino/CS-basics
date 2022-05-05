from typing import Any, Hashable


class HashTable:
    def __init__(self) -> None:
        pass

    def __getitem__(self, index: Hashable):
        raise NotImplementedError

    def __setitem__(self, index: Hashable, value: Any):
        raise NotImplementedError
