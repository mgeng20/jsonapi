import json

from src.jsonapi.jsonapi import my_dumps, my_loads


data1 = {
    "integer": 42,
    "string": "Hello, World!",
    "complex": 3 + 4j,
    "list": [1, 2, 3],
    "range": range(1, 10, 2),
    "nested": {
        "key1": "value1",
        "key2": "value2"
    }
}


data2 = {
    "integer": 20,
    "string": "abc",
    "complex": complex(1, 2),
    "list": [0, 9, 10],
    "nested": {
        "key1": "value1",
        "key2": "value2"
    },
    "boolean": True,
    "range": range(0, 5)
}


def test_loads():
    deserialized_data1 = my_loads(my_dumps(data1))
    assert deserialized_data1 == data1
    deserialized_data2 = my_loads(my_dumps(data2))
    assert deserialized_data2 == data2
