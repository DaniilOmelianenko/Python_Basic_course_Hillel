print('     Действие первое. Читаем файл, выводи на экран содержание:')
with open('HT8.1.txt', 'r') as Myfile:
    print(Myfile.read())

print('')
print('     Действие второе. Читаем предыдущий файл, пишем его содержимое в новый файл, и выводим на экран:')
with open('HT8.1.txt', 'r') as Myfile, open('HT8.2.txt', 'w') as Myfile2:
    data = Myfile.read()
    Myfile2.write(data)
with open('HT8.2.txt', 'r') as Myfile2:
    print(Myfile2.read())

print('')
print('     Действие третье. Читаем файл, изменяем и выводим на экран его новое содержание:')
with open('HT8.1.txt', 'w+') as Myfile:
    write_data = input('Введи новые данные: ')
    Myfile.write(write_data)
with open('HT8.1.txt', 'r') as Myfile:
    print(Myfile.read())