from colorist import red, green, yellow, magenta, cyan, white, black
import time
import os
import simple_term_menu
def play():
    os.system('clear')
    print("Welcome in Plague Inc. Terminal Edition")
    print("Choose a country to start the infection")
    free_country = ["France","Mexico","USA"]
    country = simple_term_menu.TerminalMenu(free_country)
    country_entry_index = country.show()
    print(country_entry_index)
    if country_entry_index == 0:
        from French import LaFrance
        # Le scénario avec la France
        LaFrance()
    elif country_entry_index == 1:
        # Le scénario avec le Mexique

        print("You chose Mexico")
    elif country_entry_index == 2:
        # Le scénario avec les USA
        print("You chose USA")
    else:
        print("Error")
        time.sleep(2)
        os.system('clear')
        play()
