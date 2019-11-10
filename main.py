from structures.City import City
from structures.Country import Country
from structures.Euro_map import Euro_map

FINISHSTRING = "0"

MIN_COORDINATE = 0
MAX_COORDINATE = 10

MIN_COUNTRY_NAME = 1
MAX_COUNTRY_NAME = 25

MIN_COUNTRIES_NUMBER = 1
MAX_COUNTRIES_NUMBER = 20


def getInput():

    input = open("tests/input.txt", "r")
    input = input.readlines()
    i = 0
    curString = input[i]
    caseNumber = 1

    while curString != finishString:

        i += 1

        if isCase(curString):

            processCase(input [i-1:i+int(curString)], caseNumber)
            caseNumber += 1
            i = i + int(curString)

        curString = input[i]



def isCase(curString):

    return int(curString) <= MAX_COUNTRIES_NUMBER and int(curString) >= MIN_COUNTRIES_NUMBER


def processCase(caseString, caseNumber):

    case = Euro_map(int(caseString[0]), caseNumber)

    for i in caseString[1:]:

        case.addCountry(getCountry(i[:-1]))

    case.addAllNeighbors()
    case.processCoins()

    print("Case number", case.caseNumber)

    for name, days in case.days.items():

        print("Name: ", name, ",  days spent: ", days)

    return


def getCountry(countryString):

    if (isCountryName(countryString.rsplit(" ")[0]) and isCountryCoordinates(countryString.rsplit(" ")[1:])):

        name = countryString.rsplit(" ")[0]
        coordinates = countryString.rsplit(" ")[1:]

    country = Country (name, coordinates)

    return country



def isCountryName(name):

    return len(name) <= MAX_COUNTRY_NAME


def isCountryCoordinates(coordinates):

    for i in coordinates:

        i = int (i)

        if i > MAX_COORDINATE or i < MIN_COORDINATE:

            return False

    return coordinates[0] <= coordinates[2] and coordinates[1] <= coordinates[3]


