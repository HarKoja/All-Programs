from sqlalchemy import create_engine,Column,String,TEXT,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker

#ایجاد موتور پایگاه داده و جلسه
engine=create_engine("sqlite:///database.db",echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    family = Column(String)
    age = Column(Integer)
    address = Column(String)
    phone = Column(String)





class Repository():
    def Add(self,obj):
        session.add(obj)
        session.commit()
    def SelectAll(self,obj):
        result = session.query(obj).all()
        return result
    def SelectById(self,obj,id):
        record = session.query(obj).filter(obj.id==id).first()
        return record
    def ShowObj(self,list,index):
        for item in list:
            attr = getattr(item,index)
            print(attr)
    def Update(self,obj,id,**kwargs):
        record = self.SelectById(obj,id)
        for key, val in kwargs.items():
            setattr(record,key,val)
        session.commit()

    def Delete(self,id,obj):
        record = self.SelectById(id,obj)
        session.delete(record)
        session.commit()

result = session.query(Person).filter(Person.name.contains("m")).all()
for item in result:
    print(""+item.name+" : "+item.family)


Base.metadata.create_all(engine)

repos = Repository()
#Add
"""
p = Person(name="",family="",age=0,address="",phone="")
repos.Add(p)
"""

"""
#SelectById
res=repos.SelectById(Person,1)
print(res.name+" "+res.family+" Age: "+res.age+" Address: "+res.address+" Phone: "+res.phone)
#ShowObj
result = repos.SelectAll(Person)
repos.ShowObj(result,"name")
#Update
repos.Update(Person,2,name="",family="",age=0,address="",phone="")
#Delete
repos.Delete(Person,3)
#Create Done
"""