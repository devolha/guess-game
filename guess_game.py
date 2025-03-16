def get_user_guess():
    import random
    number = random.randint(1,10)
    print(f"Comment: Guess number is {number}")
    print()
    user_input = int(input("Let's play Number Guess Game! Enter a number from 1 to 10: "))
    return number, user_input

    
get_user_guess()
