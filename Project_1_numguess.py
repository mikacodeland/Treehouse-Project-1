import random


def start_game():
    print("***********************************************")
    print("Welcome to the number guessing game! Good luck!")
    print("***********************************************")
    print ("""GAME RULES:
                1. Pick a number between 1 and 10 until you guess the correct number
                2. If you get the number choose whether you want continue.
                3. TRY AND GET THE LOWEST SCORE!""")
    attempt = 0
    high_score = 0
    right_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Please choose a number between 1 and 10:  "))
            if guess <= 0 or guess > 10:
                raise ValueError ("Sorry that number is not in between 1 and 10. Try again.")
        except ValueError as err:
            print ("{}".format(err))

        if 11 > guess > right_number:
            attempt += 1
            print("Too high.  Go lower.")
            continue

        elif 0 < guess < right_number:
            attempt += 1
            print("Too low. Go higher.")
            continue

        elif guess == right_number:
            attempt += 1
            print("You got it! You finished in {} attempts.".format(attempt))
            print("The game will end now, unless you would like to play again.")
            print("Would you like to play again: Y/N")
            again = input("> ")
            if again.upper() == "Y":
                if high_score > attempt or high_score == 0:
                    high_score = attempt
                    print ("The HIGH SCORE so far is {}".format(high_score))
                    attempt = 0
                    continue
                else:
                    print("The HIGH SCORE so far is {}".format(high_score))
                    attempt = 0
                    continue

            elif again.upper() == "N":
                break




if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()