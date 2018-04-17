class student:
    def __init__(self,name='default',age=999):
        self.name = name
        self.age = age

    def printer(self):
        print(self.name)
        print(self.age)

a = student('robert jr',55)
#print(type(a))
#a->name = robert jr
#a->age = 55
b = student('brad pitt',47)

#b->brad pitt
#b->age 47
c = student()
a.printer()
b.printer()
c.printer()

