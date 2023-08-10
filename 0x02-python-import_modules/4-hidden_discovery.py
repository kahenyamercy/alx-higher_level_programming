#!/usr/bin/python3

import py_compile
import dis
import marshal

# Load the compiled module
with open("hidden_4.pyc", "rb") as file:
    code = marshal.load(file)

# Extract the names defined in the module
names = code.co_names

# Filter and print the names that do not start with '__'
for name in sorted(names):
    if not name.startswith("__"):
        print(name)
