def input_check_start():
    while True:
        try:
            value_a = int(input("Делим числа от: "))
            break
        except ValueError:
            print('Ошибка! Введите целое число!!!')
    return value_a
