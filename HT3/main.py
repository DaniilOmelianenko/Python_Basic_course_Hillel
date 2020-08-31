from input_check_start import input_check_start
from input_check_end import input_check_end
from input_check_delimeter import input_check_delimeter

print("Привет, эта программа покажет все, кратные N числа, в заданном диапазоне!")
start_int = int(input_check_start())
finish_int = int(input_check_end())
delimeter = int(input_check_delimeter())
print(f'''\n{'='*100}''')
print(f"Сейчас я покажу все числа, кратные {delimeter}, в промежутке от {start_int} до {finish_int}:")

if __name__ == '__main__':
    def multiples(start, finish, delim):
        while start % delimeter:
            start += 1
        return list(range(start, finish+1, delim))


print(multiples(start_int, finish_int, delimeter))
