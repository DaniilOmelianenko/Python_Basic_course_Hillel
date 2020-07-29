number = int(input("Введите число: "))
def is_prime(value):
    d = 2
    while d * d <= value and value % d != 0:
        d += 1
    return d * d > value
print(is_prime(number))