import random

def guess(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    while guessed_number != random_number:
        guessed_number =  int(input(f"Enter a number between 1 and {x}: " ))
        if guessed_number > random_number:
            print("opps! too big. Try agian.")
        elif guessed_number < random_number:
            print("Too small, try again son!")
    print("Yay! you guess the number successfully!")

guess(10) 