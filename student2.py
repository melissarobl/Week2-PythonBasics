from dataclasses import dataclass
@dataclass
class Student:
    name: str
    college_id: int

def main():

    alice = Student('Alice', 12345)
    bob = Student('Bob', 12345)

    print(alice)
    print(bob)

main()
