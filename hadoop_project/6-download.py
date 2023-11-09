#!/usr/bin/env python3
"""Task 5"""
from snakebite.client import Client


def download(l):
    """
    Retrieves from the HDFS files listed in `l`
    and stores them in the home /tmp folder of the user
    """
    client = Client("localhost", 9900)
    dest = '/tmp/'
    for x in client.copyToLocal(l, dest):
        print(x)


if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    download(l)
    lao = open("/tmp/lao.txt", "r")
    print(lao.read())
    lao.close()
