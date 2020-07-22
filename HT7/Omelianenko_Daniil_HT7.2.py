def converter(string, delimiter):
    temp_list = string.split(delimiter)
    res_dict = dict.fromkeys(temp_list)
    return res_dict

my_string = input("Введите текст: ")
delimeter = input("Введите разделитель: ")
print(converter(my_string, delimeter))