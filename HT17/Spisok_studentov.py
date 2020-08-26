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
        return average_score / count


class Group:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.students_count = 0
        self.group_scores =

    def group_update(self, student): #dobavlenie studenta
        self.students[1] = student
        return self.students

    def show_st(self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{index + 1}) {st.name}\tage:{st.age}")

    def show_grades(self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}\n{'-' * 17}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{st.check_grades()}")




danil = Student('Daniil', 29)
print(danil.name, danil.age)
danil.add_score(8)
danil.add_score(5)
danil.add_score(2)
danil.add_score(25)
print(danil.scores)
print(danil.average_score())
group_a = Group('Group A')
print(group_a.name)
group_a.group_update(danil)
print(group_a.students)

# # Initial Data
# st_1 = Student("Howard", 20)
# st_2 = Student("Harry", 19)
#
# st_1.add_mark("Math", 9)
# st_1.add_mark("Math", 11)
# st_1.add_mark("Math", 12)
# st_1.add_mark("Physics", 9)
# st_2.add_mark("Math", 10)
#
# group = Group("INTRO")
# group.group_upd(st_1)
# group.group_upd(st_2)
#
# # Main
# print("Menu:")
# while True:
#     print("Select group:")
#     print(f"1) {group.name}")
#     try:
#         selected_group = int(input("Input: "))
#     except ValueError:
#         break
#
#     selected_group = group   # Just 1 var
#     while True:
#         print("\nSelect variant:")
#         print("1) Show list of students")
#         print("2) Check grades")
#         try:
#             select_var = int(input("Input: "))
#         except ValueError:
#             break
#         if select_var == 1:
#             selected_group.show_st()
#         if select_var == 2:
#             selected_group.show_grades()