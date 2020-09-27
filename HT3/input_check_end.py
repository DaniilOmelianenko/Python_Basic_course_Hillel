def input_check_end():
    while True:
        try:
            value_b = int(input("\nДо: "))
            break
        except ValueError:
            print('Ошибка! Введите целое число!!!')
    return value_b
