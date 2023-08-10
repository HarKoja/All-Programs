import abc
from abc import abstractmethod
class Person():
    name=""
    family=""
    phone=""
    age=0
    sex=True
    @abstractmethod
    def __init__(self):
        pass



class uni():
    name=""
    place=""
    tel=""
    email=""
    fax=""
    teachers=[]
    ClassRoom=[]
    Sections=[]
    def __init__(self,name,place,tel,email,fax):
        self.name=name
        self.place=place
        self.tel=tel
        self.email=email
        self.fax=fax
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_section(self, section):
        self.Sections.append(section)




class Teacher(Person):
    edu=""
    history=""
    Uni=[]
    Sections=[]
    def __init__(self,name="",family="",phone="",edu="",sex=True,history=""):
        self.name=name
        self.family=family
        self.phone=phone
        self.edu=edu
        self.sex=sex
        self.history=history
        self.Sections=[]
    def add_uni(self, uni):
        self.Uni.append(uni)

    def add_section(self, section):
        self.Sections.append(section)

    def GetSections(self):
        return len(self.Sections)

class Student(Person):
    studentCode=0
    age=""
    field=""
    uni=None
    Sections=[]
    def __init__(self,name="",family="",phone="",studentCode=0,sex=True,age="",field=""):
        self.name=name
        self.family=family
        self.phone=phone
        self.studentCode=studentCode
        self.sex=sex
        self.age=age
        self.field=field
    def add_section(self, section):
        self.Sections.append(section)



class ClassRoom():
    code=0
    metre=0
    level=True
    Sections=[]
    def __init__(self, code, metre, level):
        self.code=code
        self.metre=metre
        self.level=level
    def add_section(self, section):
        self.Sections.append(section)


class Lesson():
    code=0
    title=""
    Sections=[]
    def __init__(self,code,title):
        self.code=code
        self.title=title
    def add_section(self, section):
        self.Sections.append(section)

class Section():
    Uni=None
    Teacher=None
    ClassRoom=None
    Lesson=None
    start=""
    end=""
    students=[]
    def __init__(self,Uni=None,Teacher=None,ClassRoom=None,Lesson=None,start="",end=""):
        self.Uni=Uni
        self.Teacher=Teacher
        self.ClassRoom=ClassRoom
        self.Lesson=Lesson
        self.start=start
        self.end=end
    def add_student(self, student):
        self.students.append(student)


#client code


objUni=uni("chamran","ahwaz","09149266901","","")

Teacher1=Teacher("mohsen","modhej","09352671012")
Teacher2=Teacher("milad","moradyan","09120000000")

Student1=Student("ali","molodi")
Student2=Student("maryam","amani")
Student3=Student("reza","asghari")

Lesson1=Lesson(21,"oop")
Lesson2=Lesson(29,"business")

LessonClass1=ClassRoom(18,200,False)

section=Section(objUni,Teacher1,LessonClass1,Lesson1,"7:30","14")


section.add_student(Student1)
section.add_student(Student2)
section.add_student(Student3)


Student1.add_section(section)
Student2.add_section(section)
Student3.add_section(section)


Teacher1.add_section(section)
Teacher2.add_section(section)


Lesson1.add_section(section)


objUni.add_section(section)


print(Teacher2.GetSections())