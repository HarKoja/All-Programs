class a():
    name=""
    def show(self):
        print("Hello im a")

class b(a):
    family=""
    def show(self):
        print("Hello im b")
    def show_a(self):
        super().show()

obj=b()
obj.show()
obj.show_a()
