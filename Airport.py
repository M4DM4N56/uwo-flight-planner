class Airport:
    # simple initializer
    def __init__(self, code, city, country):
        self.code = code
        self.country = country
        self.city = city

    def __repr__(self):
        # formats the output nicely
        return f'{self.code} ({self.city}, {self.country})'

    # simple getter
    def getCode(self):
        return self.code

    # simple getter
    def getCity(self):
        return self.city

    # simple getter
    def getCountry(self):
        return self.country

    # simple setter
    def setCity(self, city):
        self.city = city

    # simple setter
    def setCountry(self, country):
        self.country = country
