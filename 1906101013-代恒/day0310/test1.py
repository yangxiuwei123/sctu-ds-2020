class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_course(self):
        print(max(self.score))

a = Student('代恒',18,[105,104,123])
a.get_name()
a.get_age()
a.get_course()

