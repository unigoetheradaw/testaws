
# # This is the main file
"""Das ist ein DocString"""
import os
import time
import random
from player import Player



def clearscreen():
  os.system('cls' if os.name == 'nt' else 'clear')

  
def welcome():
    print("==============16 ist tot==============")
    print("|.............:Willkommen:...........|")
    print("|....................................|")
    print("|.Press (1)..Configure your Game.....|")
    print("|.Press (2)..Auto-Game...............|")
    print("|.Press (3)..Help....................|")
    print("|.Press (4)..Admin View..............|")
    print("|.Press (5)..Exit....................|")
    print("======================================")


def role_dice(number=1, faces=6, seed=None):
    # number zeug machen
    """
    sdfgdfgfg
    
    """
    random.seed(seed)
    a = random.randint(1, faces)
    return (a)


def configure_game():
    liste = []
    print("Category choose: Configure your Game")
    print("Enter number of Players")
    num_players = int(input())  # generate player objects
    
    for i in range(num_players):
        name_player = input("Name of Player")
        liste.append(Player(name_player, i))
        #P1 = Player(name, 0, 0, 0)
    
    print(liste[0].name)
    role_dice()

    
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
