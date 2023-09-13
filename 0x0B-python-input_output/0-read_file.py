#!/usr/bin/python3

def read_file(filename=""):
    # Your code to read and print the file content goes here
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    read_file()  # Call the function with no arguments for testing
