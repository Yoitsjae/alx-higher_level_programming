#!/usr/bin/python3

def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

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
    print(lookup([]))        # Check 33
