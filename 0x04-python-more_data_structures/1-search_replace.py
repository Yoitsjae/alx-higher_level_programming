#!/usr/bin/python3

from typing import List

def search_replace(my_list: List[int], search: int, replace: int) -> List[int]:
    new_list = [replace if num == search else num for num in my_list]
    return new_list
