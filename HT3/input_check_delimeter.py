def input_check_delimeter():
    while True:
        try:
            value_c = int(input("\nНа что делим, Кэп?: "))
            if value_c != 0:
                break
            else:
                print('Нельзя делить на 0 !!!')
                continue
        except ValueError:
            print('Ошибка! Введите целое число!!!')
    return value_c
