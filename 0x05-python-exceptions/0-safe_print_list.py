#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i range(x):
            print(my_list[i], end='')
            element_printed += 1
    except IndexError:
        pass

    print()
    return element_printed
