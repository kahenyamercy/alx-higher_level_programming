#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

a = 10
b = 5

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

if __name__ == "__main__":
    operations = [
        ("+", result_add),
        ("-", result_sub),
        ("*", result_mul),
        ("/", result_div)
    ]

    for operator, result in operations:
        print(f"{a} {operator} {b} = {result}")

    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    if argc == 0:
        print("Number of argument(s): 0.")
    else:
        plural = "s" if argc > 1 else ""
        print(f"Number of argument(s): {argc}, argument{plural}:",
              end="\n" if argc == 1 else "s:\n")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
