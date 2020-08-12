import random


def start_game():
    pass


def end_game():
    pass


def run_machine():
    wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]

    result_list = [random.choice(wheel1), random.choice(wheel2), random.choice(wheel3)]
    return result_list

print(run_machine())

score_list = {"XXX": (100, 10, 100),
              "A": (90, 9, 18),
              "B": (80, 8, 16),
              "C": (70, 7, 14),
              "D": (60, 6, 12),
              "E": (50, 5, 10),
              "F": (40, 4, 8),
              "G": (30, 3, 6),
              "H": (20, 2, 4),
              "I": (10, 1, 2)
              }

temp_list = {}
for i in run_machine():
    temp_list.setdefault(i, run_machine().count(i))
print(temp_list)