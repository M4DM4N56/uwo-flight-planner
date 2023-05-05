from Airport import *


# from Assign4 import *


class Flight:
    def __init__(self, _flightNo, _origin, _destination):  # else case needed
        self._flightNo = _flightNo
        # makes sure origin and destination are instances of Airport
        if isinstance(_origin, Airport) and isinstance(_destination, Airport):
            self._origin = _origin
            self._destination = _destination
        else:
            raise TypeError("The origin and destination must be Airport objects")

    def __repr__(self):
        # sees if flight crosses any international borders or not
        if self.isDomesticFlight():
            domestic = "domestic"
        else:
            domestic = "international"

        # formats the repr all neatly
        return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} {{{domestic}}}"

    def __eq__(self, other):
        # whether or not the flights are equivalent
        if self._origin == other._origin:
            if self._destination == other._destination:
                return True
        return False

    # simple getter
    def getFlightNumber(self):
        return self._flightNo

    # simple getter
    def getOrigin(self):
        return self._origin

    # simple getter
    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        # whether or not the origin and destinations are from the same country
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        return False

    # simple setter
    def setOrigin(self):
        self._origin = self._origin

    # simple setter
    def setDestination(self, destination):
        self._destination = self._destination
