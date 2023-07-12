#!/usr/bin/python3

import json

def to_dictionary(json_string):
    return json.loads(json_string)

if __name__ == '__main__':
    s_student_1 = '{"first_name": "John", "last_name": "Doe", "age": 20}'
    student_1_dict = to_dictionary(s_student_1)
    print(student_1_dict)
    print(type(student_1_dict))

    s_student_2 = '{"first_name": "Jane", "last_name": "Smith", "age": 22}'
    student_2_dict = to_dictionary(s_student_2)
    print(student_2_dict)
    print(type(student_2_dict))

    try:
        s_invalid_json = '{"first_name": "Jack", "last_name": "Brown", "age"}'
        invalid_dict = to_dictionary(s_invalid_json)
        print(invalid_dict)
        print(type(invalid_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
