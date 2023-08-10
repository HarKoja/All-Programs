from tkinter import *
from tkinter import messagebox
from tkinter import ttk


screen=Tk()
screen.title("Registering")
screen.geometry("%dx%d+%d+%d" % (800,400,500,400))
screen.resizable(False,False)


#function

UserAll=[]
def Register(User):
    if int(User["age"])>=15:
        if Exist(User):
            messagebox.showerror("وجود داره","این کاربر قبلا ثبت شده")
            return False
        else:
            messagebox.showinfo("تمومه","همه چی اوکیه از فردا بیا")
            UserAll.append(User)
            return True
    else:
        messagebox.showwarning("بچه سالی","هنوز کوچیکی واسه باشگاه زوده")
        return False

def OnClickRegister():
    name = Name.get()
    print(Check1.get())
    print(Check2.get())
    print(Check3.get())
    print(jens.get())
    family = Family.get()
    age = Age.get()
    us = {"name": name, "family": family, "age": age}
    result=Register(us)
    if result==True:
        ListItem=[Name,Family,Age]
        insertData(ListItem)
        Clear(ListItem)

def Clear(ListVal) :
    for item in ListVal:
        item.set("")
        txt1.focus_set()

def insertData(Value):
    tbl.insert('',"end",text="1",value=[Value[0].get(),Value[1].get(),Value[2].get()])

def GetSelction(e):
    Selction_row=tbl.selection()
    if Selction_row != ():
        btn3.place(x=540,y=160)
        ListItem = [Name, Family, Age]
        Clear(ListItem)
        Name.set(tbl.item(Selction_row)["values"][0])
        Family.set(tbl.item(Selction_row)["values"][1])
        Age.set(tbl.item(Selction_row)["values"][2])

def OnClickSearch():
    query = txtSearch.get()
    result = Search(query)
    CleanTable()
    Loud(result)

def Search(Value):
    ListSec=[]
    for item in UserAll:
        if item["name"]==Value or item["family"]==Value or item["age"]==Value:
            ListSec.append(item)
    return ListSec

def Loud(Value):
    for item in Value:
        tbl.insert('', "end", text="1", value=[item["name"], item["family"], item["age"]])



def CleanTable():
    for item in tbl.get_children():
        sel=(str(item))
        tbl.delete(sel)

def Exist(Value):
    for item in UserAll:
        if Value["age"]==item["age"] and Value["family"]==item["family"] and Value["name"]==item["name"]:
            return True
    return False


def OnClickDelete():
    result=messagebox.askquestion("هشدار","ایا مطمعن هستید میخواهید این داده را حذف کنید")
    print(result)
    if result=="yes":
        Delete()


def Delete():
    select_row = tbl.selection()
    if select_row!=():
        SelectItem = tbl.item(select_row)["values"]
        dic={'name': SelectItem[0],'family': SelectItem[1],'age': str(SelectItem[2])}
        tbl.delete(select_row)
        UserAll.remove(dic)


def OnClickEdit():
    select_row = tbl.selection()
    SelectItem = tbl.item(select_row)["values"]
    dic = {'name': SelectItem[0], 'family': SelectItem[1], 'age': str(SelectItem[2])}
    indexUs=UserAll.index(dic)
    UserAll[indexUs]= {'name': Name.get(), 'family': Family.get(), 'age': str(Age.get())}
    if select_row != ():
        tbl.item(select_row,values=[Name.get(),Family.get(),str(Age.get())])
        btn3.place_forget()
        ListItem = [Name, Family, Age]
        Clear(ListItem)

def OnClickTblShow():
    frmTbl.place(x=0,y=0)

def OnClickTblClose():
    frmTbl.place_forget()

def GetValue():
    counter=[]
    for i in range(1,130):
        counter.append(i)
    return counter

#menu
menubar=Menu(screen)
usermenu=Menu(menubar,tearoff=0)
usermenu.add_command(label="افزودن کاربر")
menubar.add_cascade(label="کاربران",menu=usermenu)


screen.config(menu=menubar)

#rdo

jens=IntVar()
rdoZan=Radiobutton(screen,text="خانم",variable=jens,value=-1)
rdoZan.place(x=300,y=150)
rdoMard=Radiobutton(screen,text="اقا",variable=jens,value=2)
rdoMard.place(x=300,y=180)


Check1=IntVar()
Check2=IntVar()
Check3=IntVar()

btnCheck1=Checkbutton(screen,text="کشوری",variable=Check1).place(x=300,y=120)
btnCheck2=Checkbutton(screen,text="استانی",variable=Check2).place(x=300,y=80)
btnCheck3=Checkbutton(screen,text="بین شهری",variable=Check3).place(x=300,y=40)



frmTbl=Frame(screen,width=800,height=400,background="grey")
frmTbl.place(x=0,y=0)
frmTbl.place_forget()


bgTbl=PhotoImage(file="img/Blue Background Images, HD Pictures and Wallpaper For Free Download Pngtree.png")
iconClose=PhotoImage(file="img/icons8-lock-20.png")

lblBg=Label(frmTbl,text="*",image=bgTbl).place(x=0,y=0)
lblClose=Label(frmTbl,text="*",image=iconClose).place(x=150,y=10)
btntblClose=Button(frmTbl,text="*",command=OnClickTblClose,image=iconClose,bg="light blue").place(x=150,y=10)
btntblShow=Button(screen,text="نمایش لیست اسامی",command=OnClickTblShow).place(x=370,y=270)


lblname=Label(screen,text=": نام").place(x=500,y=40)
lblfamily=Label(screen,text=": نام خانوادگی").place(x=500,y=80)
lblage=Label(screen,text=": سن").place(x=515,y=120)

#var

Name=StringVar()
Family=StringVar()
Age=StringVar()

#entry

txt1=Entry(screen,textvariable=Name,justify="right")
txt1.place(x=370,y=40)
txt2=Entry(screen,textvariable=Family,justify="right").place(x=370,y=80)
ComboAge=ttk.Combobox(screen,state="readonly",textvariable=Age,justify="right")
ComboAge.place(x=370,y=120)
ValuesCombo=GetValue()
ComboAge["value"]=ValuesCombo


#btn


btn1=Button(screen,text="ثیت نام",command=OnClickRegister).place(x=370,y=160)
btn2=Button(screen,text="حذف",bg="#D70022",command=OnClickDelete).place(x=460,y=160)
btn3=Button(screen,text="ویرایش",bg="#058B00",command=OnClickEdit)
btn3.place_forget()

#ttk

tbl=ttk.Treeview(frmTbl,columns=("c1","c2","c3"),show="headings",height=10)

tbl.column("# 1",width=50)
tbl.heading("# 1",text="نام")


tbl.column("# 2",width=100)
tbl.heading("# 2",text="نام خانوادگی")


tbl.column("# 3",width=50)
tbl.heading("# 3",text="سن")



tbl.bind("<Button-1>",GetSelction)
tbl.place(x=70,y=40)


txtSearch=Entry(screen)
txtSearch.place(x=370,y=200)
btnSearch=Button(screen,text="جستجو",command=OnClickSearch)
btnSearch.place(x=370,y=235)

lblSearch=Label(screen,text=": مقدار جستجو")
lblSearch.place(x=500,y=200)

screen.mainloop()