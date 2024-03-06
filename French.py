from country import Country, france, mexico, usa
import os
import time
import random
import simple_term_menu
def LaFrance():
    os.system('clear')
    print("choose a name for your virus")
    virus_name = input("Virus name: ")
    os.system('clear')
    print("your virus name is",virus_name)
    time.sleep(1)
    os.system('clear')
    print("France is a country with",france.population,"inhabitants")
    print("Your virus infected his first inhabitant")
    france.infected += 1
    print("France is a country with",france.population,"inhabitants", "and",france.infected,"infected")
    turn()
global virus_name
def turn():
    os.system('clear')
    day = 0
    mortality = 0
    infection = 0.1
    dna = 0
    def shop():
        global france, mortality, infection, dna, day, virus_name
        os.system('clear')
        print("1: increase the virus's lethality by 10%")
        print("2: increase the virus's infectivity by 10%")
        choice = int(input("Choice: "))
        if choice == 1:
            mortality *= 0.1 + mortality == mortality
            dna -= 5
        elif choice == 2:
            infection = infection * 0.1 + infection
            dna -= 5
        else:
            print("Invalid choice")
            time.sleep(1)
            os.system('clear')

    while day < 100 or france.infected < france.population:
        global virus_name
        os.system('clear')
        dna_gain = random.randint(1, 5)
        dna += dna_gain
        day += 1
        print(virus_name,"is spreading in France")
        france.infected += 1
        france.infected = france.infected + (france.infected * infection)
        france.death = france.infected * mortality
        france.population -= france.death
        print("France have",france.population,"inhabitants (in hundred)")
        print("France have",france.infected,"infected (in hundred)")
        print("France have",france.death,"death (in hundred)")
        print("lethality is",mortality,"and infectivity is",infection)
        print(day,"days have passed","you have",dna,"DNA", "(+", dna_gain, ")")
        game_menu = ["Evolve","Next day"]
        Menu = simple_term_menu.TerminalMenu(game_menu)
        game_menu_entry_index = Menu.show()
        print(game_menu_entry_index)
        if game_menu_entry_index == 0:
            shop()
        elif game_menu_entry_index == 1:
            os.system('clear')
            print("Next day")
            time.sleep(0.2)
            os.system('clear')
            print("Next day.")
            time.sleep(0.2)
            os.system('clear')
            print("Next day..")
            time.sleep(0.2)
            os.system('clear')
            print("Next day...")
        elif day >= 100:
            print("Game Over")
            time.sleep(2)
            os.system('clear')
            exit()

    #if france has more infected than inhabitants display a win message
        if france.infected > france.population:
            print("You win")
            time.sleep(2)
            os.system('clear')
            exit()
        elif day >= 100:
            print("Game Over")
            time.sleep(2)
            os.system('clear')
            exit()
            
LaFrance()