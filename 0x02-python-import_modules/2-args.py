#!/usr/bin/python3
import sys

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
