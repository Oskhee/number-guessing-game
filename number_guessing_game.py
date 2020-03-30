import random


def generate_random_value(first_number, last_number):
    return random.randint(first_number, last_number)


def start_game():
    random_value = generate_random_value(1, 10)
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------\n")

    counter = 0
    condition = True
    while condition:
        print(random_value)
        try:
            user_input = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Oh no! Something went wrong, please try again!\n")
            continue
        counter += 1
        if user_input > random_value:
            print("It is lower!")
            continue
        elif user_input < random_value:
            print("It is higher!")
            continue
        else:
            print("\nYou got it! It took you {} tries.".format(counter))
            while True:
                play_again = input("\nWould you like to play again? (y/n): ")
                if play_again == 'n':
                    print("\nClosing game, see you next time!")
                    condition = False
                    break
                elif play_again == 'y':
                    print("\nThe highscore is {}".format(counter))
                    counter = 0
                    random_value = generate_random_value(1, 10)
                    break
                else:
                    print("Oh no! Something went wrong, please try again!\n")
                    continue


start_game()
