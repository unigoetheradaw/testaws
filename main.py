
# # This is Sparta
"""Das ist ein DocString"""
import os
import time
import random
from player import Player


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

  
def welcome():
    '''welcome function'''
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
    random.seed(seed)
    pips = random.randint(1, faces)
    return (pips)


def configure_game():
    players = []
    print("Category choosen: Configure your Game")
    print("Enter number of Players")
    num_players = int(input())  # generate player objects
    
    for i in range(num_players):
        name_player = input("Name of Player: ")
        players.append(Player(name_player, i))
        
    sixteen_is_dead(players)

    
def auto_game():
    return(role_dice())

    
def help():
    print("Help is coming, please hold.")
    #potato


def listprinting(obj_list):
    i = 0
    while i < len(obj_list):
        print(obj_list[i].name, "score:", obj_list[i].score)
        i += 1


def sixteen_is_dead(players):
    print("Press \<enter> to role dice. \<n> for next Player")
    for player in players:
        print("Your turn", player.name)
        while(True):
            input_str = input()
            if (input_str == ""):
                pips = role_dice()
                player.score += pips
                print("Dice was:", pips, "New Player score is", player.score)
                if (player.score == 9):
                    #break and next player
                    print("You loose, due to 9")
                    player.score = -1
                    break
                elif (player.score == 10):
                    #wait three seconds and roll again.
                    print("Force role, because of 10")
                    player.score += role_dice()
                elif (16 <= player.score):
                    #break and next player
                    print("You loose, due to 16 or higher")
                    break
                    
            if (input_str == "n"):
                break


def somefunc():
    # sumeplayers()
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

