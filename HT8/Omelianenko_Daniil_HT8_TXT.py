print('     Действие первое. Читаем файл, выводи на экран содержание:')
with open('HT8.1.txt', 'r') as my_file:
    print(my_file.read())

print('')
print('     Действие второе. Читаем предыдущий файл, пишем его содержимое в новый файл, и выводим на экран:')
with open('HT8.1.txt', 'r') as my_file, open('HT8.2.txt', 'w') as my_file2:
    data = my_file.read()
    my_file2.write(data)
with open('HT8.2.txt', 'r') as my_file2:
    print(my_file2.read())

print('')
print('     Действие третье. Читаем файл, изменяем и выводим на экран его новое содержание:')
with open('HT8.1.txt', 'w+') as my_file:
    write_data = input('Введи новые данные: ')
    my_file.write(write_data)
with open('HT8.1.txt', 'r') as my_file:
    print(my_file.read())
