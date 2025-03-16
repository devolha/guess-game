import random

def guess_number_game(number):
    number = random.randint(1,10)
    print(f"Guess number is {number}")
    print()
    user_input = int(input('Lets play Guess Game! Enter a number between 1 and 10: '))

    
