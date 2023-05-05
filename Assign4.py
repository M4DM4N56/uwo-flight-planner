from Flight import *
from Airport import *

allAirports = []
allFlightList = []
allFlights = {}


def loadData(airportFile, flightFile):  # try except statements needed
    try:
        airportF = open(airportFile, "r", encoding='utf8')
        flightF = open(flightFile, "r", encoding='utf8')
    except FileNotFoundError:
        return False

    # airport file
    for line in airportF:
        # going through each part of each line of the airport file and making them codes, countries, or cities
        line = line.split(",")
        code = line.pop(0).strip()
        country = line.pop(0).strip()
        city = line.pop(0).strip()

        allAirports.append(Airport(code, city, country))

    # flight file
    origin = ""
    destination = ""

    for line in flightF:
        # going through each part of each line of the flight file and making them flight numbers, origin codes or destination codes
        line = line.split(",")
        flightNo = line.pop(0).strip()
        originCode = line.pop(0).strip()
        destinationCode = line.pop(0).strip()

        for airport in allAirports:
            # assigning the originCode to an airport object
            if originCode.upper() == airport.getCode().upper():
                origin = airport
            # assigning the destinationCode to an airport object
            if destinationCode.upper() == airport.getCode().upper():
                destination = airport

        flight = Flight(flightNo, origin, destination)

        # if code/key doesn't exist, make it and append the new object, if it does exist, append the new object
        if originCode not in allFlights:
            allFlights[originCode] = [flight]
        else:
            allFlights[originCode].append(flight)

    return True


def getAirportByCode(code):
    for airport in allAirports:
        # runs through allAirports, if code is in the airport object repr(), return the airport
        if code in airport.__repr__():
            return airport
    return int(-1)


def findAllCityFlights(city):
    # creating variables and lists
    cityCode = "pedro"
    cityFlightsList = []

    for i in allAirports:
        # running through all the airports, and finding the airport code for that city
        if city.upper() == i.getCity().upper():
            cityCode = i.getCode()

    for values in allFlights.values():
        # running through all the values of the allFlights dictionary
        for flights in values:
            # running through each individual flight object in the allFlights dictionary
            # if the cityCode is found in either the flight's destination or origin, add it to the list
            if cityCode in flights.getOrigin().getCode() or cityCode in flights.getDestination().getCode():
                cityFlightsList.append(flights)

    return cityFlightsList


def findAllCountryFlights(country):
    cityCodes = []
    countryFlightsList = []

    for i in allAirports:
        # running through all the airports, and finding the airport code for that country, and adding it to the list
        if country == i.getCountry():
            cityCodes.append(i.getCode())

    for values in allFlights.values():
        # running through all the values of the allFlights dictionary
        for flights in values:
            # running through each individual flight object in the allFlights dictionary
            for code in cityCodes:
                # running through the codes in cityCodes, if  the code is in the flights origin or destination, add it to the list
                if code in flights.getOrigin().getCode().upper() or code in flights.getDestination().getCode().upper():
                    countryFlightsList.append(flights)
    return countryFlightsList


def findFlightBetween(origAirport, destAirport):
    setTrue = False
    flightTwoSet = set()

    for i in allFlights[origAirport.getCode().upper()]:
        # running through all flights whose code is the origin airport's origin
        # if the destination codes are the same, return the flight
        if destAirport.getCode().upper() == i.getDestination().getCode().upper():
            return f'Direct flight: {origAirport.getCode()} to {destAirport.getCode()}'

    for flightOne in allFlights[origAirport.getCode()]:
        # running through all flights whose code is the origin airport's origin
        for flightTwo in allFlights[flightOne.getDestination().getCode()]:
            # from those flights, run through all flights where the origin is the previous destination
            if destAirport.getCode().upper() == flightTwo.getDestination().getCode().upper():
                # if the dest code is the flight two dest code, add this to the list and do this all over again
                flightTwoSet.add(flightTwo.getOrigin().getCode())
                setTrue = True

    if setTrue:
        return flightTwoSet
    else:
        return int(-1)


def findReturnFlight(firstFlight):
    for flight in allFlights[firstFlight.getDestination().getCode().upper()]:
        # runs through all flights that have the same origin as the firstFlight
        if flight.getOrigin().getCode().upper() == firstFlight.getDestination().getCode().upper():
            # if the destination/origins are inversions of each other, return the flight
            if flight.getDestination().getCode().upper() == firstFlight.getOrigin().getCode().upper():
                return flight
    return int(-1)
