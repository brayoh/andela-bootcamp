class Country(object):

    """ encapsulation """

    __malaria_infected_people = 0

    def __init__(self, name, region, official_language):

        self.name = name

        self.region = region

        self.official_language = official_language


    def citizen_description(self):
        print ("Hi I'm from %s and %s is my Country" % (self.region, self.name))

    def official_language (self):
      print ("%s is our official language" %self.official_language)


    def citizen_opinion(self):
        print("{} is an awesome place to be".format(self.name))

    def set_infected_chilren(self, num):
        self.__malaria_infected_people = num


 # inherit Country
class City(Country):

     def __init__(self, city_name, stadium, number_of_hospitals):

        self.name = name

        self.region = region

        self.official_language = official_language

        self.stadium  = stadium

        self.number_of_hospitals = number_of_hospitals

        self.city_name = city_name


   # polymorphism for the method name opinion

     def citizen_opinion(self):
        print("{} is an awesome place to be".format(self.city_name))


if __name__ == '__main__':

      China = Country("Asia", "China", "Shanghai")
