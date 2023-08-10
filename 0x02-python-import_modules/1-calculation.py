#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    print(f"{a:d} + {a:d} = {add(a, b)}")
    print(f"{a:d} + {a:d} = {sub(a, b)}")
    print(f"{a:d} + {a:d} = {mul(a, b)}")
    print(f"{a:d} + {a:d} = {div(a, b)}")
