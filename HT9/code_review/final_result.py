def final_result(player_select, random_number):
    from main import number_of_attempts
    if player_select == random_number:
        if number_of_attempts == 1:
            result = f'''Ты угадал число с {number_of_attempts} попытки!!!
Невероятно! Такого еще никто не делал!!!'''
        elif number_of_attempts in range(2, 9):
            result = f'''Ты угадал число с {number_of_attempts} попытки!!!
Я видал игроков и получше!!!'''
        elif number_of_attempts == 10:
            result = f'''Ты угадал число с {number_of_attempts} попытки!!!
Ты был на волоске от проигрыша'''
    else:
        result = f"Последняя 10-я попытка потрачена! Я загадал число {random_number}. Ты проиграл!"
    return result
