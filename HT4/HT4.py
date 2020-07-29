var_string = input("Введите фразу или слово: ")
vowels = 0
for i in var_string:
    if i in 'aeuioауоыиэяюёе':
        vowels +=1
print('')
print(f"В слове \"{var_string}\" количество гласных букв равняется: {vowels}")
print('')
print('''Программа завершена! 
Для продолжение работы запустите ее еще раз!''')