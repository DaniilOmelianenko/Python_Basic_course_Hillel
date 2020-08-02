def get_rectangle_data(value1):
    Full = f'''Площадь квадрата равняется: {value1 ** 2}
Периметр квадрата равняется: {value1 * 4}
Диагональ квадрата равняется: {(2 ** 0.5) * value1}'''
    return Full


while True:
    value1 = input("Введите длину стороны квадрата: ")
    try:
        value1 = float(value1)
        break
    except ValueError:
        print("Необходимо ввести ЧИСЛО!")
        print("")
print(get_rectangle_data(value1))