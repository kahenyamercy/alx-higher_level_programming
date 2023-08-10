#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def usage_and_exit():
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)


if len(sys.argv) != 4:
    usage_and_exit()

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)
else:
    print("Unknown operator")
    usage_and_exit()

print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
