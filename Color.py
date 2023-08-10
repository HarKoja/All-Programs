from tkinter import *
from tkinter import messagebox
from tkinter import ttk


screen=Tk()
screen.title("انتخاب رنگ")
screen.geometry("%dx%d+%d+%d" % (800,400,500,400))
screen.resizable(False,False)

ListALL=[]
def OnClickAdd():
    queryAdd=Color.get()
    if not Exist(queryAdd):
        AddToList(queryAdd)
        LoadData()
    else:
        messagebox.showerror("تکراریه","پاکش کن عامو ")

def AddToList(value):
    ListALL.append(value)

def LoadData():
    for item in tbl.get_children():
        sel=(str(item))
        tbl.delete(sel)
    for item in ListALL:
        tbl.insert('',"end",text="1",values=[str(item)])

def Exist(value):
    for item in ListALL:
        if item==value:
            return True
    return False


Color=StringVar()
txtColor=Entry(screen,textvariable=Color)
txtColor.place(x=50,y=20)

btnAdd=Button(screen,text="افزودن به لیست",command=OnClickAdd).place(x=50,y=55)


tbl=ttk.Treeview(screen,columns=["c1"],show="headings")
tbl.column("#1")
tbl.heading("#1",text="رنگ هات")
tbl.place(x=50,y=90)

screen.mainloop()