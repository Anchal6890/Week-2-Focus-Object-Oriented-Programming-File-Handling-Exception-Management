class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}"

student1 = Student("Aman", 101)
output = student1.display_info()
print(output)