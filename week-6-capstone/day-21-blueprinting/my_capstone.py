# ===================================================
#  MY CAPSTONE PROJECT
#  Project name: ____________________________________
#  Path (A / B / C): ________________________________
#  Goal in one sentence: ____________________________
# ===================================================
#
#  This is a GENERIC SKELETON. Shape it to YOUR project.
#  You'll keep building this same file on Days 22, 23, and 24.
#  There is no answer key this week -- you're the author now! 🏆
# ===================================================

import random
import time


# -------- 1) SETUP: your starting variables --------
# TODO: Create the variables your game needs to track.
#   Examples (delete the ones you don't need, add your own):
#   score = 0
#   money = 100
#   health = 10
#   game_data = {}        # a dictionary (e.g., a pet's stats)
#   items = []            # a list (e.g., a deck or inventory)


def show_title():
    """Print a cool title/splash screen for your game."""
    # TODO (you'll make this fancy on Day 23):
    print("====================================")
    print("        MY CAPSTONE GAME")
    print("====================================")


def show_menu():
    """Print the choices the player can make each turn."""
    print()
    print("What would you like to do?")
    print("  1) (your first action)")
    print("  2) (your second action)")
    print("  3) (your third action)")
    print("  4) Quit")


# -------- 2) MAIN GAME LOOP --------
show_title()

while True:
    show_menu()
    choice = input("Pick an option: ")

    if choice == "1":
        print("TODO: make option 1 do something")
    elif choice == "2":
        print("TODO: make option 2 do something")
    elif choice == "3":
        print("TODO: make option 3 do something")
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")

    # TODO (Day 22): check your win/lose condition here and 'break' if the game is over.
