from random import randint

def get_user_guess():
    guess_number = randint(1,10)
    return guess_number

guess_number = get_user_guess()
print(f"Let's play a Number Guess Game!")

while True:
    try:
        user_input = int(input("Enter a number from 1 to 10:"))
        if user_input not in range(1,11):
            print('Please enter a number between 1 and 10.')
        elif user_input == guess_number:
            print(f'Congratulations! It was {guess_number}!')
            break
        elif user_input < guess_number:
            print('Your number is lower than needed. Try one more time.')
        elif user_input > guess_number:
            print('Your number is higher than needed. Try one more time.')
    except (ValueError, SyntaxError, NameError):
        print("It's not a number. Try one more time!")
  
