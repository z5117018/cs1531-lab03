class Booking():
    # bookingId, car, start, end
    def __init__(self,customer,car,location,days, insurance):
        self.__customer = customer # customer
        self.__car = car # car
        self.__location = location
        self.__days = days #int
        self.__insurance = insurance

    def getCustomer(self):
        return self.__customer 
    
    def getCar(self):
        return self.__car
    
    def getLocation(self):
        return self.__location

    def getDays(self):
        return self.__days

    def getInsurance(self):
        return self.__insurance
    
    def getPrice(self):
        return self.__price

    def setCustomer(self,customer):
        self.__customer = customer
    
    def setCar(self,car):
        self.__car = car

    def setDays(self, days):
        self.__days = days

    def setInsurance(self, insurance):
        self.__insurance = insurance

    def setLocation(self, location):
        self.__location = location

    def computeNetPrice(self):
        rentalFee = self.__car.getFee()
        rentalFee *= self.__days
        if self.__car.getCarType() == "Premium":
            rentalFee *= 1.15
        if self.__car.getCarType() == "Premium" or self.__car.getCarType() == "Large" and self.__days > 7:
                rentalFee *= 0.95
        self.__price = rentalFee
        return rentalFee
            
