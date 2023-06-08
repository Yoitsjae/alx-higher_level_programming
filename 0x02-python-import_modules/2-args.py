#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argc))

        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
