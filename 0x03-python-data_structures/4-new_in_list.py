#!/usr/bin/python3

from typing import List

def new_in_list(my_list: List[int], idx: int, element: int) -> List[int]:
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
