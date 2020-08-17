import random


def run_machine():
    wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    result_list = [random.choice(wheel1), random.choice(wheel2), random.choice(wheel3)]
    return result_list


#run_machine_result = ['A', 'C', 'B']
run_machine_result = run_machine()
print(run_machine_result)


def result_to_dict():
    temp_dict = {}
    for i in run_machine_result:
        temp_dict.setdefault(i, run_machine_result.count(i))
    return temp_dict


def x_x_x():
    for key, value in result_to_dict().items():
        if key == 'XXX' and value == 1:
            return 2
    return 1


def start_game():
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
    for key, value in result_to_dict().items():
        if value == 3:
            return score_list[key][0]
        elif value == 2:
            return (score_list[key][1]) * x_x_x()
    return 0


print(start_game())
