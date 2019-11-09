MIN_COORDINATE = 0
MAX_COORDINATE = 10




class Euro_map:

    def __init__(self, countriesNumber, caseNumber):

        self.countriesNumber = countriesNumber
        self.caseNumber = caseNumber
        self.countries = []
        self.days = {}
        self.curDay = 0



    def addCountry (self, country):

        self.countries.append(country)


    def processCoins(self):
        countriesFull = 0

        while (1):

            for country in self.countries:

                for city in country.cities:

                    city.processDay()

        #check if is full every country from those who don't have the "full days" in dictionary, add new to the dictionary
        #if all of them have the "day" return

            for i in self.countries:

                if self.days[i.name] == 0:

                    if i.isFull():

                        self.days[i.name] = self.curDay

                else:

                    countriesFull +=1

            if countriesFull == self.countriesNumber:

                return

            self.curDay +=1

        return



    def addNeighborsCountries(self, country):

        #check downside
        for i in range(int(country.coordinates[0]), int(country.coordinates[2]) + 1):

            if (country.coordinates[1] != MIN_COORDINATE):

                self.checkandaddCountryNeighbor(country, [i, country.coordinates[1] - 1])

        #check upside
        for i in range(country.coordinates[0], country.coordinates[2] + 1):

            if (country.coordinates[3] != MAX_COORDINATE):

                self.checkandaddCountryNeighbor(country, [i, country.coordinates[3] + 1])

        #check leftside
        for i in range(country.coordinates[1], country.coordinates[3] + 1):

            if (country.coordinates[0] != MIN_COORDINATE):

                self.checkandaddCountryNeighbor(country, [country.coordinates[0] - 1, i])

        #check rightside
        for i in range(country.coordinates[1], country.coordinates[3] + 1):

            if (country.coordinates[2] != MAX_COORDINATE):

                self.checkandaddCountryNeighbor(country, [country.coordinates[2] + 1, i])

        return


    def checkandaddCountryNeighbor(self, country, coordinates):

        if self.findCountryByCoordinates(coordinates) and not country.checkNeighborCountryExists(
                self.findCountryByCoordinates(coordinates)):

            country.neighborCountries.append(self.findCountryByCoordinates(coordinates))
        return


    def findCountryByCoordinates(self, coordinates):

        for i in self.countries:

            if i.coordinates[0] <= coordinates[0] and i.coordinates[2] >= coordinates [0] \
                    and i.coordinates[1] <= coordinates[1] and i.coordinates[3] >= coordinates[1]:

                return i

        return False


    def addAllNeighbors(self):

        for country in self.countries:

            self.days[country.name] = 0

        for country in self.countries:

            self.addNeighborsCountries(country)

            for city in country.cities:

                country.addNeighborsCities(city)

                for otherCountry in self.countries:

                    if (otherCountry != country):

                        city.coins[otherCountry.name] = 0

        return


