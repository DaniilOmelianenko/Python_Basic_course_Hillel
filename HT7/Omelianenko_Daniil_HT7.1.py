for number_of_months in range(1, 12):
    number_of_months = input("Please input month number: ")
    if number_of_months not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
        print("Необходимо ввести число от 1 до 12 !!!")
        print("")
        continue
    else:
        number_of_months = int(number_of_months)
        break

def get_season(value1):
    if value1 in [12, 1, 2]:
        return "It's Winter!"
    elif value1 in [3,4,5]:
        return "It's Spring!"
    elif value1 in [6,7,8]:
        return "It's Summer!"
    elif value1 in [9, 10, 11]:
        return "It's Fall!"
print(get_season(number_of_months))