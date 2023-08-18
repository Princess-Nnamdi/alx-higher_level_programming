#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout."""
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents, end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
