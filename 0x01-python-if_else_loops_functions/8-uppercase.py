#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper_char = chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        print("{}".format(upper_char), end='')
    print()
