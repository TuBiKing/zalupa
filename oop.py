class Human:
    population_size = None
    race1 = None
    race2 = None
    race3 = None
    the_smartest_race = None
    the_stupidest_race = None
    the_biggest_country = None

    def first(self, population_size, race1, race2, race3, the_smartest_race, the_stupidest_race, the_biggest_country):
        self.population_size = population_size
        self.race1 = race1
        self.race2 = race2
        self.race3 = race3
        self.the_smartest_race = the_smartest_race
        self.the_stupidest_race = the_stupidest_race
        self.the_biggest_country = the_biggest_country

    def vivod(self):
        print("количество популяции:",self.population_size,"Первая расса:", self.race1,"Вторая расса:", self.race2,"Третья расса:", self,self.race3, "Умнейшая расса:",self.the_smartest_race,"Тупейшая расса:", self,self.the_stupidest_race, "Самая большая страна:",self,self.the_biggest_country,sep = "\n")

classification_for_first_planet = Human()
classification_for_first_planet.first("8 billions", "Asian","Niggers", "European","Asian","Niggers,mazafaka","Russian")


classification_for_second_planet = Human()
classification_for_second_planet.first("20 billion", "Niggers", "Asian","European","Niggers_TheSmartest_mazafaka1","Asian((","Vatikan")



classification_for_first_planet.vivod()
classification_for_second_planet.vivod()

