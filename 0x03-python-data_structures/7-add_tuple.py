#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to a length of 2 by padding with 0 if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add corresponding elements from the tuples
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    return sum_1, sum_2
