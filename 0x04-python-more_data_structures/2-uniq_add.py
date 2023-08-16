#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_sum = 0
    unique_set = set()

    for num in my_list:
        if num not in unique_set:
            unique_sum += num
            unique_set.add(num)

    return unique_sum
