def get_user_guess():
    import random
    guess_number = random.randint(1,10)
    print(f"Comment: Guess number is {guess_number}")
    print()
    user_input = int(input("Let's play Number Guess Game! Enter a number from 1 to 10: "))
    return guess_number, user_input


    
get_user_guess()
