print ( "Привет, эта программа покажет все, кратные N числа, в заданном диапазоне!" )
a = input("Делим числа от: ")
b = input("До: ")
c = input("На что делим, Кэп?: ")
print (f"Сейчас я покажу все числа, кратные {c}, в промежутке от {a} до {b}")
i = int(a) - 1
while i <= int(b):
    if i < int(b):
        i += 1
        if (i % int(c)) != 0:
            continue;
        print (i)
    else:
        break