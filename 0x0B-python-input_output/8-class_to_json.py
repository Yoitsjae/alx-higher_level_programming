#!/usr/bin/env python3

import json

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json_string(self):
        return json.dumps(self.__dict__)

if __name__ == '__main__':
    student_1 = Student("John", "Doe", 20)
    s_student_1 = student_1.to_json_string()
    print(s_student_1)
    print(type(s_student_1))

    student_2 = Student("Jane", "Smith", 22)
    s_student_2 = student_2.to_json_string()
    print(s_student_2)
    print(type(s_student_2))
