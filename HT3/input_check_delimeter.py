def input_check_delimeter():
    while True:
        try:
            value_c = int(input("На что делим, Кэп?: "))
            break
        except ValueError:
            print('Ошибка! Введите целое число!!!')
    return value_c
