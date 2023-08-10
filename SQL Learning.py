from sqlalchemy import create_engine,Column,String,TEXT,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker

engine=create_engine("sqlite:///MyData.db",echo=True)
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class human(Base):
    __tablename__="human"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    family=Column(String)
    def __init__(self,name="",family=""):
        self.name=name
        self.family=family

class Repository():
    def Add(self,obj):
        session.add(obj)
        session.commit()
    def SelectAll(self,obj):
        result = session.query(obj).all()
        return result
#yek obj begire ke human ro bezare dakhelesh
#va yek id migire ke beg bar che asasi angam behse
#filter kon va ageh obj dakhelesh ba id ke man midam va id record mosavi bod bia first ro bede
    def SelectById(self,obj,id):
        result=session.query(obj).filter(obj.id==id).first()
        return result
#index yani name family va gheyreh
#dakhele for miad done done record hasho barmidare
#dakhele getattr migeh record aval field esm
    def ShowObj(self,list,index):
        for item in list:
            attr = getattr(item,index)
            print(attr)
#update no.1
    """
    def Update(self,obj,id,newdata):
        record =self.SelectById(obj,id)
        record.name=newdata.name
        record.family=newdata.family
        session.commit()
    """
#update no.2
    def update(self,id,object,**kwargs):
        record=self.SelectById(object,id)
        for key, val in kwargs.items():
            setattr(record,key,val)
        session.commit()
    def Delete(self,object,id):
        record = self.SelectById(object,id)
        session.delete(record)
        session.commit()



Base.metadata.create_all(engine)

"""
h = human(name="mamad", family="ahmadi")
repos.Add(h)

result = session.query(human).all()
for item in result:
    print(item.family)

result2 = session.query(human).get(1)
print(result2.name)
"""
repos=Repository()
"""
result=repos.SelectAll(human)
repos.ShowObj(result,"name")
res = repos.SelectById(human,1)
print(res.name+" : "+res.family)
"""
"""
record = repos.SelectById(human,1)
record.name="MamadAli"
record.family="shapori"
session.commit()
"""
repos.update(4,human,name="arsam",family="bilionre")

repos.Delete(human,2)