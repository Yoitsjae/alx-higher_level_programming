#!/usr/bin/env python3

import json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json_string(self):
        return json.dumps(self.__dict__)

    def save_to_json_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.to_json_string())

    def update_from_json_string(self, json_string):
        data = json.loads(json_string)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']


if __name__ == '__main__':
    student = Student("John", "Doe", 20)
    student.save_to_json_file("student.json")

    # Update student from JSON string
    json_string = '{"first_name": "Jane", "last_name": "Smith", "age": 22}'
    student.update_from_json_string(json_string)
    print(student.first_name)
    print(student.last_name)
    print(student.age)
