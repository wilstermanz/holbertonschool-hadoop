#!/usr/bin/env python3
"""Task 3"""
from snakebite.client import Client


def createdir(l):
    """Creates directories listed in l"""
    client = Client("localhost", 9900)
    for x in client.mkdir(l):
        print(x)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
