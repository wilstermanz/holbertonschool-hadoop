#!/usr/bin/env python3
"""Task 4"""
from snakebite.client import Client


def deletedir(l):
    """Deletes directories within HDFS"""
    client = Client("localhost", 9900)
    for x in client.rmdir(sorted(l, key=len, reverse=True)):
        print(x)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
