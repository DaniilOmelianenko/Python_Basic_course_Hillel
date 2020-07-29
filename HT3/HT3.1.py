print ( "Привет, эта программа покажет все, кратные N числа, в заданном диапазоне!" )
a = input("Делим числа от: ")
b = input("До: ")
c = input("На что делим, Кэп?: ")
d = (int(b) + 1)
print (f"Сейчас я покажу все числа, кратные {c}, в промежутке от {a} до {b}")
for i in range (int(a), int(d)):
    if (i % int(c)) != 0:
        continue;
    elif i == 0:
        continue;
    print(i)