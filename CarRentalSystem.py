# import booking class
from Booking import Booking

class CarRentalSystem():
    def __init__(self,cars,bookings):
        self.__cars = cars # list of cars
        self.__bookings = bookings# bookings # list of bookings        

    def getCars(self):
        return self.__cars
    
    def getBookings(self):
        return self.__bookings

    def setCars(self,cars):
        self.__cars = cars
    
    def setBookings(self,bookings):
        self.__bookings = bookings

    def addCar(self,car):
        self.__cars.append(car)

    def makeBooking(self, car, customer, location, days, insurance):
        newBooking = Booking(customer, car, location, days, insurance)
        self.__bookings.append(newBooking)
        netPrice = newBooking.computeNetPrice()
        self.emailBooking(customer.getName(),car.getCarType(),days,location,netPrice)
        
    def emailBooking(self,name,car,days,location,netPrice):
        print("Your booking has been confirmed {0}. Your {1} car will be available for {2} days, please pick it up from {3} and drop it off at {4}.\nThe net total charged is ${5}.\n".format(name,car,days,location.getPickUp(),location.getDropOff(),netPrice))