from dataclasses import dataclass
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name}, Student ID: {self.school_id} GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'abcdef', 3.6)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'zyxwvu', 3.7)
    print(sam)

    penelope = Student('Penelope', 'lmnopq', 3.2)
    print(penelope)

main()

#if __name__ == '__main__' =
 #   main()
 #


# Notes: dataclasses do not need getters and setters like (def set_name(self, name):
# dataclasses are more concise (need less code)
# Python can write code without objects (Java always needs them)

