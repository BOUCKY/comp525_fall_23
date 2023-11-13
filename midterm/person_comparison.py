"""
Create a Python class Person with attributes for a person's name and age. 
Implement a method to compare the ages of two people, returning a message that 
indicates who is older. For example, if person1 is 30 years old and person2 is 
25 years old, calling person1.compare_age(person2) should return 
"person1 is older."

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_comparison(self, other_person):
        """
        Take in two people's name and age and compare the two ages. Return the older person.
        :param self: string and integer
        :param other_person: string and integer
        :return: string
        time complexity: O(1)
        """
        if self.age > other_person.age:
            return f"{self.name} is older."
        elif self.age < other_person.age:
            return f"{other_person.name} is older."
        else:
            return f"{self.name} and {other_person.name} are of the same age."

person1 = Person("John", 30)
person2 = Person("Alice", 25)

result = person1.person_comparison(person2)
print(result)
