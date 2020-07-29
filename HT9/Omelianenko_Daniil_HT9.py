import random
if __name__ == '__main__':
    player1 = input("Введите имя игрока №1: ")
    player2 = input("Введите имя игрока №2: ")
    result1 = []
    result2 = []
    for i in range(10):
        print(f'{player1} кидает кости. У вас осталось {10 - i} попыток! Нажмите любую кнопку чтобы кинуть кости: ', end='')
        input()
        random_number = random.randint(1, 12)
        print(random_number)
        print('')
        result1.append(random_number)
        print(f'{player2} кидает кости. У вас осталось {10 - i} попыток! Нажмите любую кнопку чтобы кинуть кости: ', end='')
        input()
        random_number2 = random.randint(1, 12)
        print(random_number2)
        print('')
        result2.append(random_number2)
        if random_number == random_number2:
            print('У игроков одинаковое число, перебрасываем кости!')
            continue
print(f'Числа игрока {player1}: {result1}, Общая сумма: {sum(result1)}')
print(f'Числа игрока {player2}: {result2}, Общая сумма: {sum(result2)}')
print()
if sum(result1) > sum(result2):
    print(f'Выиграл игрок {player1}')
elif sum(result1) == sum(result2):
    print(f'Ничья! Невероятно!!!')
else:
    print(f'Выиграл игрок {player2}')