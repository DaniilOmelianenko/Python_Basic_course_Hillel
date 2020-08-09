def input_check():
    while True:
        try:
            player_select = int(input('Введите число: '))
            break
        except ValueError:
            print('Ошибка! Введите целое число!!!')
    return player_select