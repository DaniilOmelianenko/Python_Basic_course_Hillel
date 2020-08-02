number_of_months = input("Введите номер месяца: ")


def get_season(value1):
    if value1 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
        return 'Need to input valid month number!'
    elif value1 in ['12', '1', '2']:
        return "It's Winter!"
    elif value1 in ['3', '4', '5']:
        return "It's Spring!"
    elif value1 in ['6', '7', '8']:
        return "It's Summer!"
    elif value1 in ['9', '10', '11']:
        return "It's Fall!"


print(get_season(number_of_months))