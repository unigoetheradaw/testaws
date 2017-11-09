# # This is the main file
"""Das ist ein DocString"""
import os
import time
from random import *


def clearscreen():
  os.system('cls' if os.name == 'nt' else 'clear')

  
def welcome():
    print("==============16 ist tot==============")
    print("|.............:Willkommen:...........|")
    print("|....................................|")
    print("|.Press (1)..Menue...................|")
    print("|.Press (2)..Auto-Game...............|")
    print("|.Press (3)..Help....................|")
    print("|.Press (4)..Exit....................|")
    print("======================================")


def role_dice(number=1, faces=6, seed=None):
    print(randint(1,6))

def somefunc():
    welcome()
    while(True):
        a = input()
        print(a)
        if(a == "4"):
            break
        if (a == "3"):
            print(role_dice)
            time.sleep(3)
            print(role_dice)
            time.sleep(3)
            print(role_dice)
            time.sleep(3)


somefunc()

# clearscreen()
