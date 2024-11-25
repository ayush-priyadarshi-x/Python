class Animal: 
    def __init__(self, species, nature):
        self.species = species
        self.nature = nature


    def show(self): 
        print(f" Species : {self.species} \n Nature : {self.nature}")

class pets(Animal): 
    def __init__(self, species):
        super().__init__(species, "Domestic")


class dog(pets): 
    def __init__(self):
        super().__init__("Dog")


firstDog = dog()
firstDog.show()