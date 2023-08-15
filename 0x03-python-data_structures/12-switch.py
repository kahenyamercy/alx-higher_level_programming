#!/usr/bin/python3
a = 89
b = 10

# Switch the values of a and b using a temporary variable
temp = a
a = b
b = temp

print("a={:d} - b={:d}".format(a, b))
