from structures.City import City

MIN_COORDINATE = 0
MAX_COORDINATE = 10


class Country:

    def __init__ (self, name, coordinates):


        self.name = name
        self.coordinates = list(map(int, coordinates))
        self.cities = self.generateCities(coordinates)
        self.neighborCountries = []


    def generateCities(self, coordinates):

        cities = []

        for i in self.generateGrid(coordinates):

            cities.append(City(i, self.name))

        return cities


    def generateGrid (self, coordinates):

        ordinates = list(range(int(coordinates[0]), int(coordinates[2]) + 1))
        abscysses = list(range(int(coordinates[1]), int(coordinates[3]) + 1))

        return [(x, y) for x in ordinates for y in abscysses]


    def addNeighborsCities(self, city):


        #check downside
        if (city.coordinates[1] != MIN_COORDINATE):

            self.checkandaddCityNeighbour (city, [city.coordinates[0], city.coordinates[1] - 1])

        # check upside
        if (city.coordinates[1] != MAX_COORDINATE):

            self.checkandaddCityNeighbour(city, [city.coordinates[0], city.coordinates[1] + 1])

        #check leftside
        if (city.coordinates[0] != MIN_COORDINATE):

            self.checkandaddCityNeighbour(city, [city.coordinates[0] - 1, city.coordinates[1]])

        #check rightside
        if (city.coordinates[0] != MAX_COORDINATE):

            self.checkandaddCityNeighbour(city, [city.coordinates[0] + 1, city.coordinates[1]])

        return

    def checkandaddCityNeighbour(self, city, coordinates):

        if self.findCityByCoordinates(coordinates) and not city.checkNeighborCityExists(
                self.findCityByCoordinates(coordinates)):

            city.neighborCities.append(self.findCityByCoordinates(coordinates))

        return



    def isFull (self):

        for i in self.cities:

            if i.isFull() == False:

                return False

        return True


    def findCityByCoordinates(self, coordinates):

        for country in self.neighborCountries:

            for city in country.cities:

                if city.coordinates[0] == coordinates[0] and city.coordinates[1] == coordinates[1]:

                    return city

        for city in self.cities:

             if city.coordinates[0] == coordinates[0] and city.coordinates[1] == coordinates[1]:

                    return city

        return False


    def checkNeighborCountryExists (self, country):

        return country in self.neighborCountries



