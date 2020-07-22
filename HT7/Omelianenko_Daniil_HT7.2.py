def converter(string, delimiter):
    temp_list = {}
    for i in string.split(delimiter):
        temp_list.setdefault(i, string.split(delimiter). count(i))
    return temp_list

my_string = input("Введите текст: ")
delimeter = input("Введите разделитель: ")
if delimeter == "":
    delimeter = None
print(converter(my_string, delimeter))