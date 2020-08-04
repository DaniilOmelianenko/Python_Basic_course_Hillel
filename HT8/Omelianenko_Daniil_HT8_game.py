import random
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
else:
    print(f"Последняя {max_attempts}-я попытка потрачена! Я загадал число {number}. Ты проиграл!")
