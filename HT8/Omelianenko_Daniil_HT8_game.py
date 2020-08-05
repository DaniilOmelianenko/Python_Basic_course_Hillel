import random
from datetime import datetime
import json


def write_last_try_data():
    last_try_data = {'Number': guess, 'Number of attempt': number_of_attempts, 'Updated': str(datetime.now())}
    with open("last_try.json", "w") as jsonfile:
        json.dump(last_try_data, jsonfile, indent=4)


print(f"Угадай число от 1 до 50")
number_of_attempts = 0
number = random.randint(1, 50)
max_attempts = 10
while number_of_attempts < max_attempts:
    number_of_attempts += 1
    print(f"{number_of_attempts}-я попытка. Как ты думаешь, какое? ")
    guess = input()
    guess = int(guess)
    if guess < number:
        print("Мое число больше твоего")
    elif guess > number:
        print("Мое число меньше твоего")
    elif guess == number:
        break
if guess == number:
    print(f"Ты угадал число с {number_of_attempts} попытки")
    write_last_try_data()
else:
    print(f"Последняя {max_attempts}-я попытка потрачена! Я загадал число {number}. Ты проиграл!")
