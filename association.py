"""
class human():
    name=""
    family=""
    age=0
    car=car()
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age


class car():
    color="red carbon"
    plack=0
    model="Bugatti Chiron"
    human=human()
    def __init__(self,color,plack,model):
        self.color=color
        self.plack=plack
        self.model=model



objHuman=human("arsam","amini",15)
objcar=car("red carbon",88898,"Bugatti Chiron")
objcar.human=objHuman
objHuman.car=objcar
"""

class human():
    name=""
    family=""
    age=""
    car=None
    books=[]
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
#service
    def info(self):
        print(f"Hello I'am{self.name}{self.family}")
#message passing
    def TrunCars(self):
        self.car.TrunOn()
    def AddBook(self,book):
        self.books.append(book)
    def ListBook(self):
        for item in self.books:
            print(item.title)

class book():
    title=""
    price=0
    author=""
    human=None
    def __init__(self,title,price,author):
        self.title=title
        self.price=price
        self.author=author
    def ShowBookInfo(self):
        return self.title

    def ShowBookOwner(self):
        return self.human.name +" "+ self.human.family
class car():
    color="red carbon"
    plack=0
    model="Bugatti Chiron"
    human=None
    def __init__(self,color,plack,model):
        self.color=color
        self.plack=plack
        self.model=model

#service
    def TrunOn(self):
        print("TrunOn")
#nemonegiri

objHuman=human("arsam","amini",15)
objCar=car("red carbon",88898,"Bugatti Chiron")
objBook1=book("python one1",20000,"milad")
objBook2=book("python tow2",20000,"milad")


#malekiat

objHuman.AddBook(objBook1)
objHuman.AddBook(objBook2)
objBook1.human=objHuman
objBook2.human=objHuman
objHuman.car=objCar
objCar.human=objHuman


#message passing


objHuman.car.TrunOn()
objHuman.TrunCars()


#prints
print(objBook1.ShowBookOwner())
objHuman.ListBook()