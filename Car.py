from abc import ABC, abstractmethod
# Knows daily fee, current status, type and registration
# details
class Car(ABC):
    def __init__(self,fee,status,carType,registration):
        self.__fee = fee
        self.__status = status
        self.__carType = carType
        self.__registration = registration
        super().__init__()
    
    def getFee(self):
        return self.__fee
    def getStatus(self):
        return self.__status
    def getCarType(self):
        return self.__carType
    def getRegistration(self):
        return self.__registration

    def setFee(self,fee):
        self.__fee = fee
    def setStatus(self,status):
        self.__status = status
    def setCarType(self, carType):
        self.__carType = carType
    def setRegistration(self, registration):
        self.__registration = registration

    @abstractmethod
    def __str__(self):
        pass

class smallCar(Car):
    def __init__(self,fee,status,carType,registration):
        super().__init__(fee,status,carType,registration)
    def __str__(self):
        return "Small car has fee {0}, status {1} and registration {2}\n".format(self.getFee(),self.getStatus(),self.getRegistration())

class mediumCar(Car):
    def __init__(self,fee,status,carType,registration):
        super().__init__(fee,status,carType,registration)

    def __str__(self):
        return "Medium car has fee {0}, status {1} and registration {2}\n".format(self.getFee(),self.getStatus(),self.getRegistration())

class largeCar(Car):
    def __init__(self,fee,status,carType,registration):
        super().__init__(fee,status,carType,registration)

    def __str__(self):
        return "Large car has fee {0}, status {1} and registration {2}\n".format(self.getFee(),self.getStatus(),self.getRegistration())

class premiumCar(Car):
    def __init__(self,fee,status,carType,registration):
        super().__init__(fee,status,carType,registration)

    def __str__(self):
        return "Premium car has fee {0}, booking status {1} and registration {2}\n".format(self.getFee(),self.getStatus(),self.getRegistration())