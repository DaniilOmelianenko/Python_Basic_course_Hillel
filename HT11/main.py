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


run_machine_result = run_machine()



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
for i in run_machine_result:
    temp_list.setdefault(i, run_machine_result.count(i))
print(temp_list)

for key, value in temp_list.items():
    if key == 'XXX' and value == 1:
        xxx = 2
    else:
        xxx = 1

#############################
print(temp_list.values())
for key, value in temp_list.items():
    if value == 3:
        print(score_list[key][0])
    elif value == 2:
        print((score_list[key][1]) * xxx)