# # This is the main file
"""Das ist ein DocString"""
import os
import time
import random


def clearscreen():
  os.system('cls' if os.name == 'nt' else 'clear')

  
def welcome():
    print("==============16 ist tot==============")
    print("|.............:Willkommen:...........|")
    print("|....................................|")
    print("|.Press (1)..Configure your Game.....|")
    print("|.Press (2)..Auto-Game...............|")
    print("|.Press (3)..Help....................|")
    print("|.Press (4)..Exit....................|")
    print("======================================")


def role_dice(number=1, faces=6, seed=None):
    print("LOLOLOL Seed:", seed)
    random.seed(seed)
    c = random.randint(1, faces)
    random.seed(seed)
    b = random.randint(1, faces)
    random.seed(seed)
    a = random.randint(1, faces)
    return (a, b, c)


def configure_game():
    print("Category choose: Configure your Game")
    print("Enter number of Players")
    players_number = int(input())  # generate player objects
    print("Enter number of Dices")
    dices_number = int(input())  # catch errors
    print("Enter number of Faces of Dices")
    faces_number = int(input())  # catch_errors
    print("Do you want to set a seed (y/n)")
    # perhaps override seed in role_dice
    seed = input()
    role_dice(dices_number, faces_number, seed)

    
def auto_game():
    return(role_dice())

    
def help():
    potato


def somefunc():
    welcome()
    seed = 5
    while(True):
        a = input()
        print(a)
        if (a == "4"):
            break
        if (a == "1"):
             configure_game()
        if (a == "2"):
            print(auto_game())
        if (a == "3"):
            print("You are lost. Help yourself")
            break



somefunc()

# clearscreen()
