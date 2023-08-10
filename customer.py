from abc import ABC,abstractmethod
class Customer():
    @abstractmethod
    def __init__(self):
        pass
    name = ""
    family = ""

class CustomerFree(Customer):
    phone=1234
    def __init__(self):
        self.phone= +989028459923
class CustomerVIP(Customer):
    def __init__(self):
        self.codeP= 7624093

objFree = CustomerFree()
objVIP = CustomerVIP()
print(objFree.phone)

