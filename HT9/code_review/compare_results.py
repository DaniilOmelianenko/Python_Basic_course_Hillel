def compare(player_select, random_number):
    if player_select == random_number:
        return 'Поздравляю!!!'
    elif player_select > random_number:
        return 'Твоё число БОЛЬШЕ моего! Попробуй снова!'
    elif player_select < random_number:
        return 'Твоё число МЕНЬШЕ моего! Попробуй снова!'
