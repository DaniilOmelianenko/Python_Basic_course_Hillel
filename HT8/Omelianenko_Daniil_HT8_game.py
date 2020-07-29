import random
print(f"Угадай число от 1 до 50")
number_of_attempts = 0
number = random.randint(1, 50)
max_attempts = 10
while number_of_attempts < max_attempts:
    print("Как ты думаешь, какое? ")
    guess = input()
    guess = int(guess)
    number_of_attempts += 1
    if guess < number:
        print("Мое число больше твоего")
    if guess > number:
        print("Мое число меньше твоего")
    if guess == number:
        break
if guess == number:
    print(f"Ты угадал число с {number_of_attempts} попытки")
if guess != number:
    #number = str(number)
    print(f"Последняя {max_attempts}-я попытка потрачена! Я загадал число {number}. Ты проиграл!")