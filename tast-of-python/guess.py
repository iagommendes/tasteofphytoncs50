import random

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("try a guess: "))
    print("guess left")
    if guess == number:
        print("YOU GOT IT!!")
    elif guess > number:
        print("too high!")
    else:
        print("too low!")
        break
print("the secret number was: ")
print(number)

