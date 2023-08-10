from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Started


#sazande
class App(Frame):
    def __init__(self,screen=None):
        super().__init__(screen)
        self.master=screen
#seda zadn def ha
        self.CreatWidget()
    def CreatWidget(self):
        self.btn1=Button(self.master,text="Click Here",command=self.OnClickHi).pack()
#Event
    def OnClickHi(self):
        print("Hi")

#badane
if __name__=="__main__":
    screen=Tk()
    MyPage=App(screen)
    screen.mainloop()

    pass