# jsonapi

jsonapi is a Python package that provides custom serialization and deserialization for complex and range objects using the JSON format. It includes a custom JSONEncoder and JSONDecoder to handle serialization and deserialization of objects like complex numbers and range. This package is designed to extend the functionality of the standard json library in Python.

## Installation

You can install jsonapi using pip:
`pip install jsonapi`

## Serializing Data

To serialize complex or range objects, you can use the my_dumps function provided by jsonapi.

## Deserializing Data

To deserialize data with custom types, you can use the my_loads function provided by jsonapi.

## Custom Serialization

You can customize the serialization behavior for specific data types by extending the MyJSONEncoder class and overriding the default method.

## Custom Deserialization

For custom deserialization, you can extend the MyJSONDecoder class and provide a custom object_hook function to handle specific JSON structures.
