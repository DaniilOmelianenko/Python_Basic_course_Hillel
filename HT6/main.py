if __name__ == '__main__':
    while True:
        value1 = input ( "Введите Первое число: " )
        try:
            value1 = float(value1)
            break
        except ValueError:
            print ("Необходимо ввести ЧИСЛО!")
            print("")
    print("")
    while True:
        value2 = input ( "Введите Второе число: " )
        try:
            value2 = float(value2)
            break
        except ValueError:
            print ("Необходимо ввести ЧИСЛО!")
            print("")
    print("")
    while True:
        sign = input( '''Нажмите кнопку, которая соответствует требуемому действию:
        1) +
        2) -
        3) *
        4) /
        :''' )
        if sign in ['+', '-', '*', '/', '1', '2', '3', '4']:
            break
        else:
            print ("Введите знак или цифру соответствующую знаку!")
            continue
    print("")
    if sign == '+' or sign == '1':
        from add import add
        add(value1, value2)
    elif sign == '-' or sign == '2':
        from subtraction import subtraction
        subtraction(value1, value2)
    elif sign == '*' or sign == '3':
        from multiply import multiply
        multiply(value1, value2)
    elif sign == '/' or sign == '4':
        from divide import divide
        divide(value1, value2)