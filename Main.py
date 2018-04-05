from Car import *
from Customer import *
from Booking import *
from Customer import *
from CarRentalSystem import *
from Location import *
def main():
    cars = []
    bookings = []
    sys = CarRentalSystem(cars,bookings)
    testSmallCar(sys)
    testPremiumCar(sys)
    testLargeCar(sys)

def testSmallCar(sys):
    fee = 100
    carA = smallCar(fee,False,"Small","smallRego")
    location = Location("kellyville","blacktown")
    customerA = Customer(20,"Robert smallCarbooker", "LicenseNum", "rCarbooker@unsw.edu.au")
    sys.addCar(carA)
    sys.makeBooking(carA,customerA,location,4,True)
    booking = sys.getBookings()[-1]
    assert(booking.getPrice() == 400)

def testPremiumCar(sys):
    fee = 200
    carB = premiumCar(fee,False,"Premium","PremiumRego")
    location = Location("kellyville","blacktown")
    customerB = Customer(20,"Robert premiumCarbooker", "LicenseNum", "rCarbooker@unsw.edu.au")
    sys.addCar(carB)
    sys.makeBooking(carB,customerB,location,4,True)
    booking = sys.getBookings()[-1]
    assert(int(booking.getPrice()) == 873)

def testLargeCar(sys):
    fee = 150
    carC = largeCar(fee,False,"Large","LargeRego")
    location = Location("kellyville","blacktown")
    customerC = Customer(20,"Robert largeCarbooker", "LicenseNum", "rCarbooker@unsw.edu.au")
    sys.addCar(carC)
    sys.makeBooking(carC,customerC,location,4,True)
    booking = sys.getBookings()[-1]
    assert(booking.getPrice() == 600)

if __name__ == "__main__":
    main()