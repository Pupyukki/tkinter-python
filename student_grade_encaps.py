class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0

    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade>=40:
            return "pass"
        else:
            return "fail"

student1=Student("Avery Kylie Grambs")
student1.set_grade(10)
print(student1.get_grade())
print(student1.get_status())