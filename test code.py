class a():
    x=22
    y=""

class b(a):
    z=""
    j=""
class human():
    name=""
    family=""
    age=0
    weight=0
    height=0
    sex=True
    race=""

    def __init__(self,age,weight,height,sex,race,address):
        human._age=age
        human.weight=weight
        human.height=height
        human.sex=sex
        human.race=race
        self.address=address
    def GetNormalWeight(self):
        result=(self.height-100)-(self.height-150)/4
        if result > self.weight:
            return "کاهش وزن"
        elif result < self.weight:
            return "افزایش وزن"
        else:
            return "وزن نرمال"
    def Introducing(self):
        return "   name : "+self.name +"   family : "+self.family +"   address : "+self.address +"   age : "+ str(self.age)

    @property
    def age(self):
        print("Get")
        return str(self._age) +" Years Old"

    @age.setter
    def age(self,value):
        print("Set")
        if value <=0:
            return 0
        self._age=value


objHuman1=human(1,2,40,True,"white","tehran")
objHuman1.name="arsam"
objHuman1.family="amini"
objHuman1.age=17
objHuman1.weight=45
objHuman1.height=180
objHuman1.sex=True
objHuman1.race="gandomi"

r=objHuman1.Introducing()
print(r)

"""
def sum(a,b,c=None):
    if c!=None:
        return a+b+c
    else:
        return a+b
print(sum(2,2,4))


class Dog():
    def info(self):
        print("G is My Dog")


class Cat():
    def info(self):
        print("Persian is My Cat")

def Getinfo(obj):
    obj.info()

object1=Dog()
object2=Cat()
getCatDog=input("Which one Cat or Dog? ")
if getCatDog=="Cat":
    Getinfo(object2)
elif getCatDog=="Dog":
    Getinfo(object1)
else:
    print("Invalid Data!")
"""


obj1 = a()
a.x=10
a.y=20

obj2 = b()