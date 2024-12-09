## verifica se [e primo]
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
## Guess Number

import random as r
EASY_TRY = 10
HARD_TRY = 5

def check(guess, answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"Correct Answer: {answer}")

def set_difficult():
    level = input("Choose a difficult, 'easy' or 'hard': ").lower()
    if level == "hard":
        return  HARD_TRY
    else:
        return  EASY_TRY
           
rand_num = r.randint(1, 100)
print("Welcome to the number guess")
print("Im thinking aboutof a number between 1 and 100")
turns = set_difficult()

while turns > 0 :
    print(f"You have {turns} attemps to guess the number")
    guess = int(input("Whats number? "))
    check(guess=guess, answer=rand_num)
    if guess == rand_num:
        break
    turns -= 1
if turns == 0:
    print(f"You Lose, the correct answer was {rand_num}")