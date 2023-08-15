#!/usr/bin/python3


def class_to_json(obj):
    """Returns the dictionary description for
    JSON serialization of an object."""
    attributes = {}
    for key, value in obj.__dict__.items():
        if not callable(value) and not key.startswith("__"):
            attributes[key] = value
    return attributes


if __name__ == "__main__":
    MyClass = __import__('8-my_class').MyClass

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
