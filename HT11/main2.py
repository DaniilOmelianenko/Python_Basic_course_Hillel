import random


def run_wheels():
    wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    result_list = [random.choice(wheel1), random.choice(wheel2), random.choice(wheel3)]
    print(result_list)

    temp_dict = {}
    for i in result_list:
        temp_dict.setdefault(i, result_list.count(i))

    for key, value in temp_dict.items():
        if key == 'XXX' and value == 1:
            xxx = 2
            break
        else:
            xxx = 1

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

    for key, value in temp_dict.items():
        if value == 3:
            return int(score_list[key][0])
        elif value == 2:
            return int((score_list[key][1]) * xxx)
    return 0


def check_your_luck():
    total_score = 0
    while True:
        combination = run_wheels()
        print(f'SCORE: {combination}')
        total_score += combination
        print(f'TOTAL: {total_score}')
        game = input('''        Do you want to continue?
        To continue game - press [y]
        To exit game     - press any key
        : ''')
        if game != 'y':
            break
        print('')
    print(f'''\nTOTAL SCORE: {total_score}
SEE YOU!''')


if __name__ == '__main__':
    check_your_luck()
