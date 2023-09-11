#!/usr/bin/python3

def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    result = []
    for attr_name in dir(obj):
        # Filter out attributes and methods inherited from 'object' class
        if not attr_name.startswith('__'):
            attr = getattr(obj, attr_name)
            # Check if the attribute is a method or a callable function
            if callable(attr):
                result.append(attr_name)
    return result

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))  # Check 0
    print(lookup(MyClass2))  # Check 1
    print(lookup(int))       # Check 2
    print(lookup([]))        # Check 3
