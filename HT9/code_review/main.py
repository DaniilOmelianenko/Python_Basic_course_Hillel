import random
from inputvalidate import input_check
from compare_results import compare


# СДЕЛАТЬ правильный вывод при выигрыше


def guess_the_number():
    print(f"Угадай число от 1 до 1000")
    random_number = random.randint(1, 10)
    number_of_attempts = 1
    for i in range(10):
        print(f'У вас {10 - i} попыток!')
        player_select = input_check()
        print(compare(player_select, random_number))
        if player_select == random_number:
            break
        number_of_attempts += 1
    if player_select == random_number:
        print(f"Ты угадал число с {number_of_attempts} попытки")
    else:
        print(f"Последняя 10-я попытка потрачена! Я загадал число {random_number}. Ты проиграл!")
    return player_select


if __name__ == '__main__':
    guess_the_number()


# SOURCE CODE
# import random
#
# y_n = 'yes'
# while y_n == 'yes':
#     random_number = random.randint(1, 1000)
#     for i in range(10):
#         print(f'У вас {10 - i} попыток!')
#         try:
#             player_select = int(input('Введите число:'))
#         except ValueError as err:
#             print('Error you number not correct!')
#             y_n = 'error'
#             break
#         if player_select == random_number:
#             print('You win!!!!')
#             y_n = input('Хотите прожолжить?[yes/no]')
#             break
#         elif player_select > random_number:
#             print('Вваше число больше')
#         elif player_select < random_number:
#             print('Вваше число Меньше')
