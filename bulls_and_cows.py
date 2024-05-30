"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Hana Stříbrná
email: stribrna.hana@gmail.com
discord: Hanka0531
"""

import random

def greet_user():
    print(
        "Hi there!","\n",
        "-" * 47,"\n"
        "I've generated a random 4 digit number for you.","\n"
        "Let's play a bulls and cows game.","\n",
        "-" * 47
        )

def generate_secret_number():
    digits = list("123456789")
    random.shuffle(digits)
    secret_number = ''.join(digits[:4])
    #print (secret_number)
    return secret_number
    
def validate_input(user_input):
    if len(user_input) != 4:
        print("The number must be exactly 4 digits long.")
        return False
    if not user_input.isdigit():
        print("The number must consist of digits only.")
        return False
    if user_input[0] == '0':
        print("The number must not start with a zero.")
        return False
    if len(set(user_input)) != 4:
        print("The digits must be unique.")
        return False
    return True

def calculate_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    for i in range(len(secret)):
        if guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    return bulls, cows

def print_bulls_and_cows(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    print("-" * 47)

def main():
    greet_user()
    secret_number = generate_secret_number()
    guess_count = 0

    while True:
        guess = input("Enter a number:\n" + "-" * 47 + "\n>>> ")
        if not validate_input(guess):
            continue
        guess_count += 1
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guess_count} guesses!")
            if guess_count <= 5:
                print("That's amazing!")
            elif guess_count <= 10:
                print("That's average.")
            else:
                print("That's not so good.")
            break
        else:
            print_bulls_and_cows(bulls, cows)

if __name__ == "__main__":
    main()
