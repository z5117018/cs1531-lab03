class Location():
    def __init__(self,pickup,dropoff):
        self.__pickup = pickup
        self.__dropoff = dropoff
    def getPickUp(self):
        return self.__pickup
    def getDropOff(self):
        return self.__dropoff
    def setPickUp(self,pickup):
        self.__pickup = pickup
    def setDropOff(self,dropoff):
        self.__dropoff = dropoff
        