from input_check_start import input_check_start
from input_check_end import input_check_end
from input_check_delimeter import input_check_delimeter

print("Привет, эта программа покажет все, кратные N числа, в заданном диапазоне!")

value_a = input_check_start()
value_b = input_check_end()
value_c = input_check_delimeter()
value_d = (int(value_b) + 1)

print(f"Сейчас я покажу все числа, кратные {value_c}, в промежутке от {value_a} до {value_b}:")
print()

if __name__ == '__main__':
    def multiples():
        result = []
        for i in range(value_a, value_d):
            if (i % int(value_c)) != 0:
                continue
            elif i == 0:
                continue
            result.append(i)
        return result


print(multiples())
