#!/usr/bin/python3.8
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]
    filtered_names.sort()

    for name in filtered_names:
        print(name)
