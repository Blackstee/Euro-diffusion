
STARTCOINS = 1000000
PART = 1000




class City:

    def __init__(self, coordinates, country):

        self.coordinates = list(map(int, coordinates))
        self.coins = {country: STARTCOINS}
        self.country = country
        self.neighborCities = []


    def processDay (self):

        coinsPortion = {}

        for country in self.coins.keys():
            coinsPortion[country] = self.coins[country]//PART

        for neighbor in self.neighborCities:

            for country, coins in self.coins.items():

                neighbor.coins[country] += coinsPortion[country]
                self.coins[country] -= coinsPortion[country]

        return


    def isFull (self):

        for i in self.coins.values():

            if i <= 0:

                return False

        return True


    def checkNeighborCityExists (self, city):

        return city in self.neighborCities




