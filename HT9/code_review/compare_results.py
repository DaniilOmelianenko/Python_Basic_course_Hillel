def compare(player_select, random_number):
    if player_select == random_number:
        result = 'Ты угадал моё число!'
    elif player_select > random_number:
        result = 'Твоё число БОЛЬШЕ моего! Попробуй снова!'
    elif player_select < random_number:
        result = 'Твоё число МЕНЬШЕ моего! Попробуй снова!'
    return result

