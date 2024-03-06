import random
import os
import time
from colorist import blue, red, green, yellow, cyan, magenta, white
from simple_term_menu import TerminalMenu
dna = 0
virus_name = str()
day = 0

def loading():
    print("Loading")
    time.sleep(0.5)
    os.system('clear')
    print("Loading.")
    time.sleep(0.5)
    os.system('clear')
    print("Loading..")
    time.sleep(0.5)
    os.system('clear')
    print("Loading...")
    time.sleep(0.5)
    os.system('clear')
    print("Loading..")
    time.sleep(0.5)
    os.system('clear')
    print("Loading.")
    time.sleep(0.5)
    os.system('clear')
    print("Loading")
    time.sleep(0.5)
    os.system('clear')

# Statistique des pays
class Country:
    def __init__(self, population, infected, death):
        self.population = population
        self.infected = infected
        self.death = death

france = Country(67000, 0, 0)
mexico = Country(130000, 0, 0)
usa = Country(330000, 0, 0)

# Statistique des virus
class Virus:
    def __init__(self, name, dna, infectiosity, mortality):
        self.name = name
        self.dna = dna
        self.infectiosity = infectiosity
        self.mortality = mortality

virus = Virus(virus_name, 0, 0.1, 0)

def config():
   os.system('clear')
   global virus_name
   blue("Welcome to Plague Inc in Python")
   time.sleep(1)
   os.system('clear')
   green("Enter the name of your virus")
   virus.name = virus_name = input("Virus name: ")
   os.system('clear')
   loading()
   yellow("The rules are simple, you have to infect the entire world with your virus")
   time.sleep(1)
   yellow("You have to manage your DNA to improve your virus")
   time.sleep(1)
   yellow("You can increase the infectiosity and the mortality of your virus")
   time.sleep(1)
   yellow("Press 1 to start the game")
   yellow("Press 2 to quit")
   choice = input("Choice: ")
   if choice == "1":
    os.system('clear')
    green("you infected the first person in France")
    france.infected += 1
    time.sleep(1)
    green("good luck")
    time.sleep(1)
    game()
       
   elif choice == "2":
    os.system('clear')
    cyan("Goodbye")
    time.sleep(1)
    os.system('clear')
    exit()
   else:
       
       print("Invalid choice. Please try again.")
       time.sleep(1)
       os.system('clear')
       config()


#le jeu en lui même
def game():
    global virus_name
    global virus
    global france
    global day
    global dna
    c = 0
    os.system('clear')
    #boucle du jeu pour les tours
    while day < 101: 
        france.death = france.death + (france.infected * virus.mortality)
        france.infected = france.infected + (france.infected * virus.infectiosity)
        france.population = france.population - france.death
        day += 1
        dna_luck = random.randint(1, 3)
        dna += dna_luck

        

        if france.infected >= france.population and c == 0:
            c = 1
            os.system('clear')
            green("You have infected the entire world")
            time.sleep(1)
            os.system('clear')
            red("Now the world is in chaos")
            time.sleep(1)
            red("kill everyone !")
            time.sleep(1)
            os.system('clear')
            if france.death >= 67000:
                green("You have killed everyone in France")
                time.sleep(1)
                os.system('clear')
                cyan("Goodbye")
                time.sleep(1)
                os.system('clear')
                exit()

                
        

        print(virus.name, "has infected", france.infected, "people in France")
        print(virus.name, "has killed", france.death, "people in France")
        print("Day", day, "     infectiosity :", virus.infectiosity)
        print("DNA:", dna, "    mortality :", virus.mortality)
        print("1. Improve infectiosity")
        print("2. Improve mortality")
        print("3. Pass a day")
        print("4. Quit")
        choice = input("Choice: ")
        if choice == "1":
            if dna >= 10:
                dna -= 10
                virus.infectiosity += 0.1
                os.system('clear')
                green("Infectiosity improved")
                a = random.randint(1, 5)
                if a == 1:

                    yellow("the virus has developed marine transmission")
                
                elif a ==2:

                    yellow("the virus has developed air transmission")

                elif a == 3:

                    yellow("the virus has developed water transmission")

                elif a == 4:

                    yellow("the virus has developed insect transmission")

                elif a == 5:

              
                    yellow("the virus has developed rodent transmission")

                time.sleep(2)
                os.system('clear')
                 
            
            
        
            else:
                os.system('clear')
                red("Not enough DNA")
                time.sleep(1)
                os.system('clear')
        elif choice == "2":
            if dna >= 10:
                dna -= 10
                virus.mortality += 0.1
                os.system('clear')
                green("Mortality improved")
                b = random.randint(1, 5)
                if b == 1:

                    yellow("the virus has developed fever symptoms")
                
                elif b ==2:

                    yellow("the virus has developed cough symptoms")

                elif b == 3:

                    yellow("the virus has developed sneeze symptoms")

                elif b == 4:

                    yellow("the virus has developed vomit symptoms")

                elif b == 5:

                     yellow("the virus has developed diarrhea symptoms")
                time.sleep(2)
                os.system('clear')        
            else:
                os.system('clear')
                red("Not enough DNA")
                time.sleep(1)
                os.system('clear')
        elif choice == "3":
            game()
            os.system('clear')
        elif choice == "4":
            os.system('clear')
            cyan("Goodbye")
            time.sleep(1)
            os.system('clear')
            exit()
        else:
            red("Invalid choice")
            time.sleep(1)
            os.system('clear')
            game()
        


config()
