import json

class Person:
     def __init__(self, name, age):
        self.name = name
        self.age = age


     def save_to_json(self, filename):
        data = {
        "name": self.name,
        "age": self.age
        }
        with open(filename, "w") as file:
            json.dump(data, file)


name = input("Name: ")
age = input("Age: ")
w = Person(name, age)
w.save_to_json('data_lab2.json')


with open('data_lab2.json') as f:
    templates = json.load(f)

print(templates)




