from roll_the_dice import roll


while True:
    player1 = input("Введите имя игрока №1: ")
    player2 = input("Введите имя игрока №2: ")
    if player1 != player2:
        break
    else:
        print('Имена не могу быть одинаковыми! Введите имена заново!')

result1 = []
result2 = []
counter = 1

while counter <= 10:
    print(f'{player1} кидает кости. Бросок № {counter}! Нажмите любую кнопку чтобы кинуть кости: ', end='')
    input()
    random_number = roll()
    print(f"На костях выпало число {random_number}!")
    print('')
    print(f'{player2} кидает кости. Бросок № {counter}! Нажмите любую кнопку чтобы кинуть кости: ', end='')
    input()
    random_number2 = roll()
    print(f"На костях выпало число {random_number2}!")
    print('')
    if random_number == random_number2:
        print('У игроков одинаковое число, перебрасываем кости!')
        continue
    else:
        counter += 1
        result1.append(random_number)
        result2.append(random_number2)

print(f'Числа игрока {player1}: {result1}, Общая сумма: {sum(result1)}')
print(f'Числа игрока {player2}: {result2}, Общая сумма: {sum(result2)}')
print()
if sum(result1) > sum(result2):
    print(f'Выиграл игрок {player1}')
elif sum(result1) == sum(result2):
    print(f'Ничья! Невероятно!!!')
else:
    print(f'Выиграл игрок {player2}')
