class IotDevices:
    __count = 0

    def __init__(self, name, type, cost):
        print("An Object of the class IotDevices has been created")
        self.name = name
        self.type = type
        self.cost = cost
        IotDevices.__count += 1

    def printDetails(self):
        print('The Name of the device is ', self.name)
        print('It is of type', self.type)
        print('Cost', self.cost)

    @staticmethod
    def get_count():
        return IotDevices.__count


device1 = IotDevices("Raspi", "Controller", 2320)
print("Count =", IotDevices.get_count())
device2 = IotDevices("DMM", "Equipement", 500)
print("Count =", device2.get_count)
device1.printDetails()
device2.printDetails()
