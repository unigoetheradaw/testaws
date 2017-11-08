## This is the main file

import os
import time
 
def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')
    
def welcome():
    print("==============16 ist tot==============")
    print("|.............:Willkommen:...........|")
    print("|....................................|")
    print("|.Press (1)..Menue...................|")
    print("|.Press (2)..Auto-Game...............|")
    print("|.Press (3)..Exit....................|")
    print("======================================")

welcome()
time.sleep(3)

clearscreen()
#test