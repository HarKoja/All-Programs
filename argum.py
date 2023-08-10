def AvgAge(index,*args):
    avg=0
    sum=0
    for item in args:
        ObjResult = getattr(item, index)
        sum+=ObjResult
        avg=sum/len(args)
    print(avg)


class human():
    name=""
    family=""
    age=""
    height=""
    def __init__(self,name,family,age,height):
        self.name=name
        self.family=family
        self.age=age
        self.height=height


obj1=human("arsam","amini",15,176)
obj2=human("milad","moradian",24,180)
obj3=human("mohsen","modhej",35,175)

AvgAge("height",obj1,obj2,obj3)