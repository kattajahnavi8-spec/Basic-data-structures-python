import random
def game():
    number = random.randint(1, 20)
    while True:
        guess = int(input("Enter Guess: "))
        if guess == number:
            print("Correct!")
            break
        elif guess < number:
            print("Too Small")
        else:
            print("Too Large")
game()