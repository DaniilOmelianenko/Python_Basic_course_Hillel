class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []

    def add_score(self, value):
        self.scores.append(value)
        return self.scores

    def average_score(self):
        average_score = 0
        count = 0
        for i in self.scores:
            average_score += i
            count += 1
        if average_score or count != 0:
            return average_score / count


class Group:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def group_update(self, student):
        action = input(f'''Input + to add {student} to the group
Input - to remove {student} from the group
: ''')
        if action == '+':
            if student not in self.students:
                self.students[student] = student.average_score()
            else:
                raise ValueError(f'''{student} already exist in {self.name}''')
        elif action == '-':
            if student in self.students:
                self.students.pop(student)
            else:
                raise ValueError(f'''{student} does not exist in {self.name}''')
        return self.students


danil = Student('Daniil', 29)
vetalik = Student('Vetaliy', 23)
print(danil.name, danil.age)
danil.add_score(8)
danil.add_score(5)
danil.add_score(2)
danil.add_score(25)
vetalik.add_score(100)
print(danil.scores)
print(danil.average_score())
print(vetalik.name, vetalik.age)
print(vetalik.scores)
print(vetalik.average_score())
group_a = Group('Group A')
print(group_a.name)
group_a.group_update(danil)
group_a.group_update(vetalik)
print(group_a.students)
group_a.group_update(vetalik)
print(group_a.students)
