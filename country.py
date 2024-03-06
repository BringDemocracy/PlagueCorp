
class Country:
    def __init__(self, name, population, infected, death):
        self.name = name
        self.population = population
        self.infected = infected
        self.death = death
        
france = Country("France", 670000, 0, 0)
mexico = Country("Mexico", 1300000, 0, 0)
usa = Country("USA", 3300000, 0, 0)

print(france.name)
