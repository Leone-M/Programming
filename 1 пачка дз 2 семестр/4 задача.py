class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)



class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)




class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

    def enrol(self, course):
        try:
            self.learner.enrol(course)
        except AttributeError:
            print("Learner delegation isn't preformed")

    def assign_teaching(self, course):
        try:
            self.courses_taught.append(course)
        except AttributeError:
            print("Teacher delegation isn't preformed")


jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.learner.enrol("a_postgrad_course")
jane.teacher.assign_teaching("an_undergrad_course")