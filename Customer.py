class Customer():

    def __init__(self,age,name,licenseNum,email):
        self.__name = name #string
        self.__age = age #int
        self.__licenseNum = licenseNum #string
        self.__email = email

#  age, name, license number and email address
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getLicenseNum(self):
        return self.__licenseNum
    def getEmail(self):
        return self.__email

    def setName(self,name):
        self.__name = name

    def setAge(self,age):
        self.__age = age
    
    def setLicenseNum(self, licenseNum):
        self.__licenseNum = licenseNum

    def setEmail(self, email):
        self.__email = email

    