import abc
from abc import abstractmethod
class Person():
    name=""
    family=""
    age=""
    sex=True
    @abstractmethod
    def __init__(self):
        pass

class Customer(Person):
    phone=""
    def __init__(self,name,family,age,sex,phone):
        self.name=name
        self.family=family
        self.age=age
        self.sex=sex
        self.phone=phone


class Waiter(Person):
    personallyCode=""
    incom=""
    Shop=None
    Section=[]
    def __init__(self,name,family,age,sex,incom,personallyCode):
        self.name=name
        self.family=family
        self.age=age
        self.sex=sex
        self.incom=incom
        self.personallyCode=personallyCode

    def add_section(self, section):
        self.Section.append(section)


class Shop():
    logo=""
    place=""
    metre=""
    Customer=[]
    Waiter=[]
    Product=[]
    Section=[]
    def __init__(self,logo,place,metre):
        self.logo=logo
        self.place=place
        self.metre=metre
    def add_customer(self, customer):
        self.Customer.append(customer)

    def add_waiter(self, waiter):
        self.Waiter.append(waiter)

    def add_product(self, product):
        self.Product.append(product)

    def add_section(self, section):
        self.Section.append(section)


class Product():
    kind=""
    model=""
    price=""
    application=""
    quality=""
    Section=[]
    def __init__(self,kind,model,price,application,quality):
        self.kind=kind
        self.model=model
        self.price=price
        self.application=application
        self.quality=quality

    def add_section(self, section):
        self.Section.append(section)


class Section():
    Shop=None
    Waiter=None
    Product=None
    start=""
    end=""
    Customer=[]
    def __init__(self,Shop=None,Waiter=None,Product=None,start="",end=""):
        self.Shop=Shop
        self.Waiter=Waiter
        self.Product=Product
        self.start=start
        self.end=end

    def add_customer(self, customer):
        self.Customer.append(customer)


objShop=Shop("AI-Think","New york","2000m")

Waiter1=Waiter("mohsen","modhej","36",True,"2100$","0962")
Waiter2=Waiter("milad","moradian","25",True,"2000$","0928")
Waiter3=Waiter("lunia","vashangton","20",False,"1250$","0867")

Customer1=Customer("elon","musk","55",True,"+100000000")
Customer2=Customer("andrew","tate","39",True,"+408888988")

Product1=Product("Robot","AI-Lister3","19000000$","Best human robot helps to do everything","8.88/10")
Product2=Product("App","uber","Free","easy taxi easy delivery everywhere","9/10")


section=Section("objShop","Waiter1","Product1","8","21")
section.add_customer(Customer1)
section.add_customer(Customer2)


Waiter1.add_section(section)
Waiter2.add_section(section)
Waiter3.add_section(section)
