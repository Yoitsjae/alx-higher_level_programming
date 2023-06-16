#!/usr/bin/python3

from typing import List

def uniq_add(my_list: List[int]) -> int:
    unique_sum = sum(set(my_list))
    return unique_sum
