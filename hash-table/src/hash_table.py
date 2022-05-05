from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Hashable, List, Optional


@dataclass
class HashValue:
    key: Hashable
    value: Any
    next_: Optional[HashValue]


class HashTable:
    _INITIAL_BUCKETS = 10
    _GROWTH_FACTOR = 2

    def __init__(self) -> None:
        self._buckets = self._INITIAL_BUCKETS
        self._data: List[Optional[HashValue]] = [None] * self._buckets
        self._colisions_count = 0

    def _get_data_index(self, key: Hashable) -> int:
        return abs(hash(key)) % self._buckets

    def _rebalance(self):
        if self._colisions_count < self._buckets:
            return

        self._buckets *= self._GROWTH_FACTOR

        keys = []
        values = []

        for init_ref in self._data:
            ref = init_ref
            while ref is not None:
                keys.append(ref.key)
                values.append(ref.value)

                ref = ref.next_

        old_cc_value = self._colisions_count

        self._data = [None] * self._buckets
        self._colisions_count = 0
        for k, v in zip(keys, values):
            self[k] = v

        print(
            f'Decreased from {old_cc_value} colisions to {self._colisions_count}')

    def __getitem__(self, key: Hashable):
        pos = self._get_data_index(key)

        ref = self._data[pos]

        while True:
            if ref is None:
                raise KeyError

            if ref.key == key:
                return ref.value

            ref = ref.next_

    def __setitem__(self, key: Hashable, value: Any):
        pos = self._get_data_index(key)

        ref = self._data[pos]
        if ref is None:
            self._data[pos] = HashValue(key, value, None)
        else:
            prev = None
            while ref is not None:
                if ref.key == key:
                    ref.value = value
                    return

                prev = ref
                ref = ref.next_

            prev.next_ = HashValue(key, value, None)

            self._colisions_count += 1
            self._rebalance()
