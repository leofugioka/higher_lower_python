import art
import os
from random import randint
from game_data import data

# Function to clear screen and print logo
def print_logo():
    os.system('cls')
    print(art.logo)

# Start game screen
def main_screen():
    '''Initial question'''
    global game_active
    
    print_logo()
    user_answer = input("Do you want to play Higher Lower? Type 'y' or 'n': ")
    
    if user_answer == 'y':
        game_active = True
    else:
        game_active = False

# Ensure a different value for option b
def different_option(option_a):
    option_b = randint(0, len(data) - 1)
    while option_b == option_a:
        option_b = randint(0, len(data) - 1)
    return option_b

main_screen()

#### code goes inside while
while game_active:
    count_streak = 0
    streak_active = True

    option_a = randint(0, len(data) - 1)
    option_b = different_option(option_a)

    while streak_active:
        print_logo();
        print(f"Option A: {data[option_a]["name"]} | Occupation: {data[option_a]["description"]} | Country: {data[option_a]["country"]}")
        print(art.vs)
        print(f"Option B: {data[option_b]["name"]} | Occupation: {data[option_b]["description"]} | Country: {data[option_b]["country"]}")

        if data[option_a]["follower_count"] > data[option_b]["follower_count"]:
            right_answer = 'a'
        else:
            right_answer = 'b'

        user_option = input("Who do you think has more followers? 'A' or 'B': ")

        if user_option == right_answer:
            count_streak += 1
            if right_answer == 'b':
                option_a = option_b
            option_b = different_option(option_a)
            input(f"You've guessed right! | Current streak: {count_streak} | Press 'Enter' to continue")
        else:
            streak_active = False
            print_logo()
            input(f"You've guessed wrong! | Max streak: {count_streak} | Press 'Enter' to continue")
            main_screen()

print("Thank you for playing!")