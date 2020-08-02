print ( "Привет, эта программа покажет все, кратные N числа, в заданном диапазоне!" )
value_a = input("Делим числа от: ")
value_b = input("До: ")
value_c = input("На что делим, Кэп?: ")
value_d = (int(value_b) + 1)
print (f"Сейчас я покажу все числа, кратные {value_c}, в промежутке от {value_a} до {value_b}")
for i in range (int(value_a), int(value_d)):
    if (i % int(value_c)) != 0:
        continue;
    elif i == 0:
        continue;
    print(i)
