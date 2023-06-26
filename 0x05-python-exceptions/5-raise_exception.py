#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                quotient = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1):
                print("out of range")
            elif i >= len(my_list_2):
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(quotient)
    return result
def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as err:
        print(err)
        raise
