from fatherclass import Human
class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)

    def get_name(self):
        super(Student, self).get_name()
        print(self.name)

student1 = Student("光明路小学", "石敢当", 18)
print(student1.name)
print(student1.age)
student1.get_name()