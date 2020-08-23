import random


def run_machine():
    wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    result_list = [random.choice(wheel1), random.choice(wheel2), random.choice(wheel3)]
    print(result_list)
    return result_list


#run_machine_result = run_machine()
print(run_machine())

def temp_list_func():
    temp_dict = {}
    for i in run_machine():
        temp_dict.setdefault(i, run_machine().count(i))
    return temp_dict


temp_list = temp_list_func()
print(f'temp list = {temp_list}')

def x_x_x():
    for key, value in temp_list.items():
        if key == 'XXX' and value == 1:
            print('xxx = 2')
            return 2
    return 1


def check_score():
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
    for key, value in temp_list.items():
        if value == 3:
            return int(score_list[key][0])
        elif value == 2:
            return int((score_list[key][1]) * x_x_x())
        else:
            return 0


def validate_game(string):
    if string == "1":
        return True
    elif string == "2":
        return False
    else:
        return None


def start_game():
    total_score = 0
    game = True
    while game is True:
        print(run_machine())
        game_round = int(check_score())
        print(check_score())
        total_score += game_round
        print(f"Счет: {game_round}\nОбщий счет: {total_score}\n")
        game = None
        while game == None:
            game = validate_game(input('''Нажмите "1", если хотите продолжить, или "2", если хотите завершить игру.
1 - Играть
2 - Завершить игру
: '''))
            print('')
    #else:
    print(f'''\nОбщий счет: {total_score}
До встречи!''')


if __name__ == '__main__':
    start_game()
