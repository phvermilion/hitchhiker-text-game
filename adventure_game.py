import time
import random


def print_pause(words):
    print(words)
    time.sleep(2)


def intro():
    print_pause("It's dark and you find yourself alone, on the side of the "
                "road with an empty gas tank and no cell service.")
    print_pause("You can either hitchhike or walk to the nearest gas station "
                "for help.")


def make_choice():
    choice = input("Enter 1 to hitchhike.\n"
                   "Enter 2 to walk to the nearest gas station.\n")
    if choice == "1":
        hitchhike()
    elif choice == "2":
        walk()
    else:
        print_pause("Please enter 1 or 2\n")
        make_choice()


def hitchhike():
    print_pause("You raise your arm and stick your thumb up.")
    driver1 = "Driver passes you by. What would you like to do?"
    driver2 = "A driver slows down and stops on the side of the road."
    random_driver = random.choice([driver1, driver2])
    if random_driver == driver1:
        print_pause(driver1)
        make_choice()
    if random_driver == driver2:
        print_pause(driver2)
        hitchhike_choice()


def hitchhike_choice():
    print_pause("You walk up to the car and the driver offers you a lift.")
    insane_driver = ("After a while you realize the driver has passed 3 gas "
                     "stations. He takes you to an abandon shed and kills "
                     "you.")
    sane_driver = ("The driver takes you to the nearest gas station. Helps "
                   "you get a can of gas and takes you back to your car.")
    h_choice = input("Enter 1 you get in.\n" "Enter 2 chicken out.\n")
    if h_choice == "1":
        print_pause("You thank the driver and get in.")
        driver = random.choice([insane_driver, sane_driver])
        if driver == insane_driver:
            print_pause(insane_driver)
            print_pause("You are dead.")
            play_again()
        if driver == sane_driver:
            print_pause(sane_driver)
            play_again()
    elif h_choice == "2":
        print_pause("You thank the driver, but tell them you're actaully "
                    "okay. The driver leaves.")
        make_choice()
    else:
        print_pause("Please enter 1 or 2 \n")
        hitchhike_choice()


def walk():
    print_pause("You lock your car, grab your cellphone and wallet and start "
                "walking down the road.")
    hit = "You've been hit by a car."
    lift = "A car slows down beside you."
    walk = ("You have made it to the gas station. Someone there helps you get "
            "a can of gas and takes you back to your car.")
    random_walk = random.choice([hit, lift, walk])
    if random_walk == hit:
        print_pause(hit)
        play_again()
    if random_walk == lift:
        print_pause(lift)
        hitchhike()
    if random_walk == walk:
        print_pause(walk)
        play_again()


def play_game():
    intro()
    make_choice()


def play_again():
    print_pause("Would you like to play again?")
    again = input("Enter 1 to play again. \n"
                  "Enter 2 to exit.\n")
    if again == "1":
        print_pause("Starting game over...\n")
        play_game()
    elif again == "2":
        print_pause("Thanks for playing.")
    else:
        print_pause("Please enter 1 or 2")
        play_again()


play_game()
