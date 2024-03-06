import os
from simple_term_menu import TerminalMenu
import time
from colorist import blue, red, green, yellow, magenta, cyan, white, black 
import Play 
def loading():
        os.system('clear')
        blue("loading")
        time.sleep(0.2)
        os.system('clear')
        blue("loading.")
        time.sleep(0.2)
        os.system('clear')
        blue("loading..")
        time.sleep(0.2)
        os.system('clear')
        blue("loading...")
        time.sleep(0.2)


def menu_1(Home):
    os.system('clear')
    home_menu = ["Play","Settings","Exit"]
    Menu_1 = TerminalMenu(home_menu)
    Menu_1_entry_index = Menu_1.show()
    print(Menu_1_entry_index)
    if Menu_1_entry_index == 0:
        os.system('clear')
        loading()
        Play.play()
    elif Menu_1_entry_index == 1:
        os.system('clear')
        print("Settings")
    elif Menu_1_entry_index == 2:
            os.system('clear')
            red("Exit")
            time.sleep(0.2)
            os.system('clear')
            red("Exit.")
            time.sleep(0.2)
            os.system('clear')
            red("Exit..")
            time.sleep(0.2)
            os.system('clear')
            red("Exit...")
            time.sleep(0.2)
            os.system('clear')
            red("Exit..")
            time.sleep(0.2)
            os.system('clear')
            red("Exit.")
            time.sleep(0.2)
            os.system('clear')
            red("Exit")
            time.sleep(0.2)
    else:
        print("Error") 
        time.sleep(2)
        menu_1(Home)
menu_1(Home=True)

