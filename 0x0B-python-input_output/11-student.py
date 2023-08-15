#!/usr/bin/python3


class Student:
    """Defines a student by first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__

        attributes = {}
        for attr in attrs:
            if hasattr(self, attr):
                attributes[attr] = getattr(self, attr)
        return attributes

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    import os
    import sys
    Student = __import__('11-student').Student
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(new_j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
