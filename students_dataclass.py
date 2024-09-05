from dataclasses import dataclass
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

# put output in most readable format for humans using __str__:
    def __str__(self):
        return f'Name: {self.name}, Student ID: {self.school_id} GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'abcdef', 3.6)
    # print(alex.name)
    # print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'zyxwvu', 3.7)
    print(sam)

    penelope = Student('Penelope', 'lmnopq', 3.2)
    print(penelope)

main()

#if __name__ == '__main__' =
 #   main()
 #


# Notes: creating student Objects- no need for getters and setters
# dataclasses are :
        # more concise (need less code)
        # remove a lot of the boilerplate from class definitions
        # generates __init__ and __str__ automatically
# Python can write code without objects (Java always needs them)

