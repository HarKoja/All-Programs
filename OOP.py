from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from objRelashen import *

class App(Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.repository = Repository()
        self.CreatWiddget()



    def CreatWiddget(self):
        menubar = Menu(self.master)
        usermenu = Menu(menubar, tearoff=0)
        usermenu.add_command(label="افزودن کاربر")
        menubar.add_cascade(label="کاربران", menu=usermenu)

        self.master.config(menu=menubar)

        # rdo

        self.jens = IntVar()
        self.rdoZan = Radiobutton(self.master, text="خانم", variable=self.jens, value=-1)
        self.rdoZan.place(x=300, y=150)
        self.rdoMard = Radiobutton(self.master, text="اقا", variable=self.jens, value=2)
        self.rdoMard.place(x=300, y=180)

        self.Check1 = IntVar()
        self.Check2 = IntVar()
        self.Check3 = IntVar()

        self.btnCheck1 = Checkbutton(self.master, text="کشوری", variable=self.Check1).place(x=300, y=120)
        self. btnCheck2 = Checkbutton(self.master, text="استانی", variable=self.Check2).place(x=300, y=80)
        self. btnCheck3 = Checkbutton(self.master, text="بین شهری", variable=self.Check3).place(x=300, y=40)

        self. frmTbl = Frame(self.master, width=800, height=400, background="grey")
        self.frmTbl.place(x=0, y=0)
        self.frmTbl.place_forget()

        self.bgTbl = PhotoImage(file="img/Blue Background Images, HD Pictures and Wallpaper For Free Download Pngtree.png")
        self.iconClose = PhotoImage(file="img/icons8-lock-20.png")

        self.lblBg = Label( self.frmTbl, text="*", image= self.bgTbl).place(x=0, y=0)
        self.lblClose = Label( self.frmTbl, text="*", image= self.iconClose).place(x=150, y=10)
        self.btntblClose = Button( self.frmTbl, text="*", command= self.OnClickTblClose, image=self.iconClose, bg="light blue").place(x=150,y=10)
        self.btntblShow = Button(self.master, text="نمایش لیست اسامی", command= self.OnClickTblShow).place(x=370, y=270)

        self.lblname = Label(self.master, text=": نام").place(x=500, y=40)
        self.lblfamily = Label(self.master, text=": نام خانوادگی").place(x=500, y=80)
        self.lblage = Label(self.master, text=": سن").place(x=515, y=120)

        # var

        self.Name = StringVar()
        self.Family = StringVar()
        self.Age = StringVar()

        # entry

        self.txt1 = Entry(self.master, textvariable=self.Name, justify="right")
        self.txt1.place(x=370, y=40)
        self.txt2 = Entry(self.master, textvariable=self.Family, justify="right").place(x=370, y=80)
        self.ComboAge = ttk.Combobox(self.master, state="readonly", textvariable=self.Age, justify="right")
        self.ComboAge.place(x=370, y=120)
        self.ValuesCombo = self.GetValue()
        self.ComboAge["value"] = self.ValuesCombo

        # btn

        self.btn1 = Button(self.master, text="ثیت نام", command= self.OnClickRegister).place(x=370, y=160)
        self.btn2 = Button(self.master, text="حذف", bg="#D70022", command= self.OnClickDelete).place(x=460, y=160)
        self.btn3 = Button(self.master, text="ویرایش", bg="#058B00", command= self.OnClickEdit)
        self.btn3.place_forget()

        # ttk

        self.tbl = ttk.Treeview(self.frmTbl, columns=("c1", "c2", "c3"), show="headings", height=10)

        self.tbl.column("# 1", width=50)
        self.tbl.heading("# 1", text="نام")

        self.tbl.column("# 2", width=100)
        self.tbl.heading("# 2", text="نام خانوادگی")

        self.tbl.column("# 3", width=50)
        self.tbl.heading("# 3", text="سن")

        self.tbl.bind("<Button-1>", self.GetSelction)
        self.tbl.place(x=70, y=40)

        self.txtSearch = Entry(self.master)
        self.txtSearch.place(x=370, y=200)
        self.btnSearch = Button(self.master, text="جستجو", command= self.OnClickSearch)
        self.btnSearch.place(x=370, y=235)

        self.lblSearch = Label(self.master, text=": مقدار جستجو")
        self.lblSearch.place(x=500, y=200)

        self.Loud()



    #function

    UserAll=[]
    def Register(self,User):
        if int(User["age"])>=15:
            if self.Exist(User):
                messagebox.showerror("وجود داره","این کاربر قبلا ثبت شده")
                return False
            else:
                messagebox.showinfo("تمومه","همه چی اوکیه از فردا بیا")
                self.UserAll.append(User)
                return True
        else:
            messagebox.showwarning("بچه سالی","هنوز کوچیکی واسه باشگاه زوده")
            return False

    def OnClickRegister(self):
        name = self.Name.get()
        print(self.Check1.get())
        print(self.Check2.get())
        print(self.Check3.get())
        print(self.jens.get())
        family = self.Family.get()
        age = self.Age.get()
        us = {"name": name, "family": family, "age": age}
        result=self.Register(us)
        if result==True:
            ListItem=[self.Name,self.Family,self.Age]
            self.insertData(ListItem)
            self.Clear(ListItem)

    def Clear(self,ListVal) :
        for item in ListVal:
            item.set("")
            self.txt1.focus_set()

    def insertData(self,Value):
        self.tbl.insert('',"end",text="1",value=[Value[0].get(),Value[1].get(),Value[2].get()])

    def GetSelction(self,e):
        Selction_row=self.tbl.selection()
        if Selction_row != ():
            self.btn3.place(x=540,y=160)
            ListItem = [self.Name, self.Family, self.Age]
            self.Clear(ListItem)
            self.Name.set(self.tbl.item(Selction_row)["values"][0])
            self.Family.set(self.tbl.item(Selction_row)["values"][1])
            self.Age.set(self.tbl.item(Selction_row)["values"][2])

    def OnClickSearch(self):
        query = self.txtSearch.get()
        result = self.Search(query)
        self.CleanTable()
        self.Loud(result)

    def Search(self,Value):
        where = " prs_name Like '%" + Value + "%' or prs_family Like '%" + Value + "%' "
        result = self.repository.Search("personel", "*", where)
        self.CleanTable()
        for item in result:
            self.tbl.insert('', "end", text="1", value=[item["name"], item["family"], item["age"]])

    def Loud(self):
        result = self.repository.Read("personel", "*")
        self.CleanTable()
        for item in result:
            self.tbl.insert('', "end", text="1", value=[item["name"], item["family"], item["age"]])
    def CleanTable(self):
        for item in self.tbl.get_children():
            sel=(str(item))
            self.tbl.delete(sel)
    def Exist(self,Value):
        for item in self.UserAll:
            if Value["age"]==item["age"] and Value["family"]==item["family"] and Value["name"]==item["name"]:
                return True
        return False
    def OnClickDelete(self):
        result=messagebox.askquestion("هشدار","ایا مطمعن هستید میخواهید این داده را حذف کنید")
        print(result)
        if result=="yes":
            self.Delete()
    def Delete(self):
        select_row = self.tbl.selection()
        if select_row!=():
            SelectItem = self.tbl.item(select_row)["values"]
            dic={'name': SelectItem[0],'family': SelectItem[1],'age': str(SelectItem[2])}
            self.tbl.delete(select_row)
            self.UserAll.remove(dic)
    def OnClickEdit(self):
        select_row = self.tbl.selection()
        SelectItem = self.tbl.item(select_row)["values"]
        dic = {'name': SelectItem[0], 'family': SelectItem[1], 'age': str(SelectItem[2])}
        indexUs=self.UserAll.index(dic)
        self.UserAll[indexUs]= {'name': self.Name.get(), 'family': self.Family.get(), 'age': str(self.Age.get())}
        if select_row != ():
            self.tbl.item(select_row,values=[self.Name.get(),self.Family.get(),str(self.Age.get())])
            self.btn3.place_forget()
            ListItem = [self.Name, self.Family, self.Age]
            self.Clear(ListItem)
    def OnClickTblShow(self):
        self.frmTbl.place(x=0,y=0)
    def OnClickTblClose(self):
        self.frmTbl.place_forget()
    def GetValue(self):
        counter=[]
        for i in range(1,130):
            counter.append(i)
        return counter


if __name__=="__main__":
    screen = Tk()
    screen.title("Registering")
    screen.geometry("%dx%d+%d+%d" % (800, 400, 500, 400))
    screen.resizable(False, False)
    MyPage=App(screen)
    screen.mainloop()